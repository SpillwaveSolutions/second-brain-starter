# Articles workflow

Shared path for `Grok Bot: Articles` and `Laptop: Articles`.
Both write the same `knowledge/` tree through `content-media`.

## Trigger

A `FollowUpCandidate` from `Grok Bot: News Digest`, a GTM request, or a human "write this up".

## Loop

1. Pack the candidate plus GTM positioning:

```bash
python3 scripts/brain.py pack --root /follow-up-candidates/write-the-disclosure-piece.md --hops 2
```

2. Capture a `Draft` (and optional `Outline`, `Headline`, `Hook`, `KeyPoint`).
   Author is `Grok Bot: Articles` or `Laptop: Articles`.

3. Human edits the draft in git. The agent does not silently overwrite.

4. On publish, capture an `Article` that:
   - `belongs_to` a `Series`
   - `originates_from` the `Draft` and the `FollowUpCandidate`
   - `promotes` an `Offer` when the piece is commercial
   - `engaged_with` a `Subscriber` or `Segment` when you have one

5. After it is live, a local job may add `PerformanceMetric`, `PromotionPlan`, `RepurposingNote`.

## Channels

Public pieces currently live on:

- https://rickhigh.substack.com/p/the-work-is-happening-you-just-cannot
- https://rickhigh.substack.com/p/when-the-decision-already-happened
- https://medium.com/@richardhightower/open-knowledge-format-agents-dont-need-more-context-they-need-better-disclosure-35a0587df812

The second brain stores the typed record. The channel stores the rendered post.

## Local laptop job

On the laptop, Claude Code or Codex uses this same repo:

```bash
/plugin marketplace add SpillwaveSolutions/second-brain-marketplace
/plugin install content-media@spillwave-second-brain
python3 scripts/brain.py write --type Draft --title "..." --author "Laptop: Articles"
```

Do not keep a second copy of drafts in chat, Notion, or a scratch folder.
