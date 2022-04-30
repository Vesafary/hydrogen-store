import math


def capilary_pressure(gamma: float, theta: float, r: float) -> float:
    """
    :param gamma: Interfacial pressure between gas and water
    :param theta: Receding contact angle
    :param r: Pore throat radius of caprock
    :return: Capilary pressure
    """
    return 2 * gamma * math.cos(theta) / r

