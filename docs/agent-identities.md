# Agent identities

Format: `Grok Bot: <Role>` for hosted agents, `Laptop: <Role>` for local jobs.

The role is a job function. It owns a ContentPack plugin. It does not own the tree.

| Identity | Plugin | Default pack root |
|----------|--------|-------------------|
| `Grok Bot: Executive Assistant` | `executive-coordination` | `/priorities/ship-second-brain-plugins.md` |
| `Grok Bot: Sales` | `sales-pipeline` | `/opportunities/northstar-harness-sprint.md` |
| `Grok Bot: Account Management` | `account-management` | `/clients/northstar.md` |
| `Grok Bot: Executive Job Search` | `executive-job-search` | `/job-leads/lumenfield-head-of-ai-platform.md` |
| `Grok Bot: Consulting Leads` | `consulting-leads` | `/consulting-leads/northstar-platform-team.md` |
| `Grok Bot: Articles` | `content-media` | `/articles/the-work-is-happening.md` |
| `Grok Bot: News Digest` | `news-digest` | `/digests/morning-2026-08-14.md` |
| `Grok Bot: GTM` | `gtm-positioning` | `/positioning/disclosure-not-more-context.md` |
| `Laptop: Articles` | `content-media` | `/drafts/the-work-is-happening.md` |

`Grok Bot: AI News Digest` is an alias of `Grok Bot: News Digest`.

See `agents/registry.json` and `agents/identities/`.
