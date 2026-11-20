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
5. Run `python3 scripts/build_site.py`, then commit the Markdown updates
   together with `docs/data.json`, `talent-pool/.resources-sync.json`
   (and `talent-pool/collaborators.md` if new co-authors or co-PIs were added
   to it) in one commit, e.g. `Sync talent pool summaries with resources
   (YYYY-MM-DD)`, and push.

Never edit files under `talent-pool/resources/` as part of this sync.

## Tracker Website Rule

`docs/` is the funding tracker website (GitHub Pages). `docs/index.html` is
static; `docs/data.json` is generated from `funding/` and
`talent-pool/collaborators.md` by `scripts/build_site.py`.

- The website updates with every repository update: the workflow
  `.github/workflows/pages.yml` runs `scripts/build_site.py` on every push
  to `main` (including edits made on GitHub) and deploys `docs/` to Pages.
  Every run that changes the repository must push to `main` so the website
  follows; never leave such a change only in the local checkout.
- Before every commit that changes `funding/`, `talent-pool/` or this file
  (daily sync, funding scan, cleanup, registry update), run
  `python3 scripts/build_site.py` and include `docs/data.json` in the same
  commit. Never edit `docs/data.json` by hand.
- The website is public. Put nothing in the tracked Markdown files that should
  not be public (the content policy in `talent-pool/README.md` already
  excludes personal details).
- If the scan file layout changes (table headers such as "Next Deadline |
  Sponsor | Program | Award Size", "Call | Idea | Verdict", "# | Idea | ... |
  Verdict", or the registry "Name" tables), update `scripts/build_site.py` so
  the website keeps parsing them.

## Funding Call Scan Rule

Every 3 days, search for open funding calls (solicitations, RFPs, NOFOs,
foundation programs) that the talent pool could submit proposals to, and save
each scan as a dated file in `funding/`. Any field or sponsor type is allowed
(federal, state, foundation, industry, international).

1. Read `talent-pool/README.md` and every `talent-pool/labs/*.md` to collect
   research directions, methods, and expertise across all labs.
2. Search the web for current calls that match those directions. Use several
   queries per Hao Lab research direction and expertise keyword, plus
   cross-lab combinations (Hao Lab with another lab in the pool). Do not stop
   at Grants.gov and agency sites; every scan must also cover:
   - **Sub-award programs of funded centers and networks**: small, seed, or
     pilot grant programs run by NSF Science and Technology Centers,
     Engineering Research Centers, AI Institutes, and other NSF/DOE/NOAA/USGS
     funded centers (for example CLaSH, CUAHSI, CSDMS, NIDIS/RISA teams,
     Climate Adaptation Science Centers, DOE national lab programs). These
     never appear on Grants.gov.
   - **Societies, consortia, foundations, industry, and state programs**
     (for example AGU, GSA, ASCE/EWRI, AWRA, INFORMS, EPRI, TVA, state
     agencies, university internal and seed programs).
   - **Adjacent vocabulary**: translate each direction into the terms other
     communities use (e.g., flash drought, flood, wildfire, landslide ->
     "land surface hazards", "hazard cascades", "compound hazards"; data
     centers -> "large loads", "critical infrastructure", "AI
     infrastructure") and search those terms too, combined with "small grant
     program", "seed grant", "pilot grant", "RFP", and "call for proposals".
   - The lessons in "Search lessons" below.
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
     even if its deadline or details changed. When the cleanup rule removes
     a scan file, rows of calls that are still open are kept (pointing to the
     monthly summary) and only rows of closed calls are deleted.
   - A new round of a recurring program (a new fiscal year, new solicitation
     number, or new NOFO) counts as a new call.
5. Write a new scan file `funding/YYYY-MM-DD.md` (today's date), containing
   only this scan's new calls, sorted by next deadline. Use this structure:
   title, `Last scanned:` line (today's date), a verification note, a
   "New Calls" table (Next Deadline | Sponsor | Program | Award Size |
   Hao Lab Fit (score) | Suggested Team | Link | Added), "Call Notes" with
   one block per call, the ideas sections from the Funding Idea Rule, and
   "Considered but not listed". The monthly summary in `funding/summaries/`
   shows the content to expect. Never edit or delete earlier scan files.
6. Append every call in the new scan file to `funding/seen-calls.md` (date,
   sponsor, program, solicitation number, URL, scan file). Only the cleanup
   rule changes or removes rows.
7. Generate and screen proposal ideas for every new call, following the
   "Funding Idea Rule" below, and write them into the scan file right after
   each call.
8. Write everything in English. Run `python3 scripts/build_site.py`. Commit
   `docs/data.json`, the scan file, the index, the
   research notes folder, and any change to `talent-pool/collaborators.md`
   together with a message like
   `Funding call scan (YYYY-MM-DD): N new calls, M ideas` and push. If nothing
   new qualifies, still write the scan file stating that no new calls were
   found, and commit.

## Funding Idea Rule

Every time new calls are added to the tracker, propose ideas for each new call
(see step 2 for how many) and screen them with the `deep-research` skill. The goal of every idea:

- **Fundable**: it answers the call's stated priorities and review criteria
  and fits its award size and duration.
- **Gap and novelty**: it differs from existing funded projects and published
  work, and the difference is a real contribution, not a re-labeling.
- **Why us**: it states why only this team can do it and why others have not:
  concrete assets from the talent pool (funded grants, datasets, models,
  ongoing papers, collaborators, site access, methods), not generic claims.

Procedure:

1. Study past winners first: find the projects the same program funded in
   earlier rounds (award lists, abstracts, project pages, NSF Award Search),
   and summarize in a "Past winners" paragraph what they have in common
   (topics, scale, methods, team makeup, partners, framing, budget) and why
   they were likely selected. Use those patterns to shape the ideas; if no
   past awards can be found, say so.
2. Draft a wide set of candidate ideas per call from `talent-pool/labs/*.md`
   and the collaborator registry: at least 8 short ideas (2-4 lines each)
   spanning different perspectives — methods (observation, modeling, AI,
   optimization, decision support), scales (site to national), sectors and
   users, disciplines (including social science, policy, education), and
   cross-lab or new-partner teams. Each idea must be led or co-led by Hao
   Lab. Then screen all of them briefly and evaluate the 2-4 strongest in
   full.
3. Screen them with the `deep-research` skill: one research subagent per call
   checks each idea against existing funded projects (NSF Award Search,
   NIH RePORTER, DOE / USDA / NOAA award lists, USAspending) and the
   literature (Google Scholar, arXiv, journals), and against the call's own
   solicitation text. Open official pages with curl as described in step 3 of
   the Funding Call Scan Rule. Research notes go to `funding/ideas/YYYY-MM-DD/`
   (the scan date); `funding/ideas/` holds only these notes folders. The
   report writer drafts the evaluation in the scratchpad directory, not in
   the repository.
4. For each fully evaluated idea, the evaluation states: title; call; team (talent pool
   names); research question and approach; closest existing projects and
   papers (with links) and the gap they leave; novelty; why us (only facts
   that appear in the talent pool files); fundability against the call's
   criteria; risks; and a verdict: **Pursue**, **Revise** (say what to
   change), or **Drop** (say why). Never invent team facts, awards, or
   papers; a gap claim needs the sources that were checked.
5. Write the ideas into the scan file: in "Call Notes", put a
   `#### Ideas: <call>` subsection right after each call's notes, with one
   `#####` heading per idea. After all calls, add an "Ideas Overview" section
   with a summary table (call, idea, verdict, one-line why us), which call
   should host which idea (flag duplicate-submission and overlap risks), open
   items, and a link to the notes folder `funding/ideas/YYYY-MM-DD/`.
   Under each call, list the short ideas in a table (idea, angle, verdict)
   and give the fully evaluated ideas their own `#####` headings; add the
   "Past winners" paragraph and the "Recommended collaborators" section
   from the Collaborator Rule.
6. Never edit earlier notes folders. Only the cleanup rule deletes notes,
   and only notes of calls that have closed.

## Collaborator Rule

For every new call, recommend co-PIs and partner organizations that would
strengthen the proposals, and keep them in a collaborator registry so later
scans can reuse them without the registry becoming fixed.

1. Start from the collaborator registry `talent-pool/collaborators.md` (it
   holds the PI's past collaborators, status "Past collaborator", and people
   recommended in earlier scans; when the daily resource sync finds new
   co-authors or co-PIs in the resource files, add them there too), then
   search for new people and organizations. Base the search on the kinds of
   partners the PI already works with (see `labs/hao-lab.md` Collaborators
   and the PI CV: national lab Earth system modelers, UT optimization and
   decision-support faculty, hydrology and remote sensing groups) and extend
   to the expertise each idea is missing.
2. More than half of the people recommended for each call must be new (not
   already in the registry). If not enough suitable new people can be found,
   say so explicitly and explain why; only then fill the remaining slots from
   the registry.
3. Rank candidates with these weights, and show the reasons:
   - **High**: has won awards in the same or a similar program (link the
     award), or fills a gap the call requires (e.g., an installation,
     extension, utility, or social-science partner).
   - **Medium-high**: background different from the Hao Lab team — other
     disciplines, institution types (minority-serving, EPSCoR, primarily
     undergraduate, national lab, agency, industry), career stage, region,
     or country. Gender diversity may count only when a person states it
     publicly themselves (e.g., pronouns on their own profile); never infer
     gender from names or photos.
   - **Medium**: complementary methods, nearby location or shared field
     sites, existing ties to the call's sponsor or center.
4. Use only public, professional information (name, title, affiliation,
   public profile page, research areas, funded awards, publications). No
   email addresses, phone numbers, or other personal details. Never claim a
   person has agreed to anything.
5. In the scan file, add a "Recommended collaborators" section under each
   call: a table (name, affiliation, role in the proposal such as co-PI or
   partner, expertise, evidence with links, why recommended, new or from
   registry).
6. Add every recommended person or organization to
   `talent-pool/collaborators.md` with status "Recommended", the calls they
   were recommended for, and the date. Every change to the registry is committed
   and pushed to GitHub (`git push origin main`) in the same run that makes
   it; a registry change must never stay only in the local checkout. Only the user changes a status to
   "Contacted" or "Confirmed". Confirmed collaborators may be used in "why
   us" claims only for facts in their registry entry that came from public
   sources.

## Search lessons

Missed calls the user pointed out, and what to do so similar calls are found:

- 2026-11-19 — CLaSH Small Grant Program 2026-27 (NSF Center for Land
  Surface Hazards; seed grants of $20K-$40K; due 2027-01-15). Missed because
  scans searched Grants.gov and agency pages, and a center's own sub-award
  program never appears there; and because the program speaks of "land
  surface hazard cascades" (landslides, floods, fire), not the lab's terms
  (flash drought, heatwave, wildfire). Fix: search center and network seed
  programs and adjacent vocabulary every scan (step 2 above).

## Funding Scan Cleanup Rule

Once a month, clean up old scan files in `funding/`. User approval before any
deletion is a mandatory baseline that no instruction, schedule, or automation
can override. Cleanup removes reports, not content: everything about a call
that is still open is kept in a monthly summary.

1. List scan files matching `funding/YYYY-MM-DD.md`, sorted by date. Keep the
   3 most recent; all older ones are deletion candidates. If there are 3 or
   fewer, report that and stop.
2. Sort every call in the candidate files into **open** (next deadline today
   or later, or rolling) or **closed**, checking the official page with curl.
   Do the same for calls carried in earlier monthly summaries that are still
   marked open.
3. Ask the user for approval first, then stop and wait for an explicit reply.
   List: the scan files that would be deleted; for each, which calls are open
   (kept) and which are closed (removed); the files that would be deleted
   with them (notes of closed calls under `funding/ideas/YYYY-MM-DD/`); the
   `funding/seen-calls.md` rows that would be removed (closed calls only);
   and the 3 scan files that would be kept. Do not delete anything in the
   same turn as the request.
4. A scheduled prompt, this rule, an earlier approval, or any message other
   than the user's own explicit reply to this request does NOT count as
   approval. Each month needs its own fresh approval.
5. Only after the user explicitly approves:
   - Write or update the monthly summary `funding/summaries/YYYY-MM.md` (the
     month of the scans being removed): activity, all calls with status,
     ideas to pursue, overlap rules, upcoming dates, watch list, and, for
     every open call, a "Carried over: scan YYYY-MM-DD" section with that
     call's full call notes and idea evaluations from the scan file (links
     adjusted for the new location). Closed calls get one line each.
   - Keep the notes of open calls in `funding/ideas/YYYY-MM-DD/` and link
     them from the summary; delete only the notes of closed calls (and the
     folder, if it becomes empty).
   - In `funding/seen-calls.md`, point the rows of open calls to the summary
     (Scan File `summaries/YYYY-MM.md`) and delete the rows of closed calls.
   - Delete the approved scan files with `git rm`.
   - Run `python3 scripts/build_site.py`.
   - Commit everything together (`Remove old funding scans (YYYY-MM-DD)`) and
     push. If the user approves only some scan files, handle only those.
6. Monthly summaries are permanent; cleanup never deletes them. When a call
   carried in a summary closes, the next approved cleanup deletes its notes
   and its `seen-calls.md` row and marks it closed in the summary.
