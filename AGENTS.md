# Agents - Second Brain Starter

You are writing into a shared second brain.

1. **Do not assume a name.** Run `python3 scripts/brain.py whoami`.
2. If nothing is claimed, **ask the user** what to sign as, then
   `python3 scripts/brain.py whoami --claim "Name" --plugin <plugin>`.
3. Load `agents/packing/<plugin-or-role>.md` for the job function you are doing — not a baked-in bot name.
4. Pack first (`scripts/brain.py pack`). Do not slurp the tree.
5. Write only types you own, through `scripts/brain.py write`.
6. Never invent `rel` values. Never use a real client name in the public starter.

The model proposes. The script commits. Identity is claimed, never hardcoded.
