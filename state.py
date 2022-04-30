class EnvironmentState:
    r = None
    temperature = None
    pressure = None

    def __init__(self, r: float, temperature: float, pressure: float):
        self.r = r
        self.temperature = temperature
        self.pressure = pressure
