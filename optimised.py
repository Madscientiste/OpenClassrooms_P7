from time import time
from datetime import timedelta
from pprint import pprint
import csv
import math

files = ["./_data/dataset1_Python+P7.csv", "./_data/dataset2_Python+P7.csv"]


def rows_from_a_csv_file(filename, dialect="excel", **fmtparams):
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file, dialect, **fmtparams)
        next(reader, None)
        for row in reader:
            yield row


for file in files:
    rows = []

    for row in rows_from_a_csv_file(file):
        name = row[0]
        price = int(float(row[1]) * 100)
        rate = float(row[2])
        profit = (price * rate) / 100

        if price <= 0:
            continue

        rows.append([name, price, profit])

    # The Capacity is the budget
    # The Weight is the price
    # The value is the profit
    def knapsack_dyn(budget, elements):
        indexer = [[0 for x in range(budget + 1)] for x in range(len(elements) + 1)]

        for x in range(1, len(elements) + 1):
            for y in range(1, budget + 1):
                elem = elements[x - 1]

                elem_price = elem[1]
                elem_profit = elem[2]

                if elem_price <= y:
                    arg1 = elem_profit + indexer[x - 1][math.floor(y - elem_profit)]
                    arg2 = indexer[x - 1][y]

                    indexer[x][y] = max(arg1, arg2)
                else:
                    indexer[x][y] = indexer[x - 1][y]

        b = budget
        elem_count = len(elements)
        selected = []

        while b >= 0 and elem_count >= 0:
            elem = elements[elem_count - 1]
            elem_price = elem[1]
            elem_profit = elem[2]

            if indexer[elem_count][b] == indexer[elem_count - 1][b - elem_price] + elem_profit:
                selected.append(elem)
                b -= elem_price

            elem_count -= 1

        return {
            "cost": sum([i[1] for i in selected]),
            "profitable": sum([i[2] for i in selected]),
            "bought": selected,
        }

    runtimeA = time()
    result = knapsack_dyn(500, rows)
    runtimeB = time()

    pprint(result, sort_dicts=False)
    print(f"Executed in {timedelta(seconds=runtimeB - runtimeA)} for {len(rows)}rows in {file}")
    print()
