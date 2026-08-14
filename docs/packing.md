# Packing

Do not load the whole second brain.

```bash
python3 scripts/brain.py pack --root /articles/the-work-is-happening.md --hops 2 --max-nodes 20
```

Each agent has a packing prompt in `agents/packing/` that names:

- the identity lock
- nouns it may write
- nouns it may only read
- a default root

Rank: root, then verified (decisions, signed SOWs, published articles), then high-impact (next actions, blockers, offers).
