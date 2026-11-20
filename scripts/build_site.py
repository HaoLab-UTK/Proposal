"""Build the data file for the funding tracker website.

Usage:
    python scripts/build_site.py

Reads the scan files, monthly summaries, call index and collaborator registry
and writes docs/data.json, which docs/index.html renders. Run it whenever
those files change and commit docs/data.json in the same commit.
"""

import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
FUNDING = REPO_ROOT / "funding"
OUT = REPO_ROOT / "docs" / "data.json"

SCAN_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")
DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, check=True, capture_output=True, text=True
    ).stdout


def split_row(line):
    cells = line.strip().strip("|").split("|")
    return [c.strip() for c in cells]


def tables(text):
    """Yield (heading, header, rows) for every Markdown table in text."""
    lines = text.splitlines()
    heading = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            heading = line.lstrip("#").strip()
        if (
            line.startswith("|")
            and i + 1 < len(lines)
            and re.match(r"^\|\s*:?-{3,}", lines[i + 1])
        ):
            header = split_row(line)
            rows = []
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                cells = split_row(lines[i])
                if len(cells) == len(header):
                    rows.append(dict(zip(header, cells)))
                i += 1
            yield heading, header, rows
            continue
        i += 1


def first_link(cell):
    m = LINK_RE.search(cell)
    return m.group(2) if m else ""


def fit_score(cell):
    m = re.search(r";\s*(\d)\s*$", cell)
    return int(m.group(1)) if m else None


def parse_doc(path, kind):
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(REPO_ROOT).as_posix()
    title = text.splitlines()[0].lstrip("# ").strip() if text else rel
    calls, ideas = [], []
    for heading, header, rows in tables(text):
        if header[:4] == ["Next Deadline", "Sponsor", "Program", "Award Size"]:
            for r in rows:
                deadline = r["Next Deadline"]
                calls.append(
                    {
                        "deadline_text": deadline,
                        "dates": sorted(set(DATE_RE.findall(deadline))),
                        "rolling": "rolling" in deadline.lower()
                        or "anytime" in deadline.lower(),
                        "sponsor": r["Sponsor"],
                        "program": r["Program"],
                        "award": r["Award Size"],
                        "fit": r.get("Hao Lab Fit (score)", ""),
                        "score": fit_score(r.get("Hao Lab Fit (score)", "")),
                        "team": r.get("Suggested Team", ""),
                        "link": first_link(r.get("Link", "")),
                        "added": r.get("Added", ""),
                        "source": rel,
                        "section": heading,
                    }
                )
        elif header[:3] == ["Call", "Idea", "Verdict"]:
            for r in rows:
                ideas.append(
                    {
                        "call": r["Call"],
                        "idea": r["Idea"],
                        "verdict": r["Verdict"],
                        "why": r.get("One-line why us", ""),
                        "source": rel,
                    }
                )
        elif header[:2] == ["#", "Idea"] and "Verdict" in header:
            call = heading.split(":", 1)[1].strip() if ":" in heading else heading
            for r in rows:
                ideas.append(
                    {
                        "call": call,
                        "idea": f'{r["#"]}. {r["Idea"]}',
                        "verdict": r["Verdict"],
                        "why": r.get("Angle", ""),
                        "source": rel,
                        "short": True,
                    }
                )
    return {
        "file": rel,
        "kind": kind,
        "title": title,
        "date": path.stem if kind == "scan" else "",
        "markdown": text,
    }, calls, ideas


def parse_seen():
    path = FUNDING / "seen-calls.md"
    rows = []
    for _, header, table_rows in tables(path.read_text(encoding="utf-8")):
        if header and header[0] == "First Reported":
            rows.extend(table_rows)
    return rows


def parse_registry():
    path = REPO_ROOT / "talent-pool" / "collaborators.md"
    people = []
    for heading, header, rows in tables(path.read_text(encoding="utf-8")):
        if not header or header[0] != "Name":
            continue
        for r in rows:
            people.append(
                {
                    "name": r["Name"],
                    "affiliation": r.get("Affiliation", ""),
                    "expertise": r.get("Expertise", r.get("Expertise (from joint work)", "")),
                    "evidence": r.get("Evidence (public links)", r.get("Evidence in the PI CV", "")),
                    "recommended_for": r.get("Recommended for", ""),
                    "added": r.get("Added", ""),
                    "status": r.get("Status", ""),
                    "organization": "(organization)" in r["Name"],
                    "group": heading,
                }
            )
    return people


def parse_log():
    out = git(
        "log",
        "--date=iso-strict",
        "--pretty=format:%H%x09%ad%x09%s",
        "--",
        "funding",
        "talent-pool",
        "CLAUDE.md",
    )
    entries = []
    for line in out.splitlines():
        sha, date, subject = line.split("\t", 2)
        s = subject.lower()
        if s.startswith("funding call scan"):
            kind = "scan"
        elif s.startswith("sync talent pool"):
            kind = "sync"
        elif s.startswith("remove old funding scans"):
            kind = "cleanup"
        else:
            kind = "update"
        entries.append({"sha": sha[:7], "date": date, "subject": subject, "kind": kind})
    return entries


def main():
    docs, calls, ideas = [], [], []
    for path in sorted(FUNDING.iterdir()):
        if SCAN_RE.match(path.name):
            d, c, i = parse_doc(path, "scan")
            docs.append(d)
            calls += c
            ideas += i
    for path in sorted((FUNDING / "summaries").glob("*.md")):
        d, c, i = parse_doc(path, "summary")
        docs.append(d)
        calls += c
        ideas += i

    seen = parse_seen()
    for call in calls:
        for row in seen:
            if row.get("URL") and row["URL"] == call["link"]:
                call["number"] = row.get("Solicitation / NOFO No.", "")
                call["first_reported"] = row.get("First Reported", "")
                break

    try:
        head = git("rev-parse", "--short", "HEAD").strip()
    except subprocess.CalledProcessError:
        head = ""
    data = {
        "built": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "commit": head,
        "calls": calls,
        "ideas": ideas,
        "collaborators": parse_registry(),
        "docs": docs,
        "log": parse_log(),
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(
        f"Wrote {OUT.relative_to(REPO_ROOT)}: {len(calls)} calls, {len(ideas)} ideas, "
        f"{len(data['collaborators'])} collaborators, {len(docs)} documents, "
        f"{len(data['log'])} log entries"
    )


if __name__ == "__main__":
    main()
