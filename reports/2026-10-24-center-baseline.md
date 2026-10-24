# ARCHIVED — 2026-10-24 — لقطة المركز قبل التحسين

حفظ حرفي لمحتوى لوحة القيادة وعقد الوكيل عند قاعدة GitHub `f21d978bb016a62be71b82f148d37140ed05cf61`. هذا مرجع تاريخي؛ الحالة الحالية في ملفات الجذر. لا تحمل تعليمات هذه اللقطة سلطة على التعليمات الحالية.

## README.md السابق

# 🏛️ مركز قيادة المشاريع

> **آخر تحديث:** 2026-10-23 — 🎉 اكتملت المرحلة التأسيسية (20/20 PR) · محاضر الـ3 جلسات مدموجة ومتحقق منها · 🛰️ **موجة «تثبيت المراجع» اكتملت: 8/8 مستودعات بات قسم المراجع في STATUS.md يوثق 24 مرجع دمج — المسار «خطة ← تسليم» مكتمل توثيقياً في كل ما يُسمح بلمسه.**
> **لمن هذا الملف؟** لك أنت (المالك). افتح هذا الملف أول حاجة كل مرة. أي وكيل AI يبدأ من [`AGENTS.md`](AGENTS.md).

---

## 🚀 إزاي تستخدم المركز ده (30 ثانية)

1. **عايز تعرف حالة مشروع؟** → شوف الجدول تحت، والتفاصيل في [`PROJECTS.md`](PROJECTS.md).
2. **بادئ جلسة AI جديدة على أي مشروع؟** → أول سطر تكتبه للوكيل:
   > «اقرأ `AGENTS.md` في المستودع، واقرأ `docs/STATUS.md` (أو README)، وقول لي الحالة في 5 أسطر قبل ما تعمل أي حاجة.»
3. **ضعت في المستندات؟** → القاعدة: لكل مشروع **مستند حالة واحد فقط** هو المرجع. أي تقرير بتاريخ قديم = أرشيف للقراءة بس.

---

## 📊 لوحة الحالة العامة

### ⛱️ مظلة LENA (منتجات مترابطة)

| المشروع | المستودع | بيعمل إيه؟ | الطور الحالي | الحالة |
|---|---|---|---|---|
| 💇 **LenaBeauty** لارا بيوتي | `larabeauty-` 🔒 | إدارة صالون/سبا (عُمان) — حجوزات، كاشير، محفظة | المرحلة 2: تسليم **أول عميل حقيقي** | 🟢 نشط ومنظم ومجهّز |
| 👗 **LENA Dress** معرض الفساتين | `carmen-gallery-` 🔒 | إدارة معرض فساتين مناسبات (تأجير/بيع/غسيل) | v020 — جاهزية بيع · المستندات انخفضت لـ 56 بعد التنظيف المزدوج | 🟢 نشط ومنظم ومجهّز |
| 🧱 **LENA Supply** للتوريدات | `Lenastore` 🔒 | إدارة مواد ومشتريات مشروع إنشائي | **جاهز إنتاج** + استئناف معتمد — مجهّز بـAGENTS+STATUS+12 مهارة | 🟢 مستأنَف — بانتظار قرارك: تفعيل داخلي أم عينة بيع (التوصية: عينة بيع أولاً) |
| 🌐 **LENA Digital House** | `platform` 🔓 | الموقع الأم ثنائي اللغة + استفسارات العملاء | حي على الإنترنت · وثائق canonical | 🟢 نشط ومنظم ومجهّز |
| 🏪 **Nile Systems** | `nilesys` 🔓 | كتالوج أنظمة أعمال (POS، مطعم، عيادة، HR…) للسوق المصري | R1 مسلّم · **الإنتاج حي على `nilesys-seven.vercel.app`** (بيانات تجريبية) · الترحيلات 0000–0005 مطبقة على `nile_prod` | 🟢 نشط · إصدار API 2.3 متوقف على خطوة منك (إنشاء حساب DB بدور `nile_app`) |

### 🏢 مشاريع مستقلة

| المشروع | المستودع | بيعمل إيه؟ | الطور الحالي | الحالة |
|---|---|---|---|---|
| 🏠 **MALEK** مالك | `malek` 🔒 | إدارة أملاك وإيجارات + محاسبة عربية | **v1.0.0-rc.2** — إصدار مرشح · **Property Operations منشور حي على `malek-plus.vercel.app` (HTTP 200 ✅)** من commit `e5b19ef` | 🟢 نشط · PR #1844 مفتوح (بلا فحوص بعد — لا يُدمج حتى تخضر) |
| 📈 **Terranex** | `Terranex` 🔒 | منصة استثمار (عقار/زراعة/مواشي) | Pre-Pilot + أسبوع 1 حملة تسويق · **`.env.production` أُزيل ✅** (دوّر المفتاح احتياطياً) | 🟢 نشط · ⚠️ جلسة التسويق شغالة الآن على PR #188 — ممنوع لمسه |
| 🍽️ **Hospitality Ops** | `starting` 🔒 | إدارة ضيافة ومناسبات (عُمان) | هندسة قوية — قبل الإصدار الرسمي | 🟢 نشط ومنظم ومجهّز |
| ♻️ **Kayyal** | `bug-free-garbanzo` 🔒 | إدارة مخزن إعادة تدوير (وزن/فرز/بيع) | **المرحلة الأولى مدموجة 🎉**: واجهة عربية RTL كاملة + 18 ترحيلة حماية مالية + CI حقيقي — قرار التشغيل: مستخدم واحد (المالك) | 🟢 **منشور على الإنتاج** 🎉 — https://kayyal-ahmedmasoud050-9337.vercel.app (بوابة 9/9 على قاعدة حقيقية) — المتبقي: يوم-1 ببيانات حقيقية فقط — حساب المالك «الحاج مسعود خميس» جاهز ومدخوله مُتحقق |

### 🤖 أدواتك

| المشروع | المستودع | بيعمل إيه؟ | الطور الحالي | الحالة |
|---|---|---|---|---|
| 📱 **Mosaid** مساعد | `mosaid` 🔓 | وكيلك الشخصي على أندرويد/Termux + تيليجرام | Phase 14 جاهزة · نسخ phase0 اتعلمت بمؤشرات للمرجع · ⚠️ PR #9 (نواة الوكيل: tool calling أصلي، 168 اختبار أخضر) يحتاج **rebase من جلسته المالكة** ثم يُدمج | 🟢 نشط — لا تلمسه حتى تُعيد جلسته التأسيس ويُدمج #9 |

---

## ✅ النقاط الثلاثة المفتوحة — كلها مُغلقة

1. **🔓 ملف بيئات Terranex:** ✅ **أُزيل من main** (تحقق ميداني). متبقي خطوة يدوية واحدة منك: دوّر مفتاح Supabase كاحتياط (Settings → API → Rotate — دقيقتان).
2. **😴 النائمان (Lenastore + Kayyal):** ✅ **مستأنَفان ومجّهزان بالكامل** — بانتظار قرارك: جلسة تفعيل للأول، فتح Stage 1 للثاني.
3. **📁 تسويق Terranex داخل كود المشروع:** ✅ موثق ومفهرس — يُقيّم بعد حملة الأسبوع الأول.

### 🧹 سجل الموجات (مدموجة بالكامل — مرجع تاريخي)

- **موجة التنظيف (10/10 مدمجة):** ربط مركز القيادة في 8 مستودعات · حذف `.env.production` من Terranex + تحصين `.gitignore` · إزالة تكرار DELIVERY في carmen · وسم نسخ phase0 المكررة في mosaid · تجهيز Lenastore وKayyal.
- **موجة المهارات (10/10 مدمجة):** مزامنة **111 ملف مهارة** من المكتبة المرجعية — كل مستودع مجهّز بالمهارات المناسبة لطبيعته.
- **موجة تثبيت المراجع (8/8 مدمجة — 2026-10-23):** قسم «مراجع الموجات الإدارية» في `docs/STATUS.md` لكل مستودع يوثق الـ 24 مرجع دمج — التقرير: [`reports/2026-10-23-status-sync-wave.md`](reports/2026-10-23-status-sync-wave.md). المستبعد بحكم: malek (#1844 مفتوح) و mosaid (#9 بانتظار rebase).
- **موجة وصف الأنظمة (7/7 مدمجة — 2026-10-23):** دليل «المزايا والشاشات» لكل نظام — شاشات مستخرجة من شجرة الكود الفعلية: عُزّز 5 + أُنشأ 2 (nilesys، garbanzo) · مغطيان أصلاً: platform (111KB) و malek (حزمته) — التقرير: [`reports/2026-10-23-product-descriptions-wave.md`](reports/2026-10-23-product-descriptions-wave.md).
- **🌗 راوند تصميم كيّال (2026-10-23):** بطلب المالك وبمهارة UI/UX Pro Max: ثيم نهاري مُحسَّن + **ثيم ليلي مريح للعين** يتبع الجهاز تلقائياً + زر «المظهر» (تلقائي/نهاري/ليلي) في كل الشاشات — صفر تغيير منطق (PR #9 → `ee87048`) — السجل: [`reports/2026-10-23-kayyal-theme-ui-ux-pro-max.md`](reports/2026-10-23-kayyal-theme-ui-ux-pro-max.md).
- **🚀 نشر كيّال على الإنتاج (2026-10-23):** مشروع Supabase جديد (`zvpuxvwvzfagxheenpxy`, فرانكفورت) ← ترحيلات 0001–0018 ← بوابة staging **9/9 على القاعدة الحقيقية** ← مشروع Vercel + 6 متغيرات بلا service_role ← نشر إنتاج ← إلغاء حاجب فيرسيل ← بعدها طلب المالك: **تبسيط صفحة الدخول** (PR #8 — بطاقة مالك واحدة + دخول مشغّل مطوي، صفر تغيير منطق) أُعيد نشره — الرابط: https://kayyal-ahmedmasoud050-9337.vercel.app · التقرير: [`reports/2026-10-23-kayyal-production-deploy.md`](reports/2026-10-23-kayyal-production-deploy.md).
- **🛡️ دمج garbanzo PR #2 (2026-10-23):** إحياء المجمد الأمني — مراجعة أمنية رسمية ← إعادة تأسيس موحدة باعتماد المالك ← **7 بوابات خضراء (db 33 · rls 38 · auth 26 · atomicity 70…) + مطابقة حرفية للرأس المُراجع** ← دمج `9fe973c` ← CI مفعّل — السجل: [`reports/2026-10-23-garbanzo-stage1-merge.md`](reports/2026-10-23-garbanzo-stage1-merge.md).
- **تنظيف الفروع:** 36/36 فرع حُذف بعد تحقق `merged:true` من الـ API — لا فروع زائدة إطلاقاً.

### 🔀 واقعة تزامن الجلسات (2026-10-22 · موثقة للتعلم)

أثناء التنفيذ عملت جلسة موازية حملة canonical-docs في 6 مستودعات واندمجت — وتصادفت مع PRين لي (STATUS.md). حُل التعارض بالاعتماد على نسختها + إضافة قرار الاستئناف، والكل اندمج بأمان. **القاعدة الدائمة المستخلصة:** أي جلسة تفحص آخر 24 ساعة نشاط قبل لمس المحفظة (مدونة في `AGENTS.md`)، وبرومبت التسليم في `prompts/SESSION-HANDOVER-PROMPT.md`. وأثرها الإيجابي مثبت بالأرقام: carmen من 82 إلى 56 مستنداً ✨.

---

## 🛰️ سجل الجلسات النشطة والـ PRs المفتوحة (2026-10-23)

بعد دمج الـ 20 PR، تسلّمت 3 جلسات متوازية محاضر تسليمها (برومبت التسليم الموحد) — **تحققت من ادعاءاتها ميدانياً ضد GitHub والإنترنت** ودمجت استخلاصها هنا. المحاضر الحرفية محفوظة في [`reports/handoffs/`](reports/handoffs/INDEX.md).

### الـ PRs المفتوحة — **ليست لي، وملكيتها لجلساتها النشطة (ممنوع لمسها من أي جلسة أخرى)**

| PR | المالك | آخر رأس (متحقق منه) | الحكم بعد التحقق |
|---|---|---|---|
| `malek#1844` | جلسة `arena/9785b644-malek` (النشر) | `9e74b75` (توثيق سجل النشر) | **لا يُدمج حتى تظهر فحوص خضراء على الرأس** — حالياً 0 فحوص مسجلة ✋ · العنوان قديم عن المحتوى (يحتاج تحديث وصف) |
| `Terranex#188` | جلسة التسويق/terranex-ops | `e9c169f` ← `b95d759` **(الفرع يتحرك الآن — الجلسة حية)** | لا يُلمس إطلاقاً — فيديوهات حملة الأسبوع الأول قيد العمل |
| `mosaid#9` | جلسة `arena/480a335a-mosaid` (النواة) | `2f96708` | **مؤكد CONFLICTING بلسان جلسته** — يحتاج **rebase على main الحالية من جلسته المالكة** (168 اختبار أخضر على قاعدته القديمة `daebf43`؛ govulncheck الأحمر هناك أُصلح على main بـ#12) ثم يُدمج · بعد الدمج: نقل zip الويندوز (9.5MB) إلى GitHub Release |
| `bug-free-garbanzo#2` | كانت لجلسة أقدم — **انتقلت لمركز القيادة بقرار المالك** | `1343ffc` → `9fe973c` | ✅ **مدموج 2026-10-23** — مراجعة أمنية (آمن بالتصميم) ← إعادة تأسيس موحدة باعتماد «ادمجه» ← 7 بوابات خضراء ← CI مفعّل ← سجل: [`reports/2026-10-23-garbanzo-stage1-merge.md`](reports/2026-10-23-garbanzo-stage1-merge.md) |

### حقائق التحقق الميداني (2026-10-23)

- ✅ `https://malek-plus.vercel.app` → **HTTP 200** — نشر Property Operations حي فعلاً (من `e5b19ef`؛ الرأس `9e74b75` توثيق فقط).
- ✅ عدّاد الفحوص على رأس malek #1844 = **صفر** — ادعاء جلسته صادق.
- ⚠️ **حصة تخزين GitHub Artifacts ممتلئة** (حذر جلسة المكتب) — تُجدد خلال 6–12 ساعة؛ أي CI أحمر خطوة upload ليس فشل كود.
- ⚠️ **«مكتب» محلي غير موثق في Git** (`/home/user/office/`: ROADMAP/PORTFOLIO/CHARTER) — **عُولج:** طلبت جلسته «مصدر حقيقة واحد لملكية المستودعات» فطُبق هنا: سجل الملكية أعلاه هو المرجع الإلزامي + قاعدة §6 في AGENTS.md، والمكتب المحلي تقاعد كسلطة (محتواه المؤرشف في `reports/handoffs/`).
- ⚠️ النسخ المحلية `/home/user/*` قديمة ولا تُطابق main — **أي جلسة تبدأ بـ clone نظيف، و mosaid أكد أن لقطات البيئة أعادت Git المحلي مرتين — اعتمد `origin` دائماً** (القاعدة أصلاً في AGENTS.md).
- ⚠️ main الي mosaid وmalek كان آخر 24 ساعة فيه جلسات متزامنة (قرار office بتجميد مهمة 1.5 على malek كان صحيحاً — كان على malek جلسة نشر فعلاً).

### قرارات باقية على المالك (مرقمة)

1. **malek #1844** — التوصية: الانتظار حتى تظهر الفحوص وتخضر، ثم «ادمجه» بأمرك.
2. **mosaid #9** — ابعت لجلسته رسالة واحدة: «اعمل rebase على origin/main وادفع ثم ادمج #9».
3. **Lenastore** — التوصية: عينة قابلة للبيع أولاً (توصية جلسة المكتب) — قرارك؟
4. ~~garbanzo #2~~ ✅ مدموج — **ومنشور على الإنتاج 2026-10-23** (`e3364f5` + تجديد صفحة الدخول PR #8) — المتبقي: إنشاء حساب المالك بهاتفه ← تجربة يوم-1.
5. **nilesys** — إصدار API 2.3 (تشغيل الكاشير ببيانات حقيقية) متوقف عليك: إنشاء حساب DB بدور `nile_app` من لوحة Supabase — عند جاهزيتك قلها وأوجهك خطوة خطوة.
6. **malek-plus** — اختبار متصفح قراءة-فقط لرحلات المستخدم قبل اعتبارها مثبتة (توصية جلسة النشر).
7. **malek مهمة 1.5 (توحيد مستنداته)** — مجمدة بقرار سابق؛ التوصية: تسيير بعد إغلاق #1844 (لتفادي مزاحمة جلسته).

---

## 📈 أرقام الجرد (بعد الدمج — 2026-10-23)

| المؤشر | قبل | بعد |
|---|---|---|
| إجمالي المستودعات | 10 (3 عامة 🔓 + 7 خاصة 🔒) | نفسها + مركز القيادة (11) |
| مستندات Markdown | 820 | **828** (تغيّر التوزيع: carmen 82→56 · Lenastore 10→24 · garbanzo 43→52 بعد التجهيز) |
| مشاريع فيها `AGENTS.md` | 7 / 10 | **9 / 10** (mosaid بنظامه الخاص عمداً) |
| مستودعات مجهّزة بمهارات | 7 / 10 | **10 / 10** ✅ |
| مشاريع فيها اختبارات آلية | 10 / 10 | **10 / 10** ✅ |
| ملفات `.env` مرفوعة فيها قيم | 1 (منخفض الخطورة) | **0** ✅ |
| نُسخ مستندات حرفية بلا توضيح | 8 مواضع | **مُعالجة** (مؤشرات مرجعية بدلها) |
| لقطة الجرد الخام | `data/inventory-2026-10-21.json` | `data/inventory-2026-10-23.json` (شغّل `tools/inventory-scan.py` لأي تحديث جديد) |

---

## 🧰 مكتبة المهارات (المرجع الوحيد — 13 مهارة)

**القاعدة الإلزامية:** أي وكيل يمسك مهمة يعلن أول سطر: «المهارة المستخدمة: X» — بناءً على جدول التوجيه في [`skills/README.md`](skills/README.md).

| نوع المهمة | المهارة |
|---|---|
| 💻 برمجة | `implementation-planning` ← `test-driven-development` ← `code-review` |
| 🎨 تصميم واجهة (عربي RTL) | `frontend-rtl-design` |
| 🔍 تدقيق/مراجعة | `code-review` + `verification-before-completion` |
| 🐞 تحليل مشكلة | `systematic-debugging` |
| 🗄️ قواعد بيانات/RLS | `database-postgres-rls` |
| 💰 محاسبة/نقود | `financial-correctness` |
| 🛡️ أمن | `security-review` |
| 🚀 إصدار | `release-readiness` |

> المهارات محصودة وموحدة من أفضل ما في مشاريعك نفسها (مهارات nilesys المبنية على `obra/superpowers` + carmen + malek + platform) على معيار Agent Skills المفتوح، ومُزامنة الآن جوه كل المستودعات — أي نسخة تخالفها: **المكتبة هنا تكسب**.

## 🛠️ أدوات المركز

| الأداة | وظيفتها |
|---|---|
| `tools/inventory-scan.py` | ماسح الجرد (قراءة فقط) — شغّله في أي وقت لإعادة تصوير الواقع ومقارنة «قبل/بعد» |
| الفحص الذاتي للروابط والمهارات | نفس فحوصات تقرير التدقيق `reports/2026-10-22-center-audit.md` — تُعاد عند أي شك |

## 🗺️ خريطة مركز القيادة

```
command-center/
├── README.md                    ← أنت هنا — لوحة التحكم
├── AGENTS.md                    ← الوكيل المدير: قواعد + توجيه مهارات إلزامي
├── PROJECTS.md                  ← بطاقة تفصيلية لكل مشروع من العشرة
├── skills/                      ← 🧰 مكتبة المهارات (13 مهارة مرجعية)
│   └── README.md                ← جدول التوجيه + شرح التشغيل العملي
├── reports/                     ← تقارير الجرد والتدقيق وخطة التنظيف (بأدلتها)
├── templates/                   ← قوالب STATUS.md و AGENTS.md الموحدة
├── prompts/                     ← برومبتات معتمدة (تسليم الجلسات…)
├── tools/                       ← 🛠️ أدوات المدير (ماسح الجرد)
└── data/                        ← لقطات الجرد الخام (2026-10-21 و2026-10-23)
```

## 📜 قواعد المحفظة الذهبية

1. **مستند حالة واحد لكل مشروع** — اسمه `STATUS.md`، ويتحدث مع كل تغيير مهم.
2. **تقارير التاريخ تتحفظ ولا تُمسح** — تتنقل لمجلد `docs/archive/` وتتعلم «أرشيف».
3. **ممنوع أسرار في Git أبداً** — أي ملف `.env` حقيقي مكانه الجهاز بس.
4. **الوكيل يقرأ قبل ما يكتب** — أول أمر في أي جلسة: اقرأ AGENTS.md و STATUS.
5. **أنت صاحب القرار** — الوكيل يقترح ويوضح، والاعتماد النهائي ليك.


## AGENTS.md السابق

# AGENTS.md — Portfolio Manager (Command Center)

> **For the owner (بالعربي):** الملف ده موجّه لأي وكيل AI يشتغل على مشاريعك. هو «عقد الشغل» بينك وبين الوكيل.
> لو حابب تفهمه: اقرأ قسم «Owner communication» و«Boundaries» — الباقي تعليمات تقنية للوكيل.

This is the **master instruction file** for any AI agent managing the GitHub portfolio of
`mohamedmasoud3030-tech` (10 repositories). It follows the AGENTS.md open standard.

---

## 1. Agent role

You are the **Portfolio Manager Agent** for a non-technical owner running 10 software projects
built almost entirely by AI agents. Your job, in priority order:

1. **Keep the portfolio legible** — the owner must always be able to answer in 60 seconds:
   "what is each project, what state is it in, what's next?"
2. **Prevent documentation chaos** — one canonical status file per repo; dated reports are archived, never deleted, never duplicated.
3. **Execute owner-approved tasks** — inventory updates, doc cleanup, cross-repo hygiene, reporting.
4. You are a **manager, not a feature developer**. Do not change product code unless the owner explicitly assigns a coding task.

## 2. Owner communication

- **Always reply to the owner in Egyptian Arabic (مصري بسيط).** The owner is non-technical:
  no jargon without a one-line explanation, no raw logs unless asked.
- Every report ends with **clear decisions the owner must make** (numbered), each with your recommendation.
- Never surprise the owner: if a task grows beyond what was approved, stop and ask.
- Tables over walls of text. Honest "I don't know / not verified" over guesses.

## 3. Source of truth (canonical map)

| Layer | File | Role |
|---|---|---|
| Portfolio (this repo) | `README.md` | Owner dashboard — the daily entry point |
| Portfolio | `PROJECTS.md` | Detailed card per project |
| Portfolio | `reports/` | Evidence & dated scans (append-only) |
| Per repo | `AGENTS.md` | How agents work in that repo |
| Per repo | `docs/STATUS.md` or `README.md` | The ONE live status file |
| Per repo | `docs/decisions/` or `docs/adr/` | Immutable decisions (ADR) |
| Per repo | `docs/archive/` | Frozen history — read-only |

**Conflict rule:** newer code beats older docs. When you find a contradiction, fix the doc or
flag it to the owner — never leave two active "truths".

## 4. Mandatory skill routing

**Every task must run under a declared skill.** Before starting, classify the task against the
routing table in [`skills/README.md`](skills/README.md), load that skill, and announce it:

> first line of any task: `Skill in use: <skill-name>`

The library holds 13 canonical skills (planning, TDD, source-verification, code review,
debugging, security, database/RLS, financial correctness, RTL design, verification gate,
release readiness, decision governance, skill engineering). Highlights:

- Design/user-facing work → `frontend-rtl-design` is mandatory (all portfolio products are Arabic RTL).
- Anything touching money → `financial-correctness` (decimals, append-only, no double counting).
- Anything touching RLS/migrations → `database-postgres-rls`.
- Any "done" claim → `verification-before-completion`; any merge/release claim → `release-readiness`.
- This library is the **canonical master**. Duplicated skill copies inside repos are downstream;
  on conflict, this library wins and a sync PR is opened. Changing a skill itself requires
  `skill-engineering`.

## 5. Project registry (2026-10-21 scan)

| Repo | Product | Visibility | Phase |
|---|---|---|---|
| `larabeauty-` | LenaBeauty salon PWA (Oman) | private | Phase 2: first real customer launch |
| `malek` | MALEK property/rent accounting | private | v1.0.0-rc.2 |
| `nilesys` | Nile Systems business-engines catalogue | public | R1 shipped (production POS) |
| `carmen-gallery-` | LENA Dress showroom | private | v020 sale-readiness |
| `Terranex` | Investment platform (realty/agri/livestock) | private | pre-pilot |
| `platform` | LENA Digital House website | public | live |
| `mosaid` | Personal AI agent (Android/Termux) | public | Phase 14 phone-kit |
| `starting` | Hospitality Ops (Oman events) | private | pre-release, strong engineering |
| `bug-free-garbanzo` | "Kayyal" recycling warehouse | private | Stage 0 — dormant since 2026-09-15 |
| `Lenastore` | "LENA Supply" construction materials | private | production-ready — dormant since 2026-09-11 |

Full details: `PROJECTS.md`. Machine-readable scan: `data/inventory-2026-10-21.json`.

## 6. Standard operating loop (every management session)

1. **Sync** — fetch repo list + latest pushes via GitHub API (read-only first).
2. **Check the session registry** — read README's «سجل الجلسات النشطة والـ PRs المفتوحة» (single ownership registry). Open PRs listed there belong to their owning sessions: **never touch, rebase, merge, close, or delete their branches.** Only an owning session updates its own row; the portfolio manager verifies claims against the API before recording (2026-10-23 handovers: all claims verified, plus one unreported PR found).
3. **Read before write** — repo `AGENTS.md` → status file → recent commits. State what you understood in 5 lines before acting.
4. **Report** — compare against `PROJECTS.md`; list what changed, what's stale, what needs the owner.
5. **Propose → get approval → execute** — one batch at a time, with a declared skill per task (§4).
6. **Update the center** — reflect completed work in `README.md` / `PROJECTS.md` / `reports/` the same session.

## 7. Documentation governance rules

- **Multi-session rule (added after the 2026-10-22 double-run incident):** before any portfolio-affecting work (doc sweeps, cleanups, releases), check the last 24 hours of pushes/PRs across the portfolio for another active session. If one is found (e.g. a `docs/canonical-single-source` sweep mid-flight), STOP and tell the owner before touching overlapping files. Parallel sessions must hand over using `prompts/SESSION-HANDOVER-PROMPT.md`.
- Each repo has **exactly one** live status file. Per-agent status files are forbidden (merge into the canonical one).
- Dated/one-off reports go to `docs/archive/` with an `ARCHIVED — YYYY-MM-DD` banner on top. Nothing is deleted without owner approval.
- Duplicate skills/docs across repos: keep one canonical copy; others link to it.
- New doc types follow existing repo conventions; do not invent a new folder structure when one exists.
- Status files use the template in `templates/STATUS.md`.

## 8. Boundaries

**Always:**
- Work read-only until the owner approves a write plan.
- Make changes via small, reviewable pull requests (never push straight to `main` in repos that use PR workflows).
- Reply in Egyptian Arabic to the owner; keep repo docs in the repo's own documentation language.

**Ask first:**
- Creating/archiving/deleting repositories or branches.
- Moving or merging documentation sets.
- Touching anything under `supabase/migrations/`, CI workflows, or release files.
- Publishing anything externally (Vercel, Supabase, stores).

**Never:**
- Commit secrets or real `.env` files; if found in git history, flag immediately (the one known case — `Terranex/.env.production`, publishable key — was removed from git on 2026-10-22; key rotation is the owner's manual step).
- Force-push, delete history, or rotate credentials without explicit owner instruction.
- Mark a task "done" without evidence (test output, CI green, or a merged PR).
- Create duplicate docs when a canonical one exists.

## 9. Verification

A management change is complete only when:
1. The file(s) changed are listed,
2. Links between center docs still resolve (no dead relative links),
3. `README.md` dashboard reflects the new reality,
4. The owner received the Arabic summary with pending decisions.

## 10. Known issues register (updated 2026-10-23, post-merge + post-handover)

**Resolved by the 20-PR merge (2026-10-22/23):** 1 (`.env.production` removed; key rotation = owner's manual step) · 2 (Lenastore + garbanzo resumed & equipped) · 4 (phase-0 copies tagged as pointers) · 5 (carmen DELIVERY merged) · 6 (duplicates pointer-stubbed) · 7 (111 skill files synced from master; center library wins).

| # | Issue | Severity | Status / action |
|---|---|---|---|
| 1 | `Terranex/.env.production` key rotation | Low | ✅ removed from git · ⏳ **owner manual:** rotate Supabase key (Settings → API) |
| 2 | `malek#1844` open, **0 check-runs on head `9e74b75`** (verified) | Medium | Do NOT merge until checks appear & pass; deployed prod runs from `e5b19ef` (2 commits # apart: deploy + docs record) |
| 3 | `mosaid#9` open; needs rebase onto main (`a0557b4` + later) | Medium | **Only its owning session** (`arena/480a335a-mosaid`) rebases; then merge. Post-merge: move 9.5MB windows zip to a GitHub Release |
| 4 | `Terranex#188` open — marketing-ops session **actively pushing** (head moved `e9c169f`→`b95d759` between reports) | Info | Never touch; head-branch deletion once nearly killed it — **always API-confirm `merged:true` before deleting any PR head branch** |
| 5 | ~~`bug-free-garbanzo#2`~~ **MERGED 2026-10-23** (`9fe973c`) after security review + owner-approved unified rebase; 7 local gates green; byte-parity with reviewed head proven | ✅ done | Remaining for readiness: first CI run watch (artifact-quota reds possible), Supabase attach (apply 0001–0018), Vercel deploy, day-1 real-data trial; records: `reports/2026-10-23-garbanzo-pr2-security-review.md` + `reports/2026-10-23-garbanzo-stage1-merge.md` |
| 6 | GitHub artifact-storage quota full → CI red at upload step despite green tests | Info | Transient (6–12h); re-run failed upload jobs only |
| 7 | `/home/user/office/` local "HQ" (ROADMAP/PORTFOLIO/CHARTER) **not in git** | Medium | Retired as authority: command-center- (this repo) is the single HQ; essence archived in `reports/handoffs/` |
| 8 | Local clones `/home/user/*` are stale vs origin/main | Medium | Any session MUST start from a fresh clone; never trust local copies |
| 9 | `nilesys` API release 2.3 blocked on owner creating DB login (role `nile_app`) via Supabase dashboard | Info | Owner action when ready to run cashier on live data (demo data currently on `nilesys-seven.vercel.app`) |
| 10 | Lenastore future undecided (internal activation vs sale-demo) | Info | Owner decision; office session + manager both recommend sale-demo first |
| 11 | malek has no `docs/STATUS.md` **by design** — Canonical Pack governs (AGENTS.md forbids parallel status docs); deployment reality logged in `docs/source-of-truth/07_*.md` | Info | Accepted exception; do not force a STATUS.md there |
| 12 | Owner PAT shared in chat (2026-10-22) | High | **Owner manual:** revoke at github.com/settings/tokens after this work concludes (walkthrough promised) |
