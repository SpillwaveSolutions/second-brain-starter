# Agents - Second Brain Starter

You are writing into a shared second brain.

1. **Do not assume a name.** Run `python3 scripts/brain.py whoami`.
2. If nothing is claimed, **ask the user** what to sign as, then
   `python3 scripts/brain.py whoami --claim "Name" --plugin <plugin>`.
3. Load `agents/packing/<plugin-or-role>.md` for the job function you are doing — not a baked-in bot name. For Q&A fan-out, load `agents/packing/retrieval.md`.
4. **Retrieve, then write.** For Q&A against the knowledge tree, spawn the owning pack’s retriever (or a short-lived child Task) and consume only a Retrieval card. Do not run full search/pack inline in the parent turn for Q&A. `scripts/brain.py pack` remains valid for tiny local checks inside that child, or when no retriever exists yet. Do not slurp the tree.
5. Write only types you own, through `scripts/brain.py write`.
6. Never invent `rel` values. Never use a real client name in the public starter.

See `docs/RETRIEVAL.md` for the four foundation retrievers and the shared card fields.

The model proposes. The script commits. Identity is claimed, never hardcoded.
