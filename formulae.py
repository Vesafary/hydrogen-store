import math


def capilary_pressure(gamma: float, theta: float, r: float) -> float:
    """
    :param gamma: Interfacial pressure between gas and water
    :param theta: Receding contact angle
    :param r: Pore throat radius of caprock
    :return: Capilary pressure
    """
    return 2 * gamma / 1000 * math.cos(theta * math.pi / 180) / r


def column_height(gamma: float, theta: float, r: float, delta_rho: float) -> float:
    """
    :param gamma: Interfacial pressure between gas and water
    :param theta: Receding contact angle
    :param r: Pore throat radius of caprock
    :param delta_rho: Density difference between caprock and gas
    :return: Capilary pressure
    """
    return capilary_pressure(gamma, theta, r) / (delta_rho * 9.81)


def gamma(pressure: float, temperature: float, salinity: float) -> float:
    """
    See https://www.sciencedirect.com/science/article/pii/S0920410522003278?via%3Dihub
    H2−brine interfacial tension as a function of salinity, temperature, and pressure; implications for hydrogen geo-storage

    :param pressure: Pressure in MPa
    :param temperature: Temperature in K
    :param salinity: Salinity in mol/kg
    :return: Gamma in mN/m
    """
    A = -0.47876 - 0.01004 * pressure + 0.00593 * temperature

    B = 135.41479 - 0.38368 * pressure - 0.20520 * temperature + 0.00084 * pressure * temperature 

    return A * salinity + B
