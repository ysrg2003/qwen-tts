import gradio as gr
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel
import uuid

MODEL_ID = "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32

print(f"Loading {MODEL_ID}...")
model = Qwen3TTSModel.from_pretrained(MODEL_ID, device_map=device, dtype=dtype)

def generate_custom(text, speaker, instruct, language="english"):
    output_filename = f"custom_output.wav"
    try:
        wavs, sr = model.generate_custom_voice(
            text=text, 
            speaker=speaker, 
            instruct=instruct if instruct else None, 
            language=language
        )
        sf.write(output_filename, wavs[0], sr)
        return output_filename
    except Exception as e:
        raise gr.Error(f"Error: {e}")

iface = gr.Interface(
    fn=generate_custom,
    inputs=["text", "text", "text", "text"], # text, speaker, instruct, language
    outputs=gr.Audio(type="filepath")
)
iface.launch(server_name="0.0.0.0", server_port=7860)