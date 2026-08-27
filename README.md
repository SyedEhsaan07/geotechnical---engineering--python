"""
Soil Phase Relationships
Basic calculations for geotechnical engineering.
"""

def water_content(mass_water, mass_dry_soil):
    return (mass_water / mass_dry_soil) * 100


def void_ratio(porosity):
    return porosity / (1 - porosity)


def porosity(void_ratio):
    return void_ratio / (1 + void_ratio)


def degree_of_saturation(water_content, specific_gravity, void_ratio):
    return (water_content * specific_gravity) / void_ratio


def dry_unit_weight(specific_gravity, void_ratio, gamma_w=9.81):
    return (specific_gravity * gamma_w) / (1 + void_ratio)


if __name__ == "__main__":
    print("Soil Phase Relationships Calculator")
