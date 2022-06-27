import json
import matplotlib.pyplot as plt

from collections import defaultdict
from formulae import *
from random import random
from typing import List, Tuple

from result import Result, Series


def main():
    rock_types, data = read_data()

    res = {}

    pore_size_range = (1, 100)
    salinity_range = (0.5, 3.5)

    for source in data:
        rt = source["rock_type"]
            
        if rt not in res:
            res[rt] = Series(rt)

        for _ in range(100):
            pore_size = round((pore_size_range[1] - pore_size_range[0]) * random() + pore_size_range[0]) / 10**9
            salinity = round((salinity_range[1] - salinity_range[0]) * random(), 2) + salinity_range[0]
            res[rt].run(source["data"], pore_size, salinity)

    for _, series in res.items():
        series.plot()


def read_data():
    with open("rock_types.json") as rf:
        rock_types = json.load(rf)
    with open("data.json") as df:
        data = json.load(df)

    return rock_types, data


if __name__ == '__main__':
    main()
