# Architecture

The second brain is a git repo, not a product database.

```
agents/                 identity + packing prompts (procedural memory)
knowledge/              OKF Markdown + YAML (institutional memory)
scripts/brain.py        deterministic write / pack / validate
```

Session chat is working memory. It dies with the tab.
Packs are how working memory borrows institutional memory without eating the tree.

## Write boundary

| Who | Does |
|-----|------|
| Model | Proposes type, title, body, links |
| `brain.py write` | Commits frontmatter against the type registry |
| Human | Reviews the git diff |

An agent that writes a type it does not own is a bug. The script rejects it when the author is a known identity for a different plugin.

## Packs

Outbound BFS. Default 2 hops, about 20 nodes. Same contract as PKC / SAC / DEKC.
