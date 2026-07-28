# Kimi adversarial review — BOS-0001 rev 2 (exact response)

Date: 2026-07-28
Reviewed commit: f0e95c439262cc046fe1269d7c2fe299daf1557e
Reviewer: bos:actor:model:kimi-k3

Codex справді закрив більшість ударів rev 1: genesis-розділ є, канонічні байти
описані, `supplied_set` замість `read_set`, dirty-cut заборонений схемою
(`"dirty": {"const": false}`), `verification_class` — required у requirement
payload, membership має одну поверхню. Нижче — другий шар атаки.

## 1. Genesis — authority-by-file-edit (головна діра)

§1.2 механічно зводиться до: хтось пише adoption-атом у наступний коміт.
Авторитет — `bos:actor:human:s0fractal`, чий дескриптор каже "cryptographic
binding is deferred". Корінь авторитету = непідписаний git-коміт, який
*стверджує*, що була людська інструкція.

- §1.2(5) "written only after an explicit human instruction" — неверифіковна
  проза. V3 перевірить "adoption names exact revision and authority", але не
  може перевірити факт людської інструкції.
- Будь-який процес з write-доступом до репо — включно з модельним актором —
  може підробити genesis. Це саме той threat model, заради якого існує §11.
- Фікс: adoption-коміт MUST бути GPG/SSH-підписаним ключем, запіненим у
  кандидаті до адопшну, або genesis-якір у Bitcoin/Warrant.

## 2. Таймінгова петля revision ↔ adoption

- Кандидат не має поля `revision`, а §5.2 вимагає його для adopted atom.
  Додавання поля змінює байти → адоптиться об'єкт, відмінний від re-gate-нутого.
  Ритуал появи placeholder-рядка не описаний.
- §5.3 крок 6: "single top-level lexical revision line" — не сказано "within
  frontmatter". Markdown body містить `revision: "sha256:..."` у code fence.
  Два збіги → невизначена поведінка. Також indented/закоментовані збіги.
- LF-only верифікація ламається на `core.autocrlf=true`. Потрібен нормативний
  `.gitattributes` (`*.bos.md text eol=lf`) як частина V0.

## 3. Verb→schema колапс

§2: `evidence` реалізує і OBSERVES, і RECORDS. Схема не розрізняє, яке дієслово
виконує конкретний evidence-атом. "No verb is inferred from prose" — сильніше,
ніж схема дозволяє. Або `mode` у payload, або пом'якшити твердження.

## 4. Реєстр предикатів — внутрішні протиріччя

- `supersedes` structural "carries no confidence" — але суперсесія є
  найбільш оспорюваним твердженням (два успіхори одного попередника).
- Симетричні предикати (`conflicts_with`, `equivalent_to`) у directed-реєстрі
  без семантики симетрії; зворотні дублікати не ловляться.
- `equivalent_to` без resolution-семантики — прихований ID-аліасинг або
  порожній предикат.

## 5. Заборона duplicate IDs ігнорує multi-repo

§5.1: "No mirror exception exists" — але BOS координує репозиторії (множина).
Байтово ідентичний атом у двох репо тепер invalid. Краще: "duplicate IDs
invalid within one declared universe; cross-universe mirrors MUST be
byte-identical".

## 6. Commitment-mode privacy брутфорситься

§12: SHA-256 commitment без nonce/HMAC. Низькоентропійний секрет — словарна
атака; однакові секрети → однакові commitments → кореляція. Треба nonce з
private locator або keyed hash. Також словник `retention` не енумерований.

## 7. Freshness не має зубів

§13: expired claim лише "stale у view". Decision може спиратися на expired
claim — не заборонено. "Watched source commitment" без watcher-реєстру.

## 8. Lifecycle-вісь без жодного значення

Шість осей задекларовано, genesis vocabulary покриває п'ять.
`bos:status:lifecycle:*` не існує. Додавання статусу = adoption схеми —
параліч або тиск ховати стани в payload. Те саме з §7.2 scope.

## 9. Центральний експеримент — поза графом

BOS-E0001 — plain Markdown без frontmatter, не атом, не в includes, не під
revision-алгоритмом. Головний фальсифікаційний механізм невидимий для V1.

## 10. Асиметрія: views декларують universe, validator — ні

§15 вимагає universe від views; вердикти V0–V4 universe не несуть. "V1 passes"
без набору файлів — несуміжний вердикт. Фікс: validator report MUST bind
universe + cut.

## 11. Рубрика §19: disagreement без вердикту

Якщо adjudicator і evaluator розійшлись — pass чи fail? Невизначено.
"Незалежність" трьох траєкторій Phase 2 механічно неперевірювана — має бути
задекларована adjudicated.

## 12. Countervector-атоми — "mechanical" без артефактів

`verification` — англійські речення, не тести. Локація/конвенція fixture-файлів
невизначена. Треба `fixtures:` поле або convention (`tests/countervectors/`).

## Пріоритет виправлень

1. Genesis-аутентифікація (п.1).
2. Ритуал revision-placeholder + frontmatter-scope алгоритму (п.2).
3. BOS-E0001 → атом (п.9).
4. `supersedes` → contestable; симетрія; `equivalent_to` (п.4).
5. Nonce для commitments (п.6).
