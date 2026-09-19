"""Basic Atterberg limits calculations for soil mechanics."""


def plasticity_index(liquid_limit, plastic_limit):
    """Calculate plasticity index (PI)."""
    return liquid_limit - plastic_limit


def liquidity_index(water_content, plastic_limit, plasticity_index_value):
    """Calculate liquidity index (LI)."""
    if plasticity_index_value == 0:
        raise ValueError("plasticity_index_value must be non-zero.")
    return (water_content - plastic_limit) / plasticity_index_value


def consistency_index(liquid_limit, water_content, plasticity_index_value):
    """Calculate consistency index (CI)."""
    if plasticity_index_value == 0:
        raise ValueError("plasticity_index_value must be non-zero.")
    return (liquid_limit - water_content) / plasticity_index_value


def shrinkage_index(plastic_limit, shrinkage_limit):
    """Calculate shrinkage index (SI)."""
    return plastic_limit - shrinkage_limit
