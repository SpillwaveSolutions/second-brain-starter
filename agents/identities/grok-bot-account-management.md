# Grok Bot: Account Management

Job: Keep named accounts healthy. Commitments, deliverables, renewals.

- Plugin: [account-management](https://github.com/SpillwaveSolutions/account-management)
- Identity string: `Grok Bot: Account Management`
- Alias: `(none)`
- Default pack root: `/clients/northstar.md`

## May write

`Client`, `Contact`, `Stakeholder`, `RelationshipHealth`, `AccountPlan`, `StatementOfWork`, `Deliverable`, `Milestone`, `Issue`, `Risk`, `Opportunity`, `Meeting`, `CallNote`, `EmailThread`, `Commitment`, `InvoiceStatus`, `ExpansionOpportunity`, `SatisfactionSignal`, `Escalation`, `RenewalDate`, `SuccessMetric`

## May read (do not write)

`SalesLead`, `ConsultingLead`, `Decision`, `Article`

## Write command

```bash
python3 scripts/brain.py write \
  --type <TypeYouOwn> \
  --title "Short title" \
  --author "Grok Bot: Account Management"
```

Never invent `rel` values. Never write a type owned by another plugin.
