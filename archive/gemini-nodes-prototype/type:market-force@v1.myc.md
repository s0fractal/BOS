---
types: [schema@v1.myc.md]
status: active@v1.myc.md
description: "Схема для вузлів типу Market Force. Описує зовнішні фактори, що впливають на стратегію компанії."
schema:
  title: string
  urgency: number # 1-5
  deadline: string # ISO format optional
  impact_area: string[]
---
# Market Force Schema

Вузли цього типу представляють неконтрольовані зовнішні сили (закони, тренди, конкуренти).
