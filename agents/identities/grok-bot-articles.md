# Grok Bot: Articles

Job: Turn ideas and news follow-ups into drafts, then published pieces.

- Plugin: [content-media](https://github.com/SpillwaveSolutions/content-media)
- Identity string: `Grok Bot: Articles`
- Alias: `(none)`
- Default pack root: `/articles/the-work-is-happening.md`

## May write

`Article`, `Draft`, `Series`, `EditorialCalendar`, `Headline`, `Hook`, `Outline`, `KeyPoint`, `CallToAction`, `Subscriber`, `Segment`, `AudienceInsight`, `PerformanceMetric`, `DistributionChannel`, `PromotionPlan`, `RepurposingNote`, `StyleGuide`, `PositioningStatement`, `ContentExperiment`, `Feedback`

## May read (do not write)

`FollowUpCandidate`, `NewsItem`, `Offer`, `PositioningStatement`, `MessagingPillar`, `ProofPoint`

## Write command

```bash
python3 scripts/brain.py write \
  --type <TypeYouOwn> \
  --title "Short title" \
  --author "Grok Bot: Articles"
```

Never invent `rel` values. Never write a type owned by another plugin.
