from gradio_client import Client, handle_file
import shutil

# اسم المساحة بالشكل الصحيح: OwnerName/SpaceName
SPACE_URL = "Yousefsg/qwen-tts-gradio-test"

print("🔄 جاري الاتصال بالسيرفر (القناة مفتوحة ولن تنقطع)...")
client = Client(SPACE_URL)

text_to_say = "In the heart of the digital revolution, a new intelligence is rising. It doesn't sleep, it doesn't tire, and it's rewriting the rules of our world. From the way we diagnose diseases, to how we explore the furthest reaches of space, artificial intelligence is no longer a dream of the future. It is our current reality."

ref_text = "In the heart of thالe digital revolution, a new intelligence is rising. It doesn't sleep, it doesn't tire, and it's rewriting the rules of our world. From the way we diagnose diseases, to how we explore the furthest reaches of space, artificial intelligence is no longer a dream of the future. It is our current reality."

# لتجنب أخطاء عدم وجود الملف، أضفنا المسار الكامل الذي تملكه
ref_audio = r"E:\qwen tts\documentary_reference.wav" 

print("⏳ تم إرسال الطلب الضخم... جاري المعالجة في الخلفية. يمكنك ترك الجهاز يعمل!")

# يتصل عبر API Gradio الخفي والمستقر
result_path = client.predict(
    text_to_say,
    ref_text,
    handle_file(ref_audio), # يقوم برفع الملف الآلية
    "english",
    fn_index=0
)

# يقوم بنقل الملف الذي أرسله السيرفر إلى مجلدك الحالي
shutil.move(result_path, "automated_output.wav")
print("✅ تمت العملية بنجاح! الصوت محفوظ باسم automated_output.wav")