import requests
import json

AGENT_URL = "http://127.0.0.1:3000"

def add_task(text):
    try:
        res = requests.post(
            f"{AGENT_URL}/task",
            json={"text": text},
            timeout=30
        )
        print(f"Status code: {res.status_code}")
        print(f"Raw response: {res.text}")

        if res.status_code == 200 and res.text.strip():
            data = res.json()
            print(f"✅ Task added: {data}")
        else:
            print("⚠️ Agent returned empty or non-JSON response")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to agent. Is openclaw_agent.py running?")
    except Exception as e:
        print(f"❌ Error: {e}")

def list_tasks():
    try:
        res = requests.get(f"{AGENT_URL}/tasks", timeout=10)
        if res.status_code == 200:
            tasks = res.json()
            print("\n📋 Current Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "✅" if task.get("done") else "⏳"
                print(f"  {i}. {status} {task.get('text', task)}")
        else:
            print("No tasks found.")
    except Exception as e:
        print(f"❌ Error listing tasks: {e}")

if __name__ == "__main__":
    print("OpenClaw Task Manager")
    print("Commands: add, list, exit")
    while True:
        cmd = input("\nEnter command: ").strip().lower()
        if cmd == "exit":
            break
        elif cmd == "list":
            list_tasks()
        elif cmd == "add":
            text = input("Enter task: ").strip()
            if text:
                add_task(text)
        else:
            add_task(cmd)
