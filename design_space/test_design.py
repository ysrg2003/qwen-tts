from gradio_client import Client
import shutil

SPACE_URL = "Yousefsg/qwen-tts-design"
print("🔄 جاري الاتصال بالسيرفر (القناة مفتوحة ولن تنقطع)...")
client = Client(SPACE_URL)

text_to_say = "In the heart of the digital revolution, a new intelligence is rising. It doesn't sleep, it doesn't tire, and it's rewriting the rules of our world. From the way we diagnose diseases, to how we explore the furthest reaches of space, artificial intelligence is no longer a dream of the future. It is our current reality."
instruct = "A middle-aged man with a deep, resonant voice. He is speaking in a serious, confident, and cinematic documentary style. The tone is clear and captivating."

print("⏳ تم إرسال الطلب... جاري المعالجة في الخلفية. يمكنك ترك الجهاز يعمل!")

# يتصل عبر API Gradio الخفي والمستقر
result_path = client.predict(
    text_to_say,
    instruct,
    "english",
    fn_index=0
)

# يقوم بنقل الملف الذي أرسله السيرفر إلى مجلدك الحالي
output_name = "documentary_reference.wav"
shutil.move(result_path, output_name)
print(f"✅ تمت العملية بنجاح! الصوت محفوظ باسم {output_name}")
