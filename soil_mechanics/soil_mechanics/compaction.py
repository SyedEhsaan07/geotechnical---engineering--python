"""Basic soil compaction calculations for geotechnical engineering."""


def dry_unit_weight(bulk_unit_weight, water_content):
    """Calculate dry unit weight from bulk unit weight and water content.

    Parameters:
        bulk_unit_weight: Bulk/moist unit weight of soil.
        water_content: Water content as a decimal.

    Returns:
        Dry unit weight.
    """
    return bulk_unit_weight / (1 + water_content)


def water_content(mass_water, mass_dry_soil):
    """Calculate water content as a decimal.

    Parameters:
        mass_water: Mass of water.
        mass_dry_soil: Mass of dry soil.

    Returns:
        Water content as a decimal.
    """
    return mass_water / mass_dry_soil


def degree_of_saturation(water_content_value, specific_gravity, void_ratio):
    """Calculate degree of saturation as a percentage.

    Parameters:
        water_content_value: Water content as a decimal.
        specific_gravity: Specific gravity of soil solids.
        void_ratio: Void ratio.

    Returns:
        Degree of saturation in percent.
    """
    return (
        water_content_value * specific_gravity / void_ratio
    ) * 100


def void_ratio_from_dry_unit_weight(
    specific_gravity,
    dry_unit_weight_value,
    unit_weight_water=9.81,
):
    """Calculate void ratio from dry unit weight.

    Parameters:
        specific_gravity: Specific gravity of soil solids.
        dry_unit_weight_value: Dry unit weight of soil.
        unit_weight_water: Unit weight of water, default 9.81 kN/m³.

    Returns:
        Void ratio.
    """
    return (
        specific_gravity * unit_weight_water / dry_unit_weight_value
    ) - 1


def zero_air_voids_dry_unit_weight(
    specific_gravity,
    water_content_value,
    unit_weight_water=9.81,
):
    """Calculate dry unit weight at zero air voids.

    Parameters:
        specific_gravity: Specific gravity of soil solids.
        water_content_value: Water content as a decimal.
        unit_weight_water: Unit weight of water, default 9.81 kN/m³.

    Returns:
        Zero-air-voids dry unit weight.
    """
    return (
        specific_gravity * unit_weight_water
        / (1 + water_content_value * specific_gravity)
    )


def relative_compaction(field_dry_unit_weight, laboratory_max_dry_unit_weight):
    """Calculate relative compaction as a percentage.

    Parameters:
        field_dry_unit_weight: Field dry unit weight.
        laboratory_max_dry_unit_weight: Maximum dry unit weight from
            the laboratory compaction test.

    Returns:
        Relative compaction in percent.
    """
    return (
        field_dry_unit_weight / laboratory_max_dry_unit_weight
    ) * 100


def compaction_efficiency(
    field_dry_unit_weight,
    laboratory_max_dry_unit_weight,
):
    """Calculate the compaction efficiency ratio.

    Returns:
        Compaction efficiency as a decimal.
    """
    return field_dry_unit_weight / laboratory_max_dry_unit_weight


if __name__ == "__main__":
    print("Soil Compaction Calculator")
