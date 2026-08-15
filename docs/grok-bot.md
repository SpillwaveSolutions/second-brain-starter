# Wiring hosted agents

A hosted Grok Bot (or Claude / Codex job) is **your** named agent. The plugin
does not name it.

Each hosted agent needs three things:

1. **A name you choose.** Claim it with `python3 scripts/brain.py whoami --claim "…"`.
2. **Instructions** that include: do not assume an identity; ask if unknown;
   then load the packing prompt for the *plugin* you are using
   (`agents/packing/…`).
3. **Repo access** to this knowledge tree (the private working copy, not only
   the public starter).

Optional sample packing prompts (job functions, not required names):

| Job function | Packing prompt |
|--------------|----------------|
| Executive coordination | `agents/packing/grok-bot-executive-assistant.md` |
| Sales | `agents/packing/grok-bot-sales.md` |
| Account management | `agents/packing/grok-bot-account-management.md` |
| Executive job search | `agents/packing/grok-bot-executive-job-search.md` |
| Consulting leads | `agents/packing/grok-bot-consulting-leads.md` |
| Articles / content | `agents/packing/grok-bot-articles.md` |
| News digest | `agents/packing/grok-bot-news-digest.md` |
| Go-to-market | `agents/packing/grok-bot-gtm.md` |
| Local articles job | `agents/packing/laptop-articles.md` |

After a bot drafts something, it must call `scripts/brain.py write` with a
claimed identity. A reply that only lives in the chat thread is not captured.
