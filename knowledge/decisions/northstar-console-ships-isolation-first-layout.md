---
type: DecisionRecord
title: Northstar console ships isolation-first layout
description: Northstar console records author + session id on every knowledge write before it renders a pack.
status: accepted
tags: [decision, adr]
timestamp: "2026-08-17T02:56:52Z"
verified: true
generated: true
wiki_key: adr-northstar-console-ships-isolation-first-layout
truth_state: current
author: grok-bot/northstar-console
---

# Northstar console ships isolation-first layout

## Context

Two agents share one second brain. The console must show which session owns a write.

## Decision

Northstar console records author + session id on every knowledge write before it renders a pack.

## Consequences

Operators can tell lumenfield-detector writes from northstar-console writes without opening git.
