---
types: [schema@v1.myc.md]
status: active@v1.myc.md
description: "Схема для вузлів типу Product Feature. Описує компоненти, які ми створюємо."
schema:
  title: string
  solves: string[] # references to market-forces or user-needs
  complexity: string # low, medium, high
  dependencies: string[] # references to other features
---
# Product Feature Schema

Вузли цього типу описують конкретні продукти або фічі, які відповідають на зовнішні виклики.
