# 🧠 Uzbek-Russian STT Microservice (gRPC)

This is a gRPC-based Speech-to-Text (STT) microservice powered by a fine-tuned Hugging Face model specialized in **Uzbek 🇺🇿** and **Russian 🇷🇺** speech transcription.

## 🚀 Features

- 🎙️ Transcribes Uzbek and Russian audio files
- 🌐 Accepts public **audio URLs**
- 🧑‍🤝‍🧑 Optional **speaker diarization**
- 👩‍🦰 Optional **gender detection**
- ⏱️ Optional **duration calculation**
- 📦 Simple gRPC API for seamless integration

## 🧩 How It Works

1. Client sends a gRPC request with:
   - `audio_url`: Public URL of the audio file (MP3/WAV/etc.)
   - `has_diarization`: `true/false` – if speaker diarization is needed
   - `is_gender`: `true/false` – if gender identification is required
   - `is_duration`: `true/false` – if duration calculation is needed

2. The server:
   - Downloads the audio file
   - Processes it using the Uzbek-Russian STT model
   - (Optionally) applies diarization, gender tagging, and duration analysis
   - Returns the transcription result in the response

## 🛠️ Tech Stack

- **Language**: Python 🐍
- **Framework**: gRPC
- **Model**: PRIVATE STT MODEL on Huggingface
- **Audio Tools**: `pydub`, `torchaudio`, `ffmpeg`

## 📡 gRPC API

### `TranscribeRequest`

```proto
message TranscribeRequest {
  string audio_url = 1;
  bool has_diarization = 2;
  bool is_gender = 3;
  bool is_duration = 4;
}
```

### `TranscribeResponse`

```proto
message TranscribeResponse {
  string transcript = 1;
  optional string diarization_result = 2;
  optional string gender_info = 3;
  optional float audio_duration = 4;
}
```


## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/norbe2101/stt-service.git
cd stt-service
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### python server.py
```bash
python server.py
```

### 4. Send a gRPC request
```
Use any gRPC client or your own script to call the Transcribe service with the desired parameters.
```

```json
{
  "audio_url": "https://your-storage.com/audio/uzbek_speech.wav",
  "has_diarization": true,
  "is_gender": false,
  "is_duration": true
}
```

## 📄 License

```
This project is licensed under the MIT License.
```

## 🤝 Contributing

```
Pull requests and issue reports are welcome. Feel free to fork the repo and suggest improvements!
```
