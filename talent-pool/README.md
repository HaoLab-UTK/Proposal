# Talent Pool

A searchable directory of people's CVs and research directions, organized by lab.

## Structure

```
talent-pool/
├── README.md                 # this index
├── resources/                # raw material, one folder per lab (Markdown only)
│   └── <lab-name>/
│       └── <First_Last>.md   # CV or research statement converted to Markdown
└── labs/                     # one summary per lab
    └── <lab-name>.md
```

## Labs

| Lab | PI | Institution | Focus | Members | Summary |
|---|---|---|---|---|---|
| Hao Lab | Yuefeng Hao | University of Tennessee, ISE | AI data center siting, climate extremes & ecohydrology, optimization & decision support | PI + 2 PhD students | [hao-lab.md](labs/hao-lab.md) |

## Adding a Lab or Member

1. Convert the CV or research statement (`.docx` / `.pdf`) to Markdown and save it as `resources/<lab-name>/<First_Last>.md`. Do not commit the original binary files.
2. Create or update `labs/<lab-name>.md` following the sections in [hao-lab.md](labs/hao-lab.md): Overview, Research Directions, Members, Projects & Funding, Ongoing Papers, Collaborators, Expertise Index, TODO.
3. Add or update the lab's row in the table above.
