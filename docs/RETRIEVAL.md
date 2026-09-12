# Query-time retrieval

Do not run full search or pack in the parent turn for Q&A.

Foundation packs ship `*-retriever` agents. The parent **spawns** the owning
retriever (or a short-lived child Task) and keeps a **Retrieval card** only.
Hit lists, mermaid, and neighbor bodies stay in the child so they never
contaminate working context.

This starter tree is the knowledge checkout. Plugins are not installed here
automatically. When a retriever is present, spawn it. When it is not, spawn a
child Task and let that child run `scripts/brain.py pack` (tiny first). The
parent still consumes only the card.

## Foundation retrievers

Packs are the source of truth for each retriever contract.

| Pack | Retriever | Skill / command | Spawn when the question is about |
|------|-----------|-----------------|----------------------------------|
| PKC — [project-knowledge-capture](https://github.com/SpillwaveSolutions/project-knowledge-capture) | `knowledge-retriever` | `/pkc-retrieve` | Feature, DecisionRecord, Meeting, Experiment, Question, TicketLink |
| SAC — [system-architecture-capture](https://github.com/SpillwaveSolutions/system-architecture-capture) | `architecture-retriever` | `/sac-retrieve` | Service, ApiContract, Package, Runtime, Pipeline, IdentityProvider, blast radius |
| DEKC — [data-engineering-knowledge-capture](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture) | `data-retriever` | `/dekc-retrieve` | Table, Metric, LineagePath, IngestionJob, Transformation, Dashboard, DataProduct, GlossaryTerm, BusinessObject |
| RKC — [research-knowledge-capture](https://github.com/SpillwaveSolutions/research-knowledge-capture) | `research-retriever` | `/research-retrieve` | ResearchQuestion, Finding, Claim, Evidence, Subject, SourceDocument |

Fan out in parallel when the question crosses planes. Do not impersonate
another pack’s retriever.

The shared host rule will live at
[second-brain-core `docs/RETRIEVAL.md`](https://github.com/SpillwaveSolutions/second-brain-core/blob/main/docs/RETRIEVAL.md)
(may land in parallel). If that file is not on `main` yet, follow the
foundation packs.

## Shared card fields

Every retriever returns this shape. Pack-specific extras (Engine, Critical
edges, Lineage note, Spine) may appear after these:

```markdown
## Retrieval card
- Query: …
- Seed: `/path` (`Type`) — why chosen
- Fit: high|medium|low — one sentence
- Pack: hops=N nodes=N tokens=N/budget
- Lead nodes: (5–8 bullets: title · type · path · one-line why)
- Open gaps: … or none
- Next: stay|deepen-2hop|try-alt-seed `/other`
```

Answer from the card. If `Next` is `deepen-2hop` or `try-alt-seed` and the
user still needs more, spawn again. Still do not pull raw packs into the
parent.

`scripts/brain.py pack` remains valid for tiny local checks **inside** that
child, or when no retriever exists yet. It is not a parent-turn Q&A tool.

Public samples stay Northstar / Lumenfield. Never name a private remote.

See `agents/packing/retrieval.md` for when to fan out.
