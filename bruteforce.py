from time import time
from datetime import timedelta
import csv
from pprint import pprint


def rows_from_a_csv_file(filename, dialect="excel", **fmtparams):
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file, dialect, **fmtparams)
        next(reader, None)
        for row in reader:
            yield row


# name, price, rate
rows = []
file = "./_data/dataset_bruteforce.csv"

for row in rows_from_a_csv_file(file):
    name = row[0]
    price = float(row[1])
    rate = float(row[2])
    profit = (price * rate) / 100

    rows.append([name, price, rate, profit])

# The Capacity is the budget
# The Weight is the price
# The value is the profit
def knapsack(budget, rows: list, selected: list = []):
    """Time Complecity : O(2^n)"""

    if rows:
        sum_profit1, val1, cost1 = knapsack(budget, rows[1:], selected)
        value = rows[0]

        if value[1] <= budget:
            sum_profit2, val2, cost2 = knapsack(budget - value[1], rows[1:], selected + [value])

            if sum_profit1 < sum_profit2:
                return sum_profit2, val2, cost2

        return sum_profit1, val1, cost1
    else:
        return sum([i[3] for i in selected]), selected, sum([i[2] for i in selected])


# [name, price, rate, profit]
runtimeA = time()
profitable, items, cost = knapsack(500, rows)
result = {"cost": cost, "profitable": profitable, "bought": items}
runtimeB = time()

pprint(result, sort_dicts=False)
print(f"Executed in {timedelta(seconds=runtimeB - runtimeA)} for {len(rows)}rows in {file}")
print()
