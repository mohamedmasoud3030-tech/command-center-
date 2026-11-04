# 🏛️ مركز قيادة المشاريع

> ابدأ هنا لمعرفة المطلوب منك. الوكيل يبدأ من [AGENTS.md](AGENTS.md).
> تحديث الحوكمة: 2026-11-04. سجل التشغيل الحي منفصل عن التقارير التاريخية؛ هذه الجولة تدير المركز فقط ولا تعيد اختبار كود المنتجات.

## ابدأ في دقيقة

| عايز تعمل إيه؟ | افتح |
|---|---|
| تبدأ جلسة وكيل على مشروع | [برومبت البداية](prompts/START-HERE.md) |
| تعرف وصف وحالة وخطوة كل مشروع | [خريطة المشاريع](PROJECTS.md) |
| تختار قواعد تنفيذ المهمة | [توجيه المهارات](skills/README.md) |
| تستأنف شغل سابق | [فهرس التسليم](reports/handoffs/INDEX.md) |
| تتأكد إن المركز سليم | [أدوات الفحص](tools/README.md) |

**جملة البداية الجاهزة:**
> ابدأ بقراءة ريبو mohamedmasoud3030-tech/command-center- — اقرأ AGENTS.md وPROJECTS.md وسجل الجلسات في README.md، ثم اقرأ تعليمات وحالة ومهارات ريبو المشروع. أعلن المهارات التي قرأتها وحدود المهمة. أي تعديل يمر من PR قابل للمراجعة، وممنوع حذف الوثائق.

## Command Center v2 — السجل الحي وطريقة التشغيل

> **Checked:** 2026-11-04. هذا الجزء هو طبقة الحقائق التشغيلية الحالية. التقارير المؤرخة ولقطات الجرد تظل تاريخاً لا يُستنسخ منه وضع حي. حالة GitHub الحالية تُقرأ من GitHub مباشرة عبر [`tools/portfolio_report.py`](tools/portfolio_report.py)؛ لا ننسخ حالة PR يدوياً إلى عشر ملفات.

### سجل الملكية الحالي — المرجع الوحيد للجلسات

| المهمة | المشروع / الفرع / PR | النطاق | المالك والخطوة التالية |
|---|---|---|---|
| **Command Center v2 — في المراجعة** | `command-center-` / `feat/skills-quality-gate-2026-11-04` / [PR #5](https://github.com/mohamedmasoud3030-tech/command-center-/pull/5) | PR #3/#4 استُوعبا وأُغلقا؛ بوابة Skills، تقرير المحفظة، ونظام المهام؛ **لا كود منتجات** | المالك صاحب قرار الدمج؛ الخطوة التالية مراجعة الديف والفحوص والحماية على الرأس الحالي. لا merge/deploy تلقائي |
| **جلسات المنتجات** | Kiyyal PR #26–#29، MALEK #1844، Nilesys #19/#30، Mosaid #9/#14 | أعمال محفوظة خارج نطاق هذه الجلسة | ليست حجوزات تنفيذ هنا؛ الوكيل الذي يعمل عليها يسجل task tuple في مركز القيادة |
| **جلسات موازية** | لا توجد حجوزات تنفيذ مفوضة في هذا السجل | لا نقرأ PR مفتوحاً باعتباره جلسة حية | يعاد التحقق قبل كل كتابة |

**Task tuple إلزامي:** `project + objective + paths + owner + branch + PR + base SHA + handoff + next action`؛ استخدم [`templates/TASK.md`](templates/TASK.md).
فتح PR أو وجود فرع لا ينقل ملكية جلسة ولا يثبت أن أحداً يعمل عليه.

### حسم تداخل PRs المركز — P0

لا نفتح PR رابعاً لتعديل `README.md` و`reports/handoffs/INDEX.md`.
تم تنفيذ القرار: PR #5 هو **هدف التجميع الوحيد**، واستُوعبت فيه التغييرات الفريدة من #3 و#4 عبر merge عادي قابل للمراجعة؛ بعد النشر وفحص `contracts=success` أُغلقت #3 و#4 باعتبارهما superseded، من غير حذف فروعهما.

> **آخر تحقق لهذه الصفوف:** بعد نشر consolidation head في PR #5؛ الحالة التفصيلية والرؤوس والـchecks تُعاد قراءتها من GitHub/التقرير الحي.

| PR | ما يضيفه فعلاً | التداخل | القرار التشغيلي |
|---|---|---|---|
| [#3 MALEK](https://github.com/mohamedmasoud3030-tech/command-center-/pull/3) | محضر MALEK + سطر سجل + handoff index | `README.md` و`handoffs/INDEX.md` | **Closed / superseded**؛ المحتوى محفوظ في #5؛ لا حذف للـhandoff أو الفرع |
| [#4 Kiyyal](https://github.com/mohamedmasoud3030-tech/command-center-/pull/4) | تصحيح الاسم الرسمي Kiyyal + handoff CI | `README.md` و`PROJECTS.md` و`handoffs/INDEX.md` | **Closed / superseded**؛ Kiyyal خارج تنفيذ المركز؛ لا حذف للفرع |
| [#5 Skills](https://github.com/mohamedmasoud3030-tech/command-center-/pull/5) | `QUALITY_PROTOCOL`، canaries، `skill_gate`، workflow، قالب PR، وطبقة v2 | `README.md` و`PROJECTS.md` و`handoffs/INDEX.md` | **Draft / open**؛ `contracts=success`؛ ينتظر مراجعة المالك ولا merge تلقائي |

### محفظة المشاريع — live مقابل التاريخ

هذه **قائمة ملكية ونطاق** وليست نسخة من حالة GitHub. أرقام PR أدناه هي work items المطلوب متابعتها، أما open/draft/head/checks فتُقرأ لحظياً من التقرير ولا تُحرّر يدوياً في README أو `PROJECTS.md`.

| المشروع | المستودع المرجعي | نطاق المتابعة |
|---|---|---|
| Kiyyal | [`mohamedmasoud3030-tech/kiyyal`](https://github.com/mohamedmasoud3030-tech/kiyyal) | PR #26–#29؛ متابعة فقط، لا تعديل منتج من مركز القيادة |
| MALEK | [`mohamedmasoud3030-tech/malek`](https://github.com/mohamedmasoud3030-tech/malek) | PR #1844؛ المراجعة والـhosted/QA خارج المركز |
| Nile Systems | [`mohamedmasoud3030-tech/nilesys`](https://github.com/mohamedmasoud3030-tech/nilesys) | PR #19 و#30؛ قرار الإصدار منفصل |
| Mosaid | [`mohamedmasoud3030-tech/mosaid`](https://github.com/mohamedmasoud3030-tech/mosaid) | PR #9 و#14؛ لا إعادة تأسيس من المركز |
| بقية مشاريع LENA وTerranex وHospitality | الروابط والـslugs في [`PROJECTS.md`](PROJECTS.md) | canonical link والملكية فقط؛ أي 404/403 يبقى **NOT VERIFIED** |

شغّل التقرير الحي من جذر المركز:

```bash
python3 tools/portfolio_report.py
python3 tools/portfolio_report.py --json > /tmp/command-center-portfolio.json
```

### خطة v2 المعتمدة

| الأولوية | العمل | بوابة الخروج |
|---|---|---|
| P0 | دمج #3/#4 داخل #5 وإغلاق التكرار | PR واحد يملك كل تغيير المركز؛ لا ملفات سجل متنافسة |
| P0 | فصل live facts عن التاريخ | live registry في `PROJECTS.md` وREADME؛ التقارير القديمة معلّمة تاريخية |
| P1 | توحيد task/agent lifecycle | task tuple + PR template + handoff index + reservation قبل الكتابة |
| P1 | اعتماد Skills protocol | المسار الفعلي + trigger + أثر مطبق + proof؛ canary spec لا يدّعي activation |
| P1 | ضبط PR lifecycle | overlap review، base SHA، checks، unresolved/blocked، ولا merge تلقائي |
| P2 | متابعة آلية للمحفظة | `tools/portfolio_report.py` يقرأ GitHub ويعرض NOT VERIFIED صراحةً |
| P2 | حماية main والإصدار | مراجعات PR وrequired checks ورفض force-push تُفعّل من إعدادات GitHub بصلاحية المالك؛ المركز لا يدّعي أنه فعلها |

### دورة الوكيل الموحدة

1. **استلام:** سجّل task tuple والهدف وحدود التفويض.
2. **تحقق:** اقرأ هذا المركز، المشروع، GitHub الحالي، والـbase SHA.
3. **Skills:** اختر أصغر مجموعة، اقرأ الملفات الفعلية، وسجّل المسارات؛ لا تعتبر الاسم دليلاً.
4. **تنفيذ:** فرع مستقل؛ افحص التداخل قبل الكتابة؛ لا تلمس منتجاً خارج النطاق.
5. **مراجعة:** diff أولاً، ثم الفحوص المناسبة، ثم صنّف ما لم يُتحقق.
6. **تسليم:** PR واحد واضح، handoff مفهرس، أول خطوة تالية، وقرار owner مطلوب إن وجد.

## إزاي نقرأ الحالة؟

| الوصف | معناه |
|---|---|
| مبلّغ | مكتوب في تقرير أو تسليم؛ لم يُتحقق منه في هذه الجلسة |
| متحقق | له مصدر حديث وتاريخ وSHA عند الحاجة |
| مدموج | GitHub يؤكد الدمج؛ لا يعني النشر |
| منشور | دليل نشر للنسخة المعنية؛ لا يعني نجاح الاستخدام الحقيقي |
| مُجرّب فعلياً | رحلة مستخدم موثقة على النسخة والبيئة المقصودتين |
| قديم / غير متحقق | يحتاج إعادة فحص قبل البناء عليه |

## التاريخ محفوظ

- [لقطة المركز قبل هذا التحسين](reports/2026-10-24-center-baseline.md): لوحة المالك وعقد الوكيل السابقان كاملان.
- [محاضر التسليم](reports/handoffs/INDEX.md): أدلة مؤرخة وليست حجوزات دائمة.
- ملفات `reports/README.md` و`reports/PROJECTS.md` ولقطات `data/inventory-*.json` تاريخية؛ المرجع الحي هو الملفات الموجودة في جذر المستودع.
- لا حذف للوثائق. تعديلات المهارات تبدأ في المركز وتصل للمشاريع عبر PRs مستقلة مع إثبات المصدر.


## آخر تحقق للمهارات — 2026-10-24

فُحصت المشاريع العشرة عند commits مثبتة: **112 نسخة مشتركة موجودة مطابقة للأصل، صفر اختلاف**. إضافة release-readiness لكيّال ومساعد مقترحة في PRs أعلاه ولم تُدمج بعد. الأرقام تقيس تطابق الملفات الموجودة، ولا تثبت أن كل مهارة مطلوبة لكل مهمة متاحة أو تم تحميلها. [التقرير والحدود](reports/handoffs/2026-10-24-skills-audit.md).

