import json

INPUT_DATA = 'input.json'


def task() -> float:
    with open(INPUT_DATA) as f:
        json_data = json.load(f)
    count = sum(item["score"] * item["weight"] for item in json_data)
    return round(count, 3)


print(task())
