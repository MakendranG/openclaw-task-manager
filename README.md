# 🦞 OpenClaw Task Manager

An AI-powered personal task assistant built with OpenClaw, Flask, and LLaMA 3.2 — running entirely on AWS Cloud9 with no external APIs.

> Submission for the [OpenClaw Writing Challenge](https://dev.to/challenges/openclaw-2026-04-16) on DEV.to

---

## 🚀 What It Does

- Accept tasks in plain natural language
- Uses **LLaMA 3.2** (via Ollama) to generate a clean AI summary of each task
- Stores tasks locally in JSON with timestamp and status
- List all tasks anytime with a simple command
- Fully self-hosted — your data never leaves your server

---

## 🏗️ Architecture

```
User (CLI)
    ↓
app.py  ←→  openclaw_agent.py (Flask API :3000)
                    ↓
              Ollama + LLaMA 3.2
                    ↓
              tasks.json (storage)
```

---

## 📦 Tech Stack

| Component | Technology |
|---|---|
| AI Model | LLaMA 3.2 (3B) |
| Model Runner | Ollama |
| Backend API | Flask (Python) |
| CLI Interface | Python |
| Storage | JSON |
| Deployment | AWS Cloud9 + EC2 |

---

## ⚙️ Setup & Installation

### Prerequisites
- AWS Cloud9 or any Linux machine
- Python 3.9+
- Ollama installed

### 1. Install Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2
```

### 2. Clone the repo
```bash
git clone https://github.com/MakendranG/openclaw-task-manager.git
cd openclaw-task-manager
```

### 3. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Running the App

**Terminal 1 — Start the AI Agent:**
```bash
source venv/bin/activate
python openclaw_agent.py
```

**Terminal 2 — Start the CLI:**
```bash
source venv/bin/activate
python app.py
```

---

## 💬 Usage

```
OpenClaw Task Manager
Commands: add, list, exit

Enter command: add
Enter task: Remind me to deploy tomorrow at 10 AM

Status code: 200
✅ Task added: {
  "id": 1,
  "text": "Remind me to deploy tomorrow at 10 AM",
  "ai_summary": "Deploy the application tomorrow at 10 AM.",
  "done": false,
  "created_at": "2026-04-26T15:44:45.014827"
}

Enter command: list

📋 Current Tasks:
  1. ⏳ Remind me to deploy tomorrow at 10 AM
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/task` | Add a new task |
| GET | `/tasks` | List all tasks |
| GET | `/health` | Health check |

---

## 📁 Project Structure

```
openclaw-task-manager/
├── app.py               # CLI interface
├── openclaw_agent.py    # Flask API + Ollama integration
├── requirements.txt     # Python dependencies
├── tasks.json           # Local task storage
└── README.md
```

---

## 🙌 Author

**Makendran G**
- GitHub: [@MakendranG](https://github.com/MakendranG)
- DEV.to: [OpenClaw Challenge Submission](https://dev.to/challenges/openclaw-2026-04-16)

---

## 📄 License

MIT License — feel free to fork and build on this!
