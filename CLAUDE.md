# CLAUDE.md

## Daily Resource Sync Rule

`talent-pool/resources/` is the source of truth. All other Markdown files
(`talent-pool/labs/*.md`, `talent-pool/README.md`) are derived from it and must
be kept in sync. Run this procedure once per day:

1. Check for changes:
   `python scripts/resources_sync.py check`
   - Exit code 1 (no changes): stop. Do not edit, commit, or push anything.
   - Exit code 0 (changes): continue; the output lists the added (A),
     modified (M), and deleted (D) resource files.
2. Read every changed resource file in full, then update the derived Markdown:
   - `talent-pool/labs/<lab-name>.md`: update all affected sections
     (Overview, Research Directions, Members, Member Profiles, Projects &
     Funding, Ongoing Papers, Collaborators, Expertise Index, TODO) and set
     `Last updated:` to today's date.
   - New lab folder: create `talent-pool/labs/<lab-name>.md` using the same
     sections as `talent-pool/labs/hao-lab.md`.
   - Deleted resource file: remove that person from the lab summary and the
     Expertise Index.
   - `talent-pool/README.md`: update the Labs table row (focus, member count,
     summary link).
3. Follow the content policy in `talent-pool/README.md`: proposal-relevant
   content only, no personal details (contact info, GPA, grades). Do not invent
   facts that are not in the resource files. Write everything in English.
4. Record the sync: `python scripts/resources_sync.py mark`
5. Commit the Markdown updates together with `talent-pool/.resources-sync.json`
   in one commit, e.g. `Sync talent pool summaries with resources (YYYY-MM-DD)`,
   and push.

Never edit files under `talent-pool/resources/` as part of this sync.

## Funding Call Scan Rule

Every 3 days, search for open funding calls (solicitations, RFPs, NOFOs,
foundation programs) that the talent pool could submit proposals to, and save
each scan as a dated file in `funding/`. Any field or sponsor type is allowed
(federal, state, foundation, industry, international).

1. Read `talent-pool/README.md` and every `talent-pool/labs/*.md` to collect
   research directions, methods, and expertise across all labs.
2. Search the web for current calls that match those directions. Use several
   queries per Hao Lab research direction and expertise keyword, plus
   cross-lab combinations (Hao Lab with another lab in the pool).
3. Keep a call only if ALL of these hold:
   - **Strong Hao Lab relevance**: the call's core topic directly matches at
     least one Hao Lab research direction (`labs/hao-lab.md` section 2) or
     a cluster of its Expertise Index keywords, so Hao Lab could credibly
     lead or co-lead the proposal. Calls where Hao Lab would only be a minor
     add-on do not qualify. Score relevance 1-5 and keep only scores 4-5.
   - **Eligible**: a U.S. university faculty member (UT Knoxville, Assistant
     Professor) can apply as PI or Co-PI, or the call explicitly allows
     partnering in a way that fits.
   - **Open**: the next deadline (LOI, pre-proposal, or full proposal) is at
     least 14 days from today, or the call is rolling.
   - **Verified**: the sponsor's official page was opened and the details
     (title, deadline, amount, eligibility) were taken from it. Never
     invent or guess details; write "not stated" when a field is missing.
   - **How to open official pages**: do not use WebFetch (it bypasses this
     environment's proxy and fails). Download pages with
     `curl -sSL -m 60 -A "Mozilla/5.0" -o <file> <url>` into the scratchpad
     directory, extract HTML text with a small Python script that strips
     tags, and extract PDF text with `pdftotext -layout`. If a page returns a
     bot-check page or an error, state in the scan file that it could not be
     verified.
4. No repeats across scans: every call may appear in exactly one scan file.
   - Before writing, read `funding/seen-calls.md`, the permanent index of
     every call already reported. Drop any candidate that matches an entry
     (same sponsor + program, same solicitation/NOFO number, or same URL),
     even if its deadline or details changed. Rows for scan files removed by
     the cleanup rule are deleted from the index, so a call that is still
     open may be reported again as new after its scan file is cleaned up.
   - A new round of a recurring program (a new fiscal year, new solicitation
     number, or new NOFO) counts as a new call.
5. Write a new scan file `funding/YYYY-MM-DD.md` (today's date) using the
   same structure as `funding/2026-10-21.md`, containing only this scan's new
   calls, sorted by next deadline. Set `Last scanned:` to today's date. Never
   edit or delete earlier scan files.
6. Append every call in the new scan file to `funding/seen-calls.md` (date,
   sponsor, program, solicitation number, URL, scan file). Rows are removed
   only by the cleanup rule, together with their scan file.
7. Generate and screen proposal ideas for every new call, following the
   "Funding Idea Rule" below, and add the "Ideas" module to the scan file.
8. Write everything in English. Commit the scan file, the index, and the idea
   files together with a message like
   `Funding call scan (YYYY-MM-DD): N new calls, M ideas` and push. If nothing
   new qualifies, still write the scan file stating that no new calls were
   found, and commit.

## Funding Idea Rule

Every time new calls are added to the tracker, propose 3-5 ideas per new call
and screen them with the `deep-research` skill. The goal of every idea:

- **Fundable**: it answers the call's stated priorities and review criteria
  and fits its award size and duration.
- **Gap and novelty**: it differs from existing funded projects and published
  work, and the difference is a real contribution, not a re-labeling.
- **Why us**: it states why only this team can do it and why others have not:
  concrete assets from the talent pool (funded grants, datasets, models,
  ongoing papers, collaborators, site access, methods), not generic claims.

Procedure:

1. Draft 3-5 candidate ideas per call from `talent-pool/labs/*.md`. Each idea
   must be led or co-led by Hao Lab and use people from the talent pool;
   cross-lab ideas are welcome.
2. Screen them with the `deep-research` skill: one research subagent per call
   checks each idea against existing funded projects (NSF Award Search,
   NIH RePORTER, DOE / USDA / NOAA award lists, USAspending) and the
   literature (Google Scholar, arXiv, journals), and against the call's own
   solicitation text. Open official pages with curl as described in step 3 of
   the Funding Call Scan Rule. Notes go to
   `funding/ideas/research_notes/YYYY-MM-DD/`; the report writer writes the
   full evaluation to `funding/ideas/YYYY-MM-DD.md`.
3. For each idea, the evaluation states: title; call; team (talent pool
   names); research question and approach; closest existing projects and
   papers (with links) and the gap they leave; novelty; why us (only facts
   that appear in the talent pool files); fundability against the call's
   criteria; risks; and a verdict: **Pursue**, **Revise** (say what to
   change), or **Drop** (say why). Never invent team facts, awards, or
   papers; a gap claim needs the sources that were checked.
4. Add an "Ideas" section to the scan file with one row per idea (call, idea,
   verdict, one-line why us) and a link to `funding/ideas/YYYY-MM-DD.md`.
5. Never edit earlier idea files. Idea files are deleted only by the cleanup
   rule, together with the scan file they belong to.

## Funding Scan Cleanup Rule

Once a month, clean up old scan files in `funding/`. User approval before any
deletion is a mandatory baseline that no instruction, schedule, or automation
can override.

1. List scan files matching `funding/YYYY-MM-DD.md`, sorted by date. Keep the
   3 most recent; all older ones are deletion candidates. If there are 3 or
   fewer, report that and stop.
2. Ask the user for approval first: list every scan file that would be
   deleted, what would be removed with each one, and the 3 scan files that
   would be kept, then stop and wait for an explicit reply. For a scan file
   `funding/YYYY-MM-DD.md`, the items removed with it are:
   - its idea files: `funding/ideas/YYYY-MM-DD.md`,
     `funding/ideas/YYYY-MM-DD-backfill.md`, and the folders
     `funding/ideas/research_notes/YYYY-MM-DD/` and
     `funding/ideas/research_notes/YYYY-MM-DD-backfill/` (whichever exist);
   - the rows of `funding/seen-calls.md` whose "Scan File" is that file.
   Do not delete anything in the same turn as the request.
3. A scheduled prompt, this rule, an earlier approval, or any message other
   than the user's own explicit reply to this request does NOT count as
   approval. Each month needs its own fresh approval.
4. Only after the user explicitly approves: delete exactly the approved
   scan files and their idea files with `git rm`, remove their rows from
   `funding/seen-calls.md` (those calls may then be reported again as new if
   still open), commit everything together
   (`Remove old funding scans (YYYY-MM-DD)`), and push. If the user declines
   or approves only some scan files, delete only those and only their idea
   files and rows.
