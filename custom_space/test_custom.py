from gradio_client import Client
import shutil

SPACE_URL = "Yousefsg/qwen-tts-custom"
print("🔄 جاري الاتصال بالسيرفر (القناة مفتوحة ولن تنقطع)...")
client = Client(SPACE_URL)

text_to_say = "In the heart of the digital revolution, a new intelligence is rising. It doesn't sleep, it doesn't tire, and it's rewriting the rules of our world. From the way we diagnose diseases, to how we explore the furthest reaches of space, artificial intelligence is no longer a dream of the future. It is our current reality."

# قائمة الأصوات المتاحة ووصفها (اختر واحداً وضعه في متغير speaker بالأسفل):
# 1. 'ryan'     -> رخيم، عميق، مناسب جداً للوثائقيات والتعليق الرسمي. (الأفضل لمشروعك)
# 2. 'vivian'   -> نسائي، ناعم، وواضح جداً.
# 3. 'aiden'    -> رجالي، شبابي وحيوي.
# 4. 'dylan'    -> رجالي، نبرة متوسطة. 
# 5. 'eric'     -> رجالي، صوت مباشر وقوي.(استخدمه)
# 6. 'serena'   -> نسائي، نبرة دافئة.
# 7. 'uncle_fu' -> رجالي، صوت كبير في السن ووقور (مناسب للاعلانات).
# 8. 'sohee'    -> صوت كوري نسائي بلكنة إنجليزية.
# 9. 'ono_anna' -> صوت ياباتي بلكنة إنجليزية.

speaker = "eric"
instruct = ""

print("⏳ تم إرسال الطلب... جاري المعالجة في الخلفية. يمكنك ترك الجهاز يعمل!")

# يتصل عبر API Gradio الخفي والمستقر
result_path = client.predict(
    text_to_say,
    speaker,
    instruct,
    "english",
    fn_index=0
)

output_name = "custom_automated_output.wav"
shutil.move(result_path, output_name)
print(f"✅ تمت العملية بنجاح! الصوت محفوظ باسم {output_name}")
