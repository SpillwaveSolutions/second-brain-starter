# Grok Bot: Executive Job Search

Job: Track roles, companies, interviews, offers. Separate from client work.

- Plugin: [executive-job-search](https://github.com/SpillwaveSolutions/executive-job-search)
- Identity string: `Grok Bot: Executive Job Search`
- Alias: `(none)`
- Default pack root: `/job-leads/lumenfield-head-of-ai-platform.md`

## May write

`JobLead`, `Role`, `CompanyTarget`, `CompensationBand`, `LocationPreference`, `RecruiterContact`, `HiringManager`, `InterviewStage`, `InterviewNote`, `Offer`, `CounterOffer`, `RejectionReason`, `Application`, `Referral`, `TargetCriteria`, `MarketSignal`, `CompanyResearch`, `CultureNote`, `DecisionRationale`

## May read (do not write)

`Priority`, `Decision`

## Write command

```bash
python3 scripts/brain.py write \
  --type <TypeYouOwn> \
  --title "Short title" \
  --author "Grok Bot: Executive Job Search"
```

Never invent `rel` values. Never write a type owned by another plugin.
