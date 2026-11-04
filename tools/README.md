# 🛠️ أدوات مركز القيادة

| الأداة | وظيفتها | الاستخدام |
|---|---|---|
| `inventory-scan.py` | ماسح جرد قراءة فقط؛ يحفظ **لقطة تاريخية** للمستودعات والمهارات وملفات env وworkflows للمقارنة | `export GH_TOKEN=... && python3 tools/inventory-scan.py` |
| `portfolio_report.py` | تقرير GitHub حي read-only للـrepos والفروع الأساسية وPRs والرؤوس وdraft state وchecks؛ لا يكتب حالة إلى ملفات المركز | `python3 tools/portfolio_report.py` أو `--json` |
| `skill_gate.py` | فحص metadata وحالات Canary المكتوبة؛ لا يدّعي تشغيل وكيل AI | `python3 tools/skill_gate.py` |
| `validate-center.py` | فحص بنية المركز والروابط المحلية وعدم حذف الوثائق | `python3 tools/validate-center.py --base-ref <SHA>` |

**قاعدة المصدر:** `portfolio_report.py` يقرأ GitHub في وقت التشغيل. لا تُنسخ مخرجاته تلقائياً إلى `README.md` أو `PROJECTS.md`؛ هذه الملفات تحمل الملكية والنطاق والقرارات، بينما حالة GitHub الحية تبقى في المصدر نفسه أو في إخراج مؤقت يوسم بزمن الفحص.

**قاعدة الأمان:** الأدوات read-only افتراضياً. لا تسجل token في المستودع أو remote أو التقارير. إن احتاج GitHub إلى وصول مصادق، مرر credential من متغير بيئي مؤقتاً (`GITHUB_TOKEN`) ولا تحفظه.

## تقرير المحفظة الحي

```bash
# public API؛ سيظهر NOT VERIFIED عند private/404/403 أو فشل الشبكة
python3 tools/portfolio_report.py
python3 tools/portfolio_report.py --json > /tmp/command-center-portfolio.json

# وصول اختياري من البيئة فقط؛ لا قيمة افتراضية داخل الكود
GITHUB_TOKEN="$TOKEN" python3 tools/portfolio_report.py
```

يتضمن التقرير `checked_at`، اسم المستودع، الفرع الأساسي وSHA إن أمكن، PR number/title/head/branch/base/draft، وحالة check-runs إن أمكن. `NOT VERIFIED` تعني أن الأداة لم تثبت الحقيقة؛ لا تعني أن repo غير موجود. التقرير لا يفتح أو يغلق أو يدمج أو يدفع أي شيء.

## فحص المركز قبل التسليم

من جذر المستودع:

```bash
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/validate-center.py --base-ref <SHA-البداية-المتوفر-محلياً>
git diff --check
```

الأداة `validate-center.py` لا تحتاج شبكة أو مفتاحاً ولا تغير الملفات.
تفحص وجود ملفات البداية، الروابط المحلية المباشرة في وثائق التشغيل،
بيانات المهارات الأساسية وتطابق الاسم مع المجلد، وعدم اختفاء أي وثيقة
كانت موجودة في commit البداية. تنتهي برمز 1 عند الفشل.

بدون `--base-ref` تُصرّح بأن فحص الحذف لم يتم. SHA غير متاح يفشل صراحةً.
فحص الروابط لا يشمل الروابط المرجعية أو عناوين الأقسام أو الإنترنت؛ التقارير
التاريخية لا تُفحص روابطها القديمة، لكن مساراتها محمية بفحص الحذف.
فحص المهارات ليس محلل YAML عاماً؛ يدعم صيغة name/description أحادية السطر
المستخدمة في هذه المكتبة. لا يثبت تحميل الوكيل للمهارات أو مزامنة المشاريع.

## بوابة جودة المهارات

```bash
python3 tools/skill_gate.py
python3 tools/skill_gate.py --downstream ../kiyyal/.agents/skills --require frontend-rtl-design
python3 -m unittest discover -s tools -p 'test_*.py'
```

الأولى تفحص بنية المراجع و26 حالة Canary **مكتوبة فقط**؛ لا تشغّل وكيل AI. الثانية تقارن النسخ المشتركة المتاحة مقارنة حرفية؛ المهارات الاختيارية المفقودة لا تعتبر خطأ. تفاصيل التجارب الحقيقية في [بروتوكول الجودة](../skills/QUALITY_PROTOCOL.md). workflow الموجود في `.github/workflows/skills-quality.yml` يصبح بوابة مستودع فعلية فقط بعد دمجه وتحقق GitHub منه؛ وجوده في الفرع لا يثبت حماية `main`.
