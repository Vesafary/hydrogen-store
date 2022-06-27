import math
from brine_table import brine_table


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
    :param delta_rho: Density difference between brine and gas
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


def delta_rho(pressure: float, temperature: float, salinity: float) -> float:
    """
    """
    R = 8.314472
    return density_brine(temperature, salinity) - (pressure * 2.016) / (R * temperature)


def density_brine(temperature: float, salinity: float) -> float:
    """
    Makes a linear interpolation of the table from brine_table.py, which is copied from 
    https://www.journal-of-agroalimentary.ro/admin/articole/58458L8_Vol_21(1)_2015_41_52.pdf
    
    Interpolation between both concentration and temperature.
    Assumes the salt is NaCl.

    :param temperature: Temperature in K
    :param salinity: Salinity in g / L
    :return: density in gram / L
    """

    weight_water = 998.17
    molar_weight_salt = 58.443
    
    weight_percentage = salinity * molar_weight_salt / weight_water * 100
    print(weight_percentage)

    available_percentages = sorted(brine_table.keys())
    
    keys_to_take = []

    for a, b in zip(available_percentages, available_percentages[1::]):
        if a <= weight_percentage <= b:
            keys_to_take = [a, b]
            break
    
    density = 0

    for key in keys_to_take:
        available_temperatures = sorted(brine_table.get(key).keys())
        for (a, b) in zip(available_temperatures, available_temperatures[1::]):
            if a <= temperature <= b:
                ta_diff = temperature - a
                tb_diff = temperature - b
                density += (key / sum(keys_to_take)) * (a / (a + b)) * brine_table.get(key).get(a)
                density += (key / sum(keys_to_take)) * (b / (a + b)) * brine_table.get(key).get(b)
                break
    
    return density