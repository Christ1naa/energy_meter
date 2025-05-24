import json
from config import HISTORY_PATH

def save_to_history(meter_id, prev_data):
    try:
        with open(HISTORY_PATH, "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = {}

    if meter_id not in history:
        history[meter_id] = []

    history[meter_id].append(prev_data)

    with open(HISTORY_PATH, "w") as f:
        json.dump(history, f, indent=2)
