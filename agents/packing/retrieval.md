# Packing prompt — query-time retrieval

This is a **job function**, not a named bot. Load this page when the user asks
a question against the knowledge tree.

1. Run `python3 scripts/brain.py whoami`.
2. If nothing is claimed, **ask the user** what to sign as, then
   `python3 scripts/brain.py whoami --claim "Name" --plugin <plugin>`.
3. Then retrieve. Do not pack inline in this parent turn.

## When to fan out

Spawn the owning pack’s retriever (Claude Code Task / host child). Consume
**only** the Retrieval card. See `docs/RETRIEVAL.md` for the shared fields.

| Question is about | Retriever | Skill |
|-------------------|-----------|-------|
| Decisions, Features, Meetings, Experiments, Questions, TicketLinks | PKC `knowledge-retriever` | `/pkc-retrieve` |
| Services, APIs, packages, runtimes, pipelines, IdP, blast radius | SAC `architecture-retriever` | `/sac-retrieve` |
| Tables, metrics, lineage, jobs, dashboards, data products, glossary | DEKC `data-retriever` | `/dekc-retrieve` |
| ResearchQuestion, Finding, Claim, Evidence, Subject, SourceDocument | RKC `research-retriever` | `/research-retrieve` |

Cross-plane questions (why + what-is-running + data + research) spawn the
matching retrievers **in parallel**. Do not impersonate another pack.

This starter checkout does not install those plugins automatically. If the
retriever is missing, spawn a short-lived child Task. That child may run:

```bash
python3 scripts/brain.py pack --root "<seed-or-title>" --hops 1 --max-nodes 8
```

and must still return a Retrieval card only. Deepen (2 hops / ~20 nodes) is a
second spawn, not a parent dump.

## What the parent keeps

```markdown
## Retrieval card
- Query: …
- Seed: `/path` (`Type`) — why chosen
- Fit: high|medium|low — one sentence
- Pack: hops=N nodes=N tokens=N/budget
- Lead nodes: (5–8 bullets)
- Open gaps: … or none
- Next: stay|deepen-2hop|try-alt-seed `/other`
```

Do not paste search hit lists, mermaid, or neighbor bodies into this turn.

## Writes

Retrieval does not write. If the answer requires a new node, load the owning
job-function prompt under `agents/packing/` and write through
`scripts/brain.py write`. Never invent `rel` values. Public samples stay
Northstar / Lumenfield.
