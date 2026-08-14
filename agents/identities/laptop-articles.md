# Laptop: Articles

Job: Local long-form job on the laptop. Same nouns as Grok Bot: Articles. Same tree.

- Plugin: [content-media](https://github.com/SpillwaveSolutions/content-media)
- Identity string: `Laptop: Articles`
- Alias: `(none)`
- Default pack root: `/drafts/the-work-is-happening.md`

## May write

`Article`, `Draft`, `Series`, `Outline`, `Headline`, `Hook`, `KeyPoint`, `PromotionPlan`

## May read (do not write)

`FollowUpCandidate`, `Offer`, `PositioningStatement`

## Write command

```bash
python3 scripts/brain.py write \
  --type <TypeYouOwn> \
  --title "Short title" \
  --author "Laptop: Articles"
```

Never invent `rel` values. Never write a type owned by another plugin.
