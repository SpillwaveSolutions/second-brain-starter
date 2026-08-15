# Agent identities

Identity is **not** a property of a plugin. The agent using the plugin decides
who it is, or asks the human, then claims that string.

```bash
python3 scripts/brain.py whoami
python3 scripts/brain.py whoami --claim "Maya" --plugin content-media
# or export SECOND_BRAIN_IDENTITY="Maya"
```

`brain.py write` refuses to commit until an identity is claimed (`--author`,
env, or `knowledge/.identity.json`). There is no default `Grok Bot: …` author.

A plugin is a **job function**. Optional role templates live in
`agents/registry.json` as examples (how the sample Northstar graph was signed).
They are not assignments. You may sign as anything.

| Job function (plugin) | Sample signature in the fixture | Default pack root |
|-----------------------|---------------------------------|-------------------|
| `executive-coordination` | `Grok Bot: Executive Assistant` | `/priorities/ship-second-brain-plugins.md` |
| `sales-pipeline` | `Grok Bot: Sales` | `/opportunities/northstar-harness-sprint.md` |
| `account-management` | `Grok Bot: Account Management` | `/clients/northstar.md` |
| `executive-job-search` | `Grok Bot: Executive Job Search` | `/job-leads/lumenfield-head-of-ai-platform.md` |
| `consulting-leads` | `Grok Bot: Consulting Leads` | `/consulting-leads/northstar-platform-team.md` |
| `content-media` | `Grok Bot: Articles` / `Laptop: Articles` | `/articles/the-work-is-happening.md` |
| `news-digest` | `Grok Bot: News Digest` | `/digests/morning-2026-08-14.md` |
| `gtm-positioning` | `Grok Bot: GTM` | `/positioning/disclosure-not-more-context.md` |

See `agents/registry.json` and `agents/identities/` for those sample templates.
