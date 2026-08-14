# Wiring Grok Bots

Each hosted agent gets three things:

1. **Name** exactly matching the identity string (`Grok Bot: Articles`).
2. **Instructions** that paste or `@`-include `agents/packing/<slug>.md`.
3. **Repo access** to this knowledge tree (the private working copy, not only the public starter).

Suggested Grok Bot roster:

| Bot name in the UI | Packing prompt |
|--------------------|----------------|
| Grok Bot: Executive Assistant | `agents/packing/grok-bot-executive-assistant.md` |
| Grok Bot: Sales | `agents/packing/grok-bot-sales.md` |
| Grok Bot: Account Management | `agents/packing/grok-bot-account-management.md` |
| Grok Bot: Executive Job Search | `agents/packing/grok-bot-executive-job-search.md` |
| Grok Bot: Consulting Leads | `agents/packing/grok-bot-consulting-leads.md` |
| Grok Bot: Articles | `agents/packing/grok-bot-articles.md` |
| Grok Bot: AI News Digest | `agents/packing/grok-bot-news-digest.md` |
| Grok Bot: GTM | `agents/packing/grok-bot-gtm.md` |

The laptop Articles job uses `agents/packing/laptop-articles.md` and the same `knowledge/` folder.

After a bot drafts something, it must call `scripts/brain.py write`. A reply that only lives in the Grok thread is not captured.
