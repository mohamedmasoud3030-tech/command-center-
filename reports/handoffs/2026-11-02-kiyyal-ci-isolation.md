# تسليم مراجعة كيّال — 2026-11-02

**الهدف:** إصلاح العزل في CI ومراجعة PR #26 من غير لمس `main` أو نشر الإنتاج.

## المرجع الفعلي

- المستودع الرسمي: `mohamedmasoud3030-tech/kiyyal`، والاسم `bug-free-garbanzo` تاريخي.
- طلب الدمج: [kiyyal #26](https://github.com/mohamedmasoud3030-tech/kiyyal/pull/26)، Draft / OPEN، القاعدة `main@1b3186defe699d5eedb1432add70781452b66ed7`.
- رأس الفحص قبل التعديل: `4337f01ba089c396ed6b60337d480e37df4ab2c0`.
- [Push run 41362736118](https://github.com/mohamedmasoud3030-tech/kiyyal/actions/runs/41362736118) و[PR run 41362740338](https://github.com/mohamedmasoud3030-tech/kiyyal/actions/runs/41362740338): `verify` نجح، `browser-e2e` فشل، `staging-gate` تخطاه التنفيذ.

## جذر المشكلة المستنتج من السجلات والكود

- `tests/db/pg-harness.ts` يستخدم منفذ `55433` ومجلد `/tmp/kayyal-pg-55433` ثابتين على مستوى العملية.
- `playwright.config.ts` كان يسمح بعاملين افتراضيًا في CI؛ `fullyParallel: false` لا يمنع توازي ملفات `*.spec.ts`.
- ظهر في تشغيل Push خطأ حذف ملفات `initdb` أثناء الإنشاء، وفي تشغيل PR ظهر `directory exists but is not empty`. الاختبار الفاشل كان `operator-journey`، بينما نجح عشرون اختبارًا في تشغيل PR.
- أكثر من ملف E2E ينفذ `next build` على `.next` مشتركة؛ عزل العمال يمنع التصادم في البناء أيضًا. لا يوجد دليل على فشل وظيفي للمنتج في هذين السجلين، ولا إثبات على عدم وجود عيوب أخرى.

## إجراءات فرع kiyyal

- اختبار انحدار في `tests/ci/playwright-isolation.test.ts` يفرض تعطيل توازي الملفات وتثبيت عامل واحد وعدم استعمال retries.
- `playwright.config.ts`: تعيين `workers: 1` مع توثيق سبب القيد.
- `AGENTS.md`: تصحيح اسم المستودع والنسخ الحالية (Node>=22، CI Node 24.22.2، Next 16.4.3).
- `main` والإنتاج وبيانات Supabase لم تُعدل.

## نتائج التحقق والنواقص

- [GitHub CI 41426833894](https://github.com/mohamedmasoud3030-tech/kiyyal/actions/runs/41426833894) على رأس `f2ad9d695827b228cbbe0d227869f75094d6716a`: `verify=success` (Vitest **327/327**)، `browser-e2e=success` (Playwright **21/21** باستخدام عامل واحد)، `staging-gate=skipped`. نجاح CI مثبت على هذا الرأس بالذات، ولا يكفي لموافقة الدمج/الإنتاج. أي رأس أحدث يتطلب فحصه مستقلاً.
- Branch protection / required checks لحماية `main` لم تُفعّل من هذه الجلسة: أدوات GitHub المتاحة هنا لا تقدم تعديل Rulesets. يجب تفعيل مراجعات PR وRequired checks (`verify` و`browser-e2e`) ومنع force push/delete من واجهة GitHub، والتحقق من سياسة ربط الإنتاج في Vercel بصلاحيات المشروع.
- أي مشكلة مستمرة في `next-http` أو بوابة staging يجب أن تُعالج على أساس دليل جديد وليس نسبة نجاح جزئية.
- لا يوجد تفويض merge أو production deploy.

**أول خطوة لاحقة:** افحص أحدث Run لـ PR #26 (SHA مطابق)؛ إذا فشل، اقرأ خطوة الاختبار وسجلها؛ إذا نجح، استمر بمراجعة diff وقيود الحماية قبل تحويل Draft.
