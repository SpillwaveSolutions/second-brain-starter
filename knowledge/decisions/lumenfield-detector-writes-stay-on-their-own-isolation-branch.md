---
type: DecisionRecord
title: Lumenfield detector writes stay on their own isolation branch
description: "Lumenfield detector opens brain/claude-code/lumenfield-detector/<sid> before any capture."
status: accepted
tags: [decision, adr]
timestamp: "2026-08-17T02:56:52Z"
verified: true
generated: true
wiki_key: adr-lumenfield-detector-writes-stay-on-their-own-isolation-branch
truth_state: current
author: claude-code/lumenfield-detector
---

# Lumenfield detector writes stay on their own isolation branch

## Context

The detector job must not collide with the console job on the shared tree.

## Decision

Lumenfield detector opens brain/claude-code/lumenfield-detector/<sid> before any capture.

## Consequences

Non-overlapping paths merge independently of the northstar-console session.
