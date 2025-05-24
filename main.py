from meter import process_meter

if __name__ == "__main__":
    meter_id = input("Введіть номер лічильника: ")
    date = input("Введіть дату (YYYY-MM-DD): ")
    day = int(input("Денний показник: "))
    night = int(input("Нічний показник: "))

    result = process_meter(meter_id, date, {"day": day, "night": night})
    print("Результат:")
    print(result)
