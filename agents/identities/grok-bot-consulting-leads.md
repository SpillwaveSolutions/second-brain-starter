# Grok Bot: Consulting Leads

Job: Qualify inbound consulting interest against Spillwave offers.

- Plugin: [consulting-leads](https://github.com/SpillwaveSolutions/consulting-leads)
- Identity string: `Grok Bot: Consulting Leads`
- Alias: `(none)`
- Default pack root: `/consulting-leads/northstar-platform-team.md`

## May write

`ConsultingLead`, `EngagementType`, `Scope`, `BudgetRange`, `Timeline`, `DecisionMaker`, `QualificationNote`, `Proposal`, `StatementOfWork`, `DiscoveryCall`, `Objection`, `Competitor`, `WinLossReason`, `ReferralSource`, `CapabilityMatch`

## May read (do not write)

`Article`, `Offer`, `PositioningStatement`, `Client`

## Write command

```bash
python3 scripts/brain.py write \
  --type <TypeYouOwn> \
  --title "Short title" \
  --author "Grok Bot: Consulting Leads"
```

Never invent `rel` values. Never write a type owned by another plugin.
