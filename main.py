from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import aiohttp
import uuid
import os
import asyncio
import ffmpeg
import torch

app = FastAPI()

# ======== Mock STT Model (replace with your actual model) ===========
class STTModel:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Model loaded on {self.device}")
        # self.model = load_your_model().to(self.device)

    def transcribe(self, wav_path):
        # Dummy output for demo — plug in actual model
        return f"Transcribed text from {os.path.basename(wav_path)}"

model = STTModel()

# ======== Input Schema ===========
class AudioRequest(BaseModel):
    audio_url: str

# ======== Helper Functions ==========

async def download_audio(url, download_dir="downloads"):
    os.makedirs(download_dir, exist_ok=True)
    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(download_dir, filename)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise HTTPException(status_code=400, detail="Failed to download audio.")
            with open(filepath, 'wb') as f:
                f.write(await response.read())
    return filepath

def convert_to_wav(input_path):
    output_path = input_path.replace(".mp3", ".wav")
    (
        ffmpeg
        .input(input_path)
        .output(output_path, ac=1, ar='16k')  # mono, 16kHz
        .overwrite_output()
        .run(quiet=True)
    )
    return output_path

# ======== API Endpoint ============
@app.post("/transcribe")
async def transcribe_audio(request: AudioRequest):
    try:
        # Step 1: Download
        mp3_path = await download_audio(request.audio_url)

        # Step 2: Convert
        wav_path = convert_to_wav(mp3_path)

        # Step 3: Transcribe
        transcription = model.transcribe(wav_path)

        # Step 4: Cleanup (optional)
        os.remove(mp3_path)
        os.remove(wav_path)

        return {"text": transcription}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
