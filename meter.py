import json
from config import TARIFFS, FAKE_INCREMENT, INITIAL_DATA_PATH
from history import save_to_history


def load_data():
    try:
        with open(INITIAL_DATA_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_data(data):
    with open(INITIAL_DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)


def calculate_bill(prev, curr):
    result = {}
    diffs = {}
    for period in ['day', 'night']:
        diff = curr[period] - prev[period]
        if diff < 0:
            diff += FAKE_INCREMENT[period]
            result['warning'] = f"Показник зменшився для {period}. Накручено {FAKE_INCREMENT[period]} кВт."
        diffs[period] = diff
        result[period + "_bill"] = diff * TARIFFS[period]
    result['total'] = result['day_bill'] + result['night_bill']
    return result, diffs


def process_meter(meter_id, date, new_data):
    data = load_data()
    prev = data.get(meter_id)

    if prev:
        save_to_history(meter_id, prev)
        result, diffs = calculate_bill(prev['readings'], new_data)
        data[meter_id] = {"date": date, "readings": new_data}
    else:
        result = {"info": "Новий лічильник. Дані збережено без обрахунку."}
        data[meter_id] = {"date": date, "readings": new_data}

    save_data(data)
    return result
