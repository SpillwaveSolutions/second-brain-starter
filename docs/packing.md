# Packing

Do not load the whole second brain.

For Q&A, the parent spawns a retriever (or a short-lived child Task) and
consumes a Retrieval card only. Do not run full search/pack inline in the
parent turn. See `docs/RETRIEVAL.md` and `agents/packing/retrieval.md`.

`scripts/brain.py pack` remains valid for tiny local checks **inside** that
child, or when no retriever exists yet:

```bash
python3 scripts/brain.py pack --root /articles/the-work-is-happening.md --hops 2 --max-nodes 20
```

Each agent has a packing prompt in `agents/packing/` that names:

- the identity lock
- nouns it may write
- nouns it may only read
- a default root

Rank: root, then verified (decisions, signed SOWs, published articles), then high-impact (next actions, blockers, offers).
