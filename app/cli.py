from app.meter_logic import process_meter_data

def run_cli():
    meter_id = input("Номер лічильника: ")
    date = input("Дата (YYYY-MM-DD): ")
    day = int(input("Денний показник: "))
    night = int(input("Нічний показник: "))

    result = process_meter_data({
        "id": meter_id,
        "date": date,
        "readings": {"day": day, "night": night}
    })

    if "warning" in result:
        print(result["warning"])
        confirm = input("Підтвердити накрутку? (y/n): ")
        if confirm.lower() != "y":
            print("Введіть коректні дані.")
            return

    print("✅ Результат обробки:")
    print(result)
