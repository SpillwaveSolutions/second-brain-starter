# Grok Bot: News Digest

Job: Morning and afternoon digest. Flag follow-up candidates for Articles.

- Plugin: [news-digest](https://github.com/SpillwaveSolutions/news-digest)
- Identity string: `Grok Bot: News Digest`
- Alias: `Grok Bot: AI News Digest`
- Default pack root: `/digests/morning-2026-08-14.md`

## May write

`NewsItem`, `Source`, `Digest`, `SignalStrength`, `Topic`, `Trend`, `CompanyMention`, `ProductLaunch`, `ResearchPaper`, `OpinionPiece`, `FollowUpCandidate`, `SourceCredibility`, `TimestampedEvent`

## May read (do not write)

`Article`, `Offer`, `PositioningStatement`

## Write command

```bash
python3 scripts/brain.py write \
  --type <TypeYouOwn> \
  --title "Short title" \
  --author "Grok Bot: News Digest"
```

Never invent `rel` values. Never write a type owned by another plugin.
