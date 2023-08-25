# TODO решите задачу
import json

file_input = 'input.json'

def task() -> float:
    with open(file_input, 'r') as file:
        data = json.load(file)

    total = sum(item['score'] * item['weight'] for item in data)
    return round(total, 3)


print(task())
