"""Detect changes under talent-pool/resources since the last Markdown sync.

Usage:
    python scripts/resources_sync.py check   # exit 0 = changed, 1 = unchanged
    python scripts/resources_sync.py mark    # record the current state as synced

The state file stores the git tree hash of the resources folder and the
commit it was taken from, so only committed content is compared.
"""

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RESOURCES = "talent-pool/resources"
STATE_FILE = REPO_ROOT / "talent-pool" / ".resources-sync.json"


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()


def load_state():
    if not STATE_FILE.exists():
        return None
    return json.loads(STATE_FILE.read_text())


def check():
    tree = git("rev-parse", f"HEAD:{RESOURCES}")
    state = load_state()
    if state and state["tree"] == tree:
        print("No changes in resources since last sync.")
        return 1
    if state:
        print(f"Resources changed since {state['commit'][:7]} ({state['date']}):")
        print(git("diff", "--name-status", state["commit"], "HEAD", "--", RESOURCES))
    else:
        print("No sync state found; treat all resources as changed:")
        print(git("ls-files", RESOURCES))
    return 0


def mark():
    state = {
        "tree": git("rev-parse", f"HEAD:{RESOURCES}"),
        "commit": git("rev-parse", "HEAD"),
        "date": git("log", "-1", "--format=%cs", "HEAD"),
    }
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")
    print(f"Marked resources tree {state['tree'][:7]} as synced.")
    return 0


if __name__ == "__main__":
    commands = {"check": check, "mark": mark}
    if len(sys.argv) != 2 or sys.argv[1] not in commands:
        print(__doc__)
        sys.exit(2)
    sys.exit(commands[sys.argv[1]]())
