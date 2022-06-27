import matplotlib.pyplot as plt

from formulae import *


class Result:
    temperature: float = 0
    rock_type: int = 0
    data: dict = {}
    angle_type: str = None
    
    def __init__(self, temperature, rock_type, angle_type):
        self.temperature = temperature
        self.rock_type = rock_type
        self.data = {}
        self.angle_type = angle_type
    
    def point(self, x, y):
        if x not in self.data:
            self.data[x] = []
        self.data[x].append(y)

    def finish(self):
        xs = sorted(self.data.keys())
        ys = []
        errs = []

        for x in xs:
            average = sum(self.data[x]) / len(self.data[x])

            ys.append(average)
            errs.append([max([average - y for y in self.data[x]]), max([y - average for y in self.data[x]])])
        
        return xs, ys, list(zip(*errs))


class Series:
    rock_type: str = None
    results = None
    

    def __init__(self, rock_type):
        self.rock_type = rock_type
        self.results = {}

    def run(self, data, pore_size, salinity):
        for series in data:
            temperature = series['temperature']
            angle_type = series['type']
            
            if (temperature, angle_type) not in self.results:
                self.results[(temperature, angle_type)] = Result(temperature, self.rock_type, angle_type)

            for datapoint in series["points"]:
                g = gamma(datapoint["pressure"], temperature, salinity)
                dr = delta_rho(datapoint["pressure"], temperature, salinity)

                self.results[(temperature, angle_type)].point(
                    datapoint["pressure"],
                    column_height(g, datapoint['contact_angle'], pore_size, dr)
                )

    def plot(self):
        for (temperature, angle_type), res in self.results.items():
            xs, ys, errs = res.finish()

            plt.errorbar(xs, ys, yerr=errs, label=temperature)
        print(self.rock_type)
        plt.show()
