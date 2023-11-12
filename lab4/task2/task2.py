import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as input_file:
        csv_data = csv.DictReader(input_file, delimiter=",", quotechar="\n")
        dict_result = []
        for row in csv_data:
            dict_result.append(dict(row))

    with open(OUTPUT_FILENAME, "w") as output_file:
        json.dump(dict_result, output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
