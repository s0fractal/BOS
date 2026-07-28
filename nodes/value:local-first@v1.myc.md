---
types: [value@v0.myc.md]
status: active@v1.myc.md
priority: critical
domain: [architecture, user-experience]
# Машинно-читабельні обмеження (Contracts)
enforces:
  - rule: "user_data_location == local"
  - requires_capabilities: [offline-first, sync-engine]
  - forbids_dependencies: [cloud-only-db]
---
# Local-First Підхід

## Суть цінності (Human Context)
Ми фундаментально вважаємо, що дані користувача належать користувачу. Застосунок має миттєво реагувати на дії без очікування мережевих запитів. Мережа — це опція для синхронізації та колаборації, а не обов'язкова умова для базової роботи. 

Цей підхід гарантує приватність, швидкість та незалежність від стабільності інтернету.

## Стратегічні наслідки (Strategic Implications)
Будь-який новий `feature@v1.myc.md` або `architecture-decision@v1.myc.md`, який проектується в цій системі, **повинен** задовольняти правила, описані в блоці `enforces` у Frontmatter.

Якщо архітектурне рішення порушує цю цінність (наприклад, вимагає постійного з'єднання з сервером для рендерингу UI), оркестратор стратегії позначатиме такий вузол як `invalid`, поки конфлікт не буде вирішено або явно задокументовано через `error@v0.myc.md` (як свідомий компроміс).

## Машинні перевірки (Execution Hooks / Code-as-Data)
Ось приклад того, як цей файл може містити логіку для зовнішнього валідатора (наприклад, який біжить в CI або локальному watcher'і):

```python run="strategy-linter"
def validate_node(node):
    if "requires_connection" in node.properties and node.properties["requires_connection"] == True:
        return {
            "valid": False, 
            "reason": f"Порушено цінність [[{__file__}]]: архітектура вимагає з'єднання"
        }
    return {"valid": True}
```
