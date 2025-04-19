import hashlib
import time

def log_decision(agent_name, task, result):
    timestamp = time.time()
    hash_val = hashlib.sha256(result.encode()).hexdigest()
    log_entry = {
        "timestamp": timestamp,
        "agent": agent_name,
        "task": task,
        "hash": hash_val,
        "output": result
    }
    print("🧾 MASUMI LOG:", log_entry)
