"""
Soil phase-relation calculations for geotechnical engineering.
"""


def water_content(mass_water, mass_dry_soil):
    """
    Calculate water content, w (%).

    w = (mass of water / mass of dry soil) × 100
    """
    if mass_dry_soil == 0:
        raise ValueError("mass_dry_soil must be non-zero.")
    return (mass_water / mass_dry_soil) * 100


def void_ratio_from_porosity(porosity):
    """
    Calculate void ratio, e, from porosity, n.

    e = n / (1 - n)
    """
    if not 0 < porosity < 1:
        raise ValueError("porosity must be between 0 and 1 (exclusive).")
    return porosity / (1 - porosity)


def porosity_from_void_ratio(void_ratio):
    """
    Calculate porosity, n, from void ratio, e.

    n = e / (1 + e)
    """
    if void_ratio < 0:
        raise ValueError("void_ratio must be non-negative.")
    return void_ratio / (1 + void_ratio)


def degree_of_saturation(water_content_percent, specific_gravity, void_ratio):
    """
    Calculate degree of saturation, S (%).

    S = (w × Gs / e) × 100
    """
    if specific_gravity <= 0:
        raise ValueError("specific_gravity must be greater than 0.")
    if void_ratio == 0:
        raise ValueError("void_ratio must be non-zero.")
    water_content_decimal = water_content_percent / 100
    return (water_content_decimal * specific_gravity / void_ratio) * 100


def dry_unit_weight(specific_gravity, void_ratio, gamma_w=9.81):
    """
    Calculate dry unit weight, γd (kN/m³).

    γd = (Gs × γw) / (1 + e)
    """
    if specific_gravity <= 0:
        raise ValueError("specific_gravity must be greater than 0.")
    if void_ratio < 0:
        raise ValueError("void_ratio must be non-negative.")
    if gamma_w <= 0:
        raise ValueError("gamma_w must be greater than 0.")
    return (specific_gravity * gamma_w) / (1 + void_ratio)
