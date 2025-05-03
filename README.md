# NITA: Neural Intelligent Task Assistant 🧠🎙️

NITA is a Python-based voice assistant capable of responding to wake words, recognizing commands, and executing tasks using AI models and speech recognition.

---

## 🚀 Features

- Hotword activation (e.g., "Hey Nita")
- Command recognition using trained ML model
- Text-to-speech feedback
- Extendable module system

---

## 📁 Folder Structure

```
NITA/
├── main.py
├── requirements.txt
├── models/
│   ├── vectorizer.pkl
│   └── command_classifier.pkl
├── modules/
│   ├── ai_command.py
│   ├── hotword_listener.py
│   ├── speech_recognition.py
│   ├── text_to_speech.py
│   └── response_engine.py
├── assets/
│   └── wake_word_model/
│       └── hey-nita_en_windows_v2_2_0.ppn
```

---

## 🔧 Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/nita.git
cd nita
```

### 2. Set Up Virtual Environment (Windows)

```bash
python -m venv .venv
.venv\Scripts\activate
```

> For Mac/Linux: `source .venv/bin/activate`

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Download Required Model Files

### 🔊 Wake Word Model (Porcupine)

1. Go to: [https://console.picovoice.ai/](https://console.picovoice.ai/)
2. Log in and create a **custom wake word**: "Hey Nita"
3. Select:
   - Platform: **Windows**
   - Language: **English**
   - Type: **Porcupine Wake Word**
4. Download the `.ppn` file and place it in:

```bash
assets/wake_word_model/hey-nita_en_windows_v2_2_0.ppn
```

---

### 🧠 ML Model Files

- `vectorizer.pkl`
- `command_classifier.pkl`

Place these in the `models/` directory.
If not provided, train your own using the script in `training/train_intent_classifier.py` (if included).

---

## ▶️ Run the App

```bash
python main.py
```

If everything is set correctly, NITA will listen for "Hey Nita" and respond to your voice commands.

---

## 🛠️ Troubleshooting

- **PorcupineActivationLimitError**: Recreate the wake word from your Picovoice dashboard.
- **No module named 'pyaudio'**: Install it using:
  ```bash
  pip install pipwin
  pipwin install pyaudio
  ```

---

## 📬 Contributions Welcome!

Feel free to fork this repo and submit PRs to improve NITA’s intelligence or expand its skillset.
