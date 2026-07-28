---
types: [value@v0.myc.md]
status: active@v1.myc.md
priority: critical
domain: [architecture, process, management]
enforces:
  - rule: "has_spec(node) == true before node.status == 'implementation@v1.myc.md'"
  - requires: [docs-as-code-linter@v1.myc.md]
---
# Spec-First Підхід (Spec-Driven Development)

## Суть цінності
Ми спочатку проектуємо та описуємо систему (Specification), і лише потім пишемо код. Це дозволяє знаходити архітектурні помилки до їх реалізації, економить час розробників і гарантує, що розроблена система відповідає початковим вимогам. 

Markdown у цьому Vault (як цей самий файл) і є нашою специфікацією. Це **Single Source of Truth**.

## Стратегічні наслідки (Process Restrictions)
Будь-який `feature@v1.myc.md` має починатися зі статусу `draft@v1.myc.md` і переходити в статус `spec-approved@v1.myc.md` **ДО** того, як з'явиться перший рядок коду (або PR). 

Якщо лінтер виявить код, що імплементує фічу без затвердженої специфікації, процес CI/CD буде заблоковано, оскільки це порушує Spec-First підхід.
