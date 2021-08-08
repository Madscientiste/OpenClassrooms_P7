import time
from pprint import pprint

import numpy as np
import pandas as waifu

config = {
    "sep": ",",
    "dtype": {"name": str, "price": np.float64, "rate": np.float64},
}

start = time.process_time()

dataframe = waifu.read_csv("./_data/dataset_bruteforce.csv", **config)
dataframe["profit"] = dataframe["price"] * dataframe["rate"] / 100
dataframe = dataframe.sort_values(by=["profit"], ascending=False)

# The Capacity is the budget
# The Weight is the price
def knapsack(budget, rows: list, selected: list = []):
    if rows:
        sum1, val1 = knapsack(budget, rows[1:], selected)
        value = rows[0]

        if value[1] <= budget:
            selected.append(value)
            sum2, val2 = knapsack(budget - value[1], rows[1:0], selected)

            if sum1 < sum2:
                return sum2, val2

        return sum1, val1
    else:
        return sum([i[3] for i in selected]), selected


# [name, price, rate, profit]
rows = dataframe.values.tolist()
pprint(knapsack(500, rows))
print(f"Taken : {time.process_time() - start}s")
