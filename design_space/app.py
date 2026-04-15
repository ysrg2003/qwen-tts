import gradio as gr
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel
import uuid

MODEL_ID = "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32

print(f"Loading {MODEL_ID}...")
model = Qwen3TTSModel.from_pretrained(MODEL_ID, device_map=device, dtype=dtype)

def generate_design(text, instruct, language="english"):
    output_filename = f"design_output.wav"
    try:
        wavs, sr = model.generate_voice_design(
            text=text, 
            instruct=instruct, 
            language=language
        )
        sf.write(output_filename, wavs[0], sr)
        return output_filename
    except Exception as e:
        raise gr.Error(f"Error: {e}")

iface = gr.Interface(
    fn=generate_design,
    inputs=["text", "text", "text"], # text, instruct, language
    outputs=gr.Audio(type="filepath")
)
iface.launch(server_name="0.0.0.0", server_port=7860)