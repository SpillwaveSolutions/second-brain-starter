# Cursor on this starter tree

Grok Bot often opens a **Cursor cloud agent against this knowledge tree**,
not against a plugin repo. This file is the binding for that session.

## What Cursor sees here

- `AGENTS.md` / `CLAUDE.md`
- `scripts/brain.py`
- packing prompts under `agents/packing/`
- `.cursor/rules/second-brain.mdc` (always on)

It does **not** automatically have `content-media` or any other plugin
installed. Do not wait for `/plugin install`. Follow the write protocol.

## Protocol

1. Claim identity with `python3 scripts/brain.py whoami --claim "…"`.
2. Load the packing prompt for the job (`agents/packing/…`).
3. Write only via `python3 scripts/brain.py write`.
4. Never dump the tree. Never invent a private remote.

Local Cursor users who want pack skills can still:

```text
/plugin marketplace add SpillwaveSolutions/second-brain-marketplace
/plugin install content-media
```

That is optional. The protocol above is not.

See also [grok-bot.md](grok-bot.md).
