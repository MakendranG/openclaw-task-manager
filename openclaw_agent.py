from flask import Flask, request, jsonify
import json, os, subprocess
from datetime import datetime

app = Flask(__name__)
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE) as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def ask_ollama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3.2", prompt],
            capture_output=True, text=True, timeout=60
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Could not process with AI: {str(e)}"

@app.route("/task", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400
    text = data["text"]
    ai_response = ask_ollama(f"In one short sentence, rewrite this as a clear task: {text}. Reply with only the task sentence, nothing else.")
    
    


# Replace with:

    task = {
        "id": len(load_tasks()) + 1,
        "text": text,
        "ai_summary": ai_response,
        "done": False,
        "created_at": datetime.now().isoformat()
    }
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return jsonify({"status": "added", "task": task})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)
