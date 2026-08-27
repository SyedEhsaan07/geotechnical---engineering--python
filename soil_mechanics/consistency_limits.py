"""
Consistency Limits
Basic Atterberg limits calculations for geotechnical engineering.
"""


def plasticity_index(liquid_limit, plastic_limit):
    """Calculate plasticity index (PI)."""
    return liquid_limit - plastic_limit


def liquidity_index(natural_water_content, plastic_limit, plasticity_index_value):
    """Calculate liquidity index (LI)."""
    return (
        (natural_water_content - plastic_limit)
        / plasticity_index_value
    )


def consistency_index(liquid_limit, natural_water_content, plasticity_index_value):
    """Calculate consistency index (CI)."""
    return (
        (liquid_limit - natural_water_content)
        / plasticity_index_value
    )


def shrinkage_index(plastic_limit, shrinkage_limit):
    """Calculate shrinkage index (SI)."""
    return plastic_limit - shrinkage_limit


if __name__ == "__main__":
    print("Atterberg Limits Calculator")
