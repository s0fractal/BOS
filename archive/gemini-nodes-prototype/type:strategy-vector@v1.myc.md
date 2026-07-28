---
types: [schema@v1.myc.md]
status: active@v1.myc.md
description: "Схема для напрямків стратегії."
schema:
  title: string
  score: number # 0-5
  components: string[] # references to product-features
  solves: string[] # references to market-forces
---
# Strategy Vector Schema

Вектор стратегії — це "молекула", яка поєднує фічі для вирішення ринкових потреб. Вектори оцінюються за потенціалом.
