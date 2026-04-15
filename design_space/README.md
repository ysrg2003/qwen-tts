---
title: Qwen3 TTS API
emoji: 🎙️
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
---
# 🎨 مساحة تصميم الصوت الدقيق (Voice Design Space)

## 📌 ما هي هذه المساحة؟
مساحة مخصصة حصرياً لتشغيل موديل `Qwen3-TTS-12Hz-1.7B-VoiceDesign`.
**الهدف:** تخليق وابتكار بصمة صوتية جديدة من العدم بناءً على "وصف نصي" لخصائص الصوت ونبرته وحالته العاطفية.

## 💡 متى أستخدمها؟
إذا لم يكن لديك صوت لتقليده (Clone) ولم تعجبك الأصوات الجاهزة (Custom)، يمكنك هنا صناعة المعلق الصوتي الخاص بك (مثل: رجل عجوز حكيم، أو فتاة طائشة، أو معلق وثائقي). بعد توليد الملف الذي يعجبك هنا، تحتفظ به وتستخدمه كمرجع في مساحة الاستنساخ (Clone Space) لتثبيت الصوت للفيديوهات الطويلة.

## 🛠️ المتغيرات في كود الاختبار (`test_design.py`)
1. **`API_URL`**: رابط المساحة التي رفعت عليها هذه الملفات.
2. **`text`**: النص القصير الذي تريد للصوت الجديد قراءته (ينصح بجعله بين 5 لـ 15 ثانية كمرجع).
3. **`instruct`**: الوصف الروائي للصوت (Prompt). 
   - *أمثلة وصفية (بالإنجليزي أفضل للنموذج):*
     - `A middle-aged man with a deep, resonant voice. He is speaking in a serious documentary style.`
     - `A young energetic female streaming a gaming video with high excitement.`
     - `An old wise wizard speaking slowly and softly.`
4. **`language`**: لغة التحدث. الخيارات: `auto`, `english`, `chinese`, `french`, `german`, `italian`, `japanese`, `korean`, `portuguese`, `russian`, `spanish`.