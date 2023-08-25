# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as input_file:
        lines = [line for line in csv.DictReader(input_file)]

    # TODO считать содержимое csv файла

# TODO Сериализовать в файл с отступами равными 4

    with open(OUTPUT_FILENAME, 'w') as output_file:
        json.dump(lines, output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
