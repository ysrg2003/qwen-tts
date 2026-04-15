import gradio as gr
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel
import os

MODEL_ID = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32

print("Loading Base (Clone) Model...")
model = Qwen3TTSModel.from_pretrained(MODEL_ID, device_map=device, dtype=dtype)

def generate_clone(text, ref_text, ref_audio_path, language):
    output_filename = "output_clone.wav"
    try:
        wavs, sr = model.generate_voice_clone(
            text=text, 
            ref_audio=ref_audio_path, 
            ref_text=ref_text, 
            language=language
        )
        sf.write(output_filename, wavs[0], sr)
        return output_filename
    except Exception as e:
        raise gr.Error(f"Error: {e}")

# واجهة Gradio تقوم بإنشاء API خلفي لا ينقطع اتصاله
iface = gr.Interface(
    fn=generate_clone,
    inputs=["text", "text", gr.Audio(type="filepath"), "text"],
    outputs=gr.Audio(type="filepath")
)
iface.launch(server_name="0.0.0.0", server_port=7860)