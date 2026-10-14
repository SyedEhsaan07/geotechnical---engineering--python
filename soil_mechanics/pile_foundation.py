"""Pile foundation analysis utilities for geotechnical design studies."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import atan, ceil, degrees, pi
from typing import Iterable, List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class PileCapacity:
    """Capacity summary for a single pile."""

    diameter_m: float
    length_m: float
    base_capacity_kN: float
    shaft_capacity_kN: float
    ultimate_capacity_kN: float
    allowable_capacity_kN: float
    safety_factor: float


@dataclass(frozen=True)
class PileGroupResult:
    """Design and performance summary for a candidate pile group."""

    diameter_m: float
    length_m: float
    rows: int
    cols: int
    count: int
    spacing_m: float
    efficiency: float
    group_ultimate_capacity_kN: float
    group_allowable_capacity_kN: float
    service_load_kN: float
    utilization_ratio: float
    estimated_settlement_m: Optional[float]
    total_cost: float


def _require_positive(name: str, value: float) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero.")


def pile_area(diameter_m: float) -> float:
    """Return pile base area (m²)."""
    _require_positive("diameter_m", diameter_m)
    return pi * (diameter_m**2) / 4


def pile_perimeter(diameter_m: float) -> float:
    """Return pile perimeter (m)."""
    _require_positive("diameter_m", diameter_m)
    return pi * diameter_m


def single_pile_capacity(
    diameter_m: float,
    length_m: float,
    end_bearing_pressure_kpa: float,
    skin_friction_kpa: float,
    safety_factor: float = 2.5,
) -> PileCapacity:
    """Compute single-pile ultimate and allowable capacities in kN."""
    _require_positive("length_m", length_m)
    _require_positive("end_bearing_pressure_kpa", end_bearing_pressure_kpa)
    _require_positive("skin_friction_kpa", skin_friction_kpa)
    _require_positive("safety_factor", safety_factor)

    base_capacity = pile_area(diameter_m) * end_bearing_pressure_kpa
    shaft_capacity = pile_perimeter(diameter_m) * length_m * skin_friction_kpa
    ultimate_capacity = base_capacity + shaft_capacity
    allowable_capacity = ultimate_capacity / safety_factor

    return PileCapacity(
        diameter_m=diameter_m,
        length_m=length_m,
        base_capacity_kN=base_capacity,
        shaft_capacity_kN=shaft_capacity,
        ultimate_capacity_kN=ultimate_capacity,
        allowable_capacity_kN=allowable_capacity,
        safety_factor=safety_factor,
    )


def capacity_vs_depth(
    diameter_m: float,
    depths_m: Iterable[float],
    end_bearing_gradient_kpa_per_m: float,
    skin_friction_kpa: float,
    base_end_bearing_kpa: float = 0.0,
    safety_factor: float = 2.5,
) -> List[Tuple[float, float]]:
    """Generate allowable pile capacity (kN) versus depth (m)."""
    _require_positive("end_bearing_gradient_kpa_per_m", end_bearing_gradient_kpa_per_m)
    _require_positive("skin_friction_kpa", skin_friction_kpa)

    profile = []
    for depth_m in depths_m:
        _require_positive("depth_m", depth_m)
        end_bearing_pressure = base_end_bearing_kpa + end_bearing_gradient_kpa_per_m * depth_m
        result = single_pile_capacity(
            diameter_m=diameter_m,
            length_m=depth_m,
            end_bearing_pressure_kpa=end_bearing_pressure,
            skin_friction_kpa=skin_friction_kpa,
            safety_factor=safety_factor,
        )
        profile.append((depth_m, result.allowable_capacity_kN))
    return profile


def required_number_of_piles(
    service_load_kN: float,
    allowable_single_capacity_kN: float,
    efficiency: float = 1.0,
) -> int:
    """Compute required pile count for a service load."""
    _require_positive("service_load_kN", service_load_kN)
    _require_positive("allowable_single_capacity_kN", allowable_single_capacity_kN)
    _require_positive("efficiency", efficiency)
    return ceil(service_load_kN / (allowable_single_capacity_kN * efficiency))


def pile_group_efficiency(rows: int, cols: int, spacing_m: float, diameter_m: float) -> float:
    """Estimate group efficiency with a Converse-Labarre type relation."""
    if rows < 1 or cols < 1:
        raise ValueError("rows and cols must be at least 1")
    _require_positive("spacing_m", spacing_m)

    if rows == 1 and cols == 1:
        return 1.0

    theta_deg = degrees(atan(diameter_m / spacing_m))
    reduction = theta_deg * ((rows - 1) * cols + (cols - 1) * rows) / (90 * rows * cols)
    return max(0.1, min(1.0, 1.0 - reduction))


def arrangement_dimensions(rows: int, cols: int, spacing_m: float, diameter_m: float) -> Tuple[float, float, float]:
    """Return group length, width, and plan area in meters/m²."""
    if rows < 1 or cols < 1:
        raise ValueError("rows and cols must be at least 1")
    _require_positive("spacing_m", spacing_m)

    length_m = (rows - 1) * spacing_m + diameter_m
    width_m = (cols - 1) * spacing_m + diameter_m
    return length_m, width_m, length_m * width_m


def settlement_estimate(
    service_load_kN: float,
    rows: int,
    cols: int,
    spacing_m: float,
    diameter_m: float,
    soil_modulus_kpa: float,
    poisson_ratio: float = 0.3,
    influence_factor: float = 1.0,
) -> float:
    """Estimate immediate settlement (m) using an elastic approximation."""
    _require_positive("soil_modulus_kpa", soil_modulus_kpa)

    _, width_m, area_m2 = arrangement_dimensions(rows, cols, spacing_m, diameter_m)
    contact_pressure_kpa = service_load_kN / area_m2
    return (
        contact_pressure_kpa
        * width_m
        * (1 - poisson_ratio**2)
        * influence_factor
        / soil_modulus_kpa
    )


def analyze_pile_options(
    diameters_m: Sequence[float],
    lengths_m: Sequence[float],
    end_bearing_pressure_kpa: float,
    skin_friction_kpa: float,
    safety_factor: float = 2.5,
) -> List[PileCapacity]:
    """Analyze all diameter/length combinations for single pile capacity."""
    return [
        single_pile_capacity(
            diameter_m=diameter,
            length_m=length,
            end_bearing_pressure_kpa=end_bearing_pressure_kpa,
            skin_friction_kpa=skin_friction_kpa,
            safety_factor=safety_factor,
        )
        for diameter, length in product(diameters_m, lengths_m)
    ]


def optimize_pile_configuration(
    service_load_kN: float,
    diameters_m: Sequence[float],
    lengths_m: Sequence[float],
    end_bearing_pressure_kpa: float,
    skin_friction_kpa: float,
    safety_factor: float = 2.5,
    spacing_ratio: float = 3.0,
    max_rows: int = 8,
    max_cols: int = 8,
    unit_cost_per_meter: float = 1.0,
    settlement_limit_m: Optional[float] = None,
    soil_modulus_kpa: Optional[float] = None,
) -> PileGroupResult:
    """Find a cost-efficient and safe pile-group configuration."""
    _require_positive("service_load_kN", service_load_kN)
    _require_positive("spacing_ratio", spacing_ratio)
    _require_positive("unit_cost_per_meter", unit_cost_per_meter)

    best: Optional[PileGroupResult] = None

    for diameter, length in product(diameters_m, lengths_m):
        single = single_pile_capacity(
            diameter_m=diameter,
            length_m=length,
            end_bearing_pressure_kpa=end_bearing_pressure_kpa,
            skin_friction_kpa=skin_friction_kpa,
            safety_factor=safety_factor,
        )
        spacing = spacing_ratio * diameter

        for rows, cols in product(range(1, max_rows + 1), range(1, max_cols + 1)):
            count = rows * cols
            efficiency = pile_group_efficiency(rows, cols, spacing, diameter)
            group_allowable = count * single.allowable_capacity_kN * efficiency

            if group_allowable < service_load_kN:
                continue

            utilization = service_load_kN / group_allowable
            settlement = None
            if soil_modulus_kpa is not None:
                settlement = settlement_estimate(
                    service_load_kN=service_load_kN,
                    rows=rows,
                    cols=cols,
                    spacing_m=spacing,
                    diameter_m=diameter,
                    soil_modulus_kpa=soil_modulus_kpa,
                )
                if settlement_limit_m is not None and settlement > settlement_limit_m:
                    continue

            candidate = PileGroupResult(
                diameter_m=diameter,
                length_m=length,
                rows=rows,
                cols=cols,
                count=count,
                spacing_m=spacing,
                efficiency=efficiency,
                group_ultimate_capacity_kN=count * single.ultimate_capacity_kN * efficiency,
                group_allowable_capacity_kN=group_allowable,
                service_load_kN=service_load_kN,
                utilization_ratio=utilization,
                estimated_settlement_m=settlement,
                total_cost=count * length * unit_cost_per_meter,
            )

            if best is None:
                best = candidate
                continue

            rank_current = (
                candidate.total_cost,
                candidate.count,
                -candidate.utilization_ratio,
                candidate.estimated_settlement_m
                if candidate.estimated_settlement_m is not None
                else float("inf"),
            )
            rank_best = (
                best.total_cost,
                best.count,
                -best.utilization_ratio,
                best.estimated_settlement_m
                if best.estimated_settlement_m is not None
                else float("inf"),
            )
            if rank_current < rank_best:
                best = candidate

    if best is None:
        raise ValueError("No configuration satisfies the provided constraints.")

    return best
