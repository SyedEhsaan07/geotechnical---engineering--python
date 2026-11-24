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


def flow_index(liquidity_limit_at_n1, liquidity_limit_at_n2, blows_n1, blows_n2):
    """
    Calculate flow index, If, from two Casagrande flow curve points.

    If = (w1 - w2) / log10(N2 / N1)
    """
    if blows_n1 <= 0 or blows_n2 <= 0:
        raise ValueError("blows_n1 and blows_n2 must be greater than 0.")
    if blows_n1 == blows_n2:
        raise ValueError("blows_n1 and blows_n2 must be different.")
    import math

    denominator = math.log10(blows_n2 / blows_n1)
    if denominator == 0:
        raise ValueError("Invalid blow count ratio for flow index calculation.")
    return (liquidity_limit_at_n1 - liquidity_limit_at_n2) / denominator


def toughness_index(plasticity_index_value, flow_index_value):
    """Calculate toughness index, It = PI / If."""
    if flow_index_value == 0:
        raise ValueError("flow_index_value must be non-zero.")
    return plasticity_index_value / flow_index_value
