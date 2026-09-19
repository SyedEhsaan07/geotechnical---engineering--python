"""Compaction and density-control calculations for geotechnical engineering."""


def zero_air_voids_dry_unit_weight(
    water_content_percent, specific_gravity, gamma_w=9.81
):
    """
    Calculate theoretical zero-air-voids dry unit weight, γd(zav) (kN/m³).

    γd(zav) = (Gs × γw) / (1 + w × Gs)
    where w is water content as decimal.
    """
    if specific_gravity <= 0:
        raise ValueError("specific_gravity must be greater than 0.")
    if gamma_w <= 0:
        raise ValueError("gamma_w must be greater than 0.")
    water_content_decimal = water_content_percent / 100
    if water_content_decimal < 0:
        raise ValueError("water_content_percent must be non-negative.")
    return (specific_gravity * gamma_w) / (1 + water_content_decimal * specific_gravity)


def relative_compaction(field_dry_unit_weight, maximum_lab_dry_unit_weight):
    """
    Calculate relative compaction, RC (%).

    RC = (field dry unit weight / maximum laboratory dry unit weight) × 100
    """
    if maximum_lab_dry_unit_weight == 0:
        raise ValueError("maximum_lab_dry_unit_weight must be non-zero.")
    return (field_dry_unit_weight / maximum_lab_dry_unit_weight) * 100


def dry_density_index(maximum_void_ratio, minimum_void_ratio, in_situ_void_ratio):
    """
    Calculate density index (relative density), ID (%), for granular soils.

    ID = ((emax - e) / (emax - emin)) × 100
    """
    if maximum_void_ratio <= minimum_void_ratio:
        raise ValueError("maximum_void_ratio must be greater than minimum_void_ratio.")
    return (
        (maximum_void_ratio - in_situ_void_ratio)
        / (maximum_void_ratio - minimum_void_ratio)
    ) * 100
