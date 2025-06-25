# 🧠 Chatbot Voice Assistant (Jarvish)

An AI-powered voice assistant that can:
- Answer questions using OpenAI GPT
- Speak responses using `pyttsx3`
- Understand voice commands
- Schedule appointments

## 🛠️ Tech Stack
- Python 3.12
- OpenAI API
- PyAudio + SpeechRecognition
- pyttsx3 (Text-to-speech)
- dotenv

## 🚀 How to Run

```bash
# Clone this repo
git clone https://github.com/SenseiKunal/Chatbot-Voice-Assistant.git
cd Chatbot-Voice-Assistant

# Create virtual environment
uv venv
.venv\Scripts\Activate.ps1

# Install dependencies
uv pip install -r requirements.txt

# Add your API Key
# Create `.env` file with:
OPENAI_API_KEY=sk-xxxxxx

# Run the assistant
python src/chatbot.py
