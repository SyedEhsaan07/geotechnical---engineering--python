# Geotechnical Engineering (Python)

Simple, reusable Python functions for common geotechnical engineering calculations.

## Included modules

- `soil_mechanics.phase_relationships`
  - Water content
  - Void ratio / porosity conversions
  - Degree of saturation
  - Dry unit weight
- `soil_mechanics.consistency_limits`
  - Plasticity index
  - Liquidity index
  - Consistency index
  - Shrinkage index

## Quick example

```python
from soil_mechanics.phase_relationships import water_content
from soil_mechanics.consistency_limits import plasticity_index

w = water_content(20, 100)              # 20%
pi = plasticity_index(45, 25)           # 20
```

## Notes

- Inputs are expected in standard geotechnical units and conventions described in function docstrings.
- This repository is intended as a lightweight educational/reference toolkit.
