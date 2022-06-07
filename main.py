import json

from formulae import *


def main():
    rock_types, data = read_data()

    for source in data:
        for series in source["data"]:
            print("-----")
            print(f"{series['temperature']}K - {series['type']}")
            for datapoint in series["points"]:
                g = gamma(datapoint["pressure"], series["temperature"], 1.05)

                print(f"{capilary_pressure(g, datapoint['contact_angle'], 0.000000005) / 1000000} MPa")


def read_data():
    with open("rock_types.json") as rf:
        rock_types = json.load(rf)
    with open("data.json") as df:
        data = json.load(df)

    return rock_types, data


if __name__ == '__main__':
    main()
