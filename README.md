# Second Brain Starter

PUBLIC starter. Fictional sample graph only.

Shared OKF `knowledge/` tree for the job-function plugins plus local laptop jobs.
Plugins from [second-brain-marketplace](https://github.com/SpillwaveSolutions/second-brain-marketplace) write here.
**Identity is claimed by the agent (or asked of the human), never shipped in the plugin.**


## Clone

```bash
git clone https://github.com/SpillwaveSolutions/second-brain-starter.git
cd second-brain-starter
python3 scripts/brain.py doctor
python3 tests/test_brain.py
```


## This is the public fixture

Safe to fork. Every name is fictional (Northstar the account, Lumenfield the employer, Avery Quinn and Jordan Hale the people). Point live agents at your own private tree — do not put its location in a public repo.


## Quick start

```bash
# Identity is not hardcoded. Ask, then claim.
python3 scripts/brain.py whoami
python3 scripts/brain.py whoami --claim "Your Name" --plugin content-media

# Bounded pack (2 hops, ~20 nodes)
python3 scripts/brain.py pack --root "The work is happening you just cannot see it"

# Deterministic write (uses the claimed identity if --author is omitted)
python3 scripts/brain.py write \
  --type Draft \
  --title "When the decision already happened"

# Validate links and owned rels
python3 scripts/brain.py validate
```

## Job functions

Plugins own catalogs. Agents claim a signature. The table below is the sample
Northstar fixture, not a required roster.

| Plugin | Sample signature in the fixture | Pack from |
|--------|--------------------------------|-----------|
| `executive-coordination` | `Grok Bot: Executive Assistant` | `/priorities/ship-second-brain-plugins.md` |
| `sales-pipeline` | `Grok Bot: Sales` | `/opportunities/northstar-harness-sprint.md` |
| `account-management` | `Grok Bot: Account Management` | `/clients/northstar.md` |
| `executive-job-search` | `Grok Bot: Executive Job Search` | `/job-leads/lumenfield-head-of-ai-platform.md` |
| `consulting-leads` | `Grok Bot: Consulting Leads` | `/consulting-leads/northstar-platform-team.md` |
| `content-media` | `Grok Bot: Articles` / `Laptop: Articles` | `/articles/the-work-is-happening.md` |
| `news-digest` | `Grok Bot: News Digest` | `/digests/morning-2026-08-14.md` |
| `gtm-positioning` | `Grok Bot: GTM` | `/positioning/disclosure-not-more-context.md` |


## Sample graph (Northstar)

A single fictional story so packs cross plugins:

```
NewsItem  →  FollowUpCandidate  →  Draft  →  Article  →  ConsultingLead
                                              │                 │
                                              ▼                 ▼
                                            Offer          SalesLead → Opportunity → Client
```

Job search (Lumenfield) is a separate track on purpose. Do not fold it into a client pack.

## Install the plugins

```bash
/plugin marketplace add SpillwaveSolutions/second-brain-marketplace
/plugin install content-media@spillwave-second-brain
```

Point every plugin at this repo's `knowledge/` folder.

## License

MIT. Copyright 2026 Rick Hightower / contributors.
