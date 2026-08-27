"""
Soil Phase Relationships
Basic phase-relation calculations for geotechnical engineering.

Author: Syed Ehsaan
"""

def water_content(mass_water, mass_dry_soil):
    """
    Calculate water content, w (%).

    w = (mass of water / mass of dry soil) × 100
    """
    return (mass_water / mass_dry_soil) * 100


def void_ratio_from_porosity(porosity):
    """
    Calculate void ratio, e, from porosity, n.

    e = n / (1 - n)

    Porosity must be entered as a decimal.
    Example: 0.40 for 40%.
    """
    return porosity / (1 - porosity)


def porosity_from_void_ratio(void_ratio):
    """
    Calculate porosity, n, from void ratio, e.

    n = e / (1 + e)

    Returns porosity as a decimal.
    """
    return void_ratio / (1 + void_ratio)


def degree_of_saturation(water_content_percent, specific_gravity, void_ratio):
    """
    Calculate degree of saturation, S (%).

    S = (w × Gs / e) × 100

    water_content_percent is entered as a percentage.
    Example: 20 means 20%.
    """
    water_content_decimal = water_content_percent / 100
    return (water_content_decimal * specific_gravity / void_ratio) * 100


def dry_unit_weight(specific_gravity, void_ratio, gamma_w=9.81):
    """
    Calculate dry unit weight, γd (kN/m³).

    γd = (Gs × γw) / (1 + e)

    Default unit weight of water:
    γw = 9.81 kN/m³
    """
    return (specific_gravity * gamma_w) / (1 + void_ratio)


if __name__ == "__main__":
    print("Soil Phase Relationships Calculator")
    print("-----------------------------------")

    w = water_content(20, 100)
    e = void_ratio_from_porosity(0.40)
    n = porosity_from_void_ratio(0.667)
    S = degree_of_saturation(20, 2.70, 0.667)
    gamma_d = dry_unit_weight(2.70, 0.667)

    print(f"Water content: {w:.2f}%")
    print(f"Void ratio: {e:.3f}")
    print(f"Porosity: {n:.3f}")
    print(f"Degree of saturation: {S:.2f}%")
    print(f"Dry unit weight: {gamma_d:.2f} kN/m³")
