# Geotechnical Engineering Python Toolkit

This repository provides Python modules for core geotechnical calculations, with a complete **pile foundation design workflow** for building projects.

## Project scope (based on your assignment)

The toolkit now supports:
- Modular pile-capacity functions
- Analysis for multiple pile diameters and lengths
- Automatic estimation of required pile count
- Pile capacity vs depth profile generation
- Comparison of different pile arrangements
- Group capacity and settlement estimation
- Optimization of pile configuration by safety and quantity/cost

## Package structure

- `soil_mechanics/phase_relationships.py` – soil phase relationship calculations
- `soil_mechanics/consistency_limits.py` – Atterberg limits utilities
- `soil_mechanics/pile_foundation.py` – pile foundation design and optimization
- `soil_mechanics/__init__.py` – public API exports

## Quick usage

```python
from soil_mechanics import (
    analyze_pile_options,
    capacity_vs_depth,
    optimize_pile_configuration,
)

# 1) Analyze single-pile capacity for alternatives
options = analyze_pile_options(
    diameters_m=[0.4, 0.5, 0.6],
    lengths_m=[12, 15, 18],
    end_bearing_pressure_kpa=2400,
    skin_friction_kpa=70,
    safety_factor=2.5,
)

# 2) Capacity-vs-depth curve data for plotting
curve = capacity_vs_depth(
    diameter_m=0.5,
    depths_m=[8, 10, 12, 14, 16, 18],
    end_bearing_gradient_kpa_per_m=110,
    skin_friction_kpa=70,
    base_end_bearing_kpa=800,
)

# 3) Optimize pile group arrangement
best = optimize_pile_configuration(
    service_load_kN=8500,
    diameters_m=[0.4, 0.5, 0.6],
    lengths_m=[12, 15, 18],
    end_bearing_pressure_kpa=2400,
    skin_friction_kpa=70,
    safety_factor=2.5,
    spacing_ratio=3.0,
    unit_cost_per_meter=120,
    soil_modulus_kpa=25000,
    settlement_limit_m=0.04,
)

print(best)
```

## Running tests

From repository root:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Notes

- Units are assumed consistent with kN, m, and kPa.
- Capacity/settlement methods are simplified educational formulas suitable for coursework-level comparison studies.
