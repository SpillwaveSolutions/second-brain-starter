# Second Brain Starter

PUBLIC starter. Fictional sample graph only.

Shared OKF `knowledge/` tree for the eight Grok Bot job functions plus local laptop jobs.
Plugins from [second-brain-marketplace](https://github.com/SpillwaveSolutions/second-brain-marketplace) write here.

## Clone

```bash
git clone https://github.com/SpillwaveSolutions/second-brain-starter.git
cd second-brain-starter
python3 scripts/brain.py doctor
python3 tests/test_brain.py
```


## This is the public fixture

Safe to fork. Every name is fictional (Northstar the account, Lumenfield the employer, Avery Quinn and Jordan Hale the people).

The private working copy lives at `SpillwaveSolutions/grok-bot-knowledge`.


## Quick start

```bash
# Who is this agent?
python3 scripts/brain.py whoami --identity "Grok Bot: Articles"

# Bounded pack (2 hops, ~20 nodes)
python3 scripts/brain.py pack --root "The work is happening you just cannot see it"

# Deterministic write
python3 scripts/brain.py write \
  --type Draft \
  --title "When the decision already happened" \
  --author "Grok Bot: Articles"

# Validate links and owned rels
python3 scripts/brain.py validate
```

## Agent roster

| Identity | Plugin | Pack from |
|----------|--------|-----------|
| `Grok Bot: Executive Assistant` | `executive-coordination` | `/priorities/ship-second-brain-plugins.md` |
| `Grok Bot: Sales` | `sales-pipeline` | `/opportunities/northstar-harness-sprint.md` |
| `Grok Bot: Account Management` | `account-management` | `/clients/northstar.md` |
| `Grok Bot: Executive Job Search` | `executive-job-search` | `/job-leads/lumenfield-head-of-ai-platform.md` |
| `Grok Bot: Consulting Leads` | `consulting-leads` | `/consulting-leads/northstar-platform-team.md` |
| `Grok Bot: Articles` | `content-media` | `/articles/the-work-is-happening.md` |
| `Grok Bot: News Digest` | `news-digest` | `/digests/morning-2026-08-14.md` |
| `Grok Bot: GTM` | `gtm-positioning` | `/positioning/disclosure-not-more-context.md` |
| `Laptop: Articles` | `content-media` | `/drafts/the-work-is-happening.md` |

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
