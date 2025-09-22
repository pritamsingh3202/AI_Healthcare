# 🩺  Healthcare System

This project is a voice- and vision-enabled healthcare assistant.  
It listens to a patient’s symptoms, looks at uploaded images (like a skin rash), and replies with a short, doctor-style opinion—both in text **and** a natural-sounding voice.

The goal isn’t to replace a real doctor, but to give people **quick, accessible first-step insights** before they seek professional care.

---

## ✨ What It Can Do
- **Talk to You** – Speak your symptoms and the system converts your voice to text using **Whisper Large-v3** (via Groq API).
- **See the Problem** – Upload a photo of a visible condition (skin, eye, etc.) and a **Meta-LLaMA multimodal model** analyzes it.
- **Respond Like a Doctor** – Receives the AI’s medical opinion in both written form and lifelike audio using **gTTS** or **ElevenLabs**.
- **Simple Web UI** – Built with **Gradio**, so you can interact directly from your browser.

---

## 🛠️ Tech Stack
| Area | Technology | Why it’s used |
|------|------------|---------------|
| Speech-to-Text | **Whisper Large-v3 (Groq)** | Accurate transcription even with background noise |
| Image Analysis | **Meta-LLaMA-4 Maverick** | Handles multimodal (text + image) medical queries |
| Text-to-Speech | **gTTS** & **ElevenLabs** | gTTS for quick TTS, ElevenLabs for natural voice |
| Web UI | **Gradio** | Fast, clean interface without heavy frontend code |
| Audio Handling | **SpeechRecognition**, **Pydub** | Record, process, and export audio |
| Env Mgmt | **python-dotenv** | Keeps API keys safe and separate |

---

## 🚀 Getting Started
### 1. Clone the repo
```bash
git clone https://github.com/yourusername/healthcare-system.git
cd healthcare-system


##  Set environment variables

Create a .env file in the root directory and add:

GROQ_API_KEY=your_groq_key
ELEVENLABS_API_KEY=your_elevenlabs_key

