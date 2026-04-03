---
title: OpenEnv Delivery
emoji: 🚚
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# 🚚 OpenEnv Delivery Environment

## 📌 Overview
This is a grid-based delivery environment where an AI agent must navigate to delivery locations and complete deliveries efficiently.

The agent interacts using the standard OpenEnv API:
- `/reset`
- `/step`
- `/state`

---

## 🎯 Tasks

### Easy
- Single delivery location
- Small grid
- Max steps: 20

### Medium
- Multiple delivery locations
- Medium grid
- Max steps: 40

### Hard
- Multiple deliveries + complexity
- Larger grid
- Max steps: 60

---

## 🎮 Action Space

Discrete actions:
- `up`
- `down`
- `left`
- `right`

---

## 👀 Observation Space

```json
{
  "agent_position": [x, y],
  "delivery_locations": [[x1, y1]],
  "delivered": [true/false],
  "steps": number
}