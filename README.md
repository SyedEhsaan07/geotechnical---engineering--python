# Geotechnical Engineering Toolkit (Python)

This repository is a lightweight Python toolkit for common **soil mechanics** calculations.

It is designed for:
- Civil/geotechnical engineering students
- Quick hand-checks during assignments or design studies
- Reusable utility functions for larger geotechnical scripts

---

## What this project actually is

This is **not** a full software application with a GUI or web interface.

It is a **Python package of calculation functions** grouped by topic:
- Phase relationships
- Consistency (Atterberg limits)
- Compaction and density control

You import functions, pass input values, and get computed outputs.

---

## Repository structure

```text
geotechnical---engineering--python/
├── README.md
└── soil_mechanics/
    ├── __init__.py
    ├── phase_relationships.py
    ├── consistency_limits.py
    └── compaction.py
```

- `soil_mechanics/__init__.py` exposes the public API so you can import directly from `soil_mechanics`.

---

## Included calculations

### 1) Phase relationships (`soil_mechanics.phase_relationships`)
- `water_content(mass_water, mass_dry_soil)`
- `void_ratio_from_porosity(porosity)`
- `porosity_from_void_ratio(void_ratio)`
- `degree_of_saturation(water_content_percent, specific_gravity, void_ratio)`
- `dry_unit_weight(specific_gravity, void_ratio, gamma_w=9.81)`
- `saturated_unit_weight(specific_gravity, void_ratio, gamma_w=9.81)`
- `submerged_unit_weight(specific_gravity, void_ratio, gamma_w=9.81)`

### 2) Consistency limits (`soil_mechanics.consistency_limits`)
- `plasticity_index(liquid_limit, plastic_limit)`
- `liquidity_index(water_content, plastic_limit, plasticity_index_value)`
- `consistency_index(liquid_limit, water_content, plasticity_index_value)`
- `shrinkage_index(plastic_limit, shrinkage_limit)`
- `flow_index(liquidity_limit_at_n1, liquidity_limit_at_n2, blows_n1, blows_n2)`
- `toughness_index(plasticity_index_value, flow_index_value)`

### 3) Compaction (`soil_mechanics.compaction`)
- `zero_air_voids_dry_unit_weight(water_content_percent, specific_gravity, gamma_w=9.81)`
- `relative_compaction(field_dry_unit_weight, maximum_lab_dry_unit_weight)`
- `dry_density_index(maximum_void_ratio, minimum_void_ratio, in_situ_void_ratio)`

---

## How to make it work (setup)

### Option A: Run directly in this repository
1. Install Python 3.9+.
2. Open terminal in the repository root.
3. Run Python and import functions.

Example:
```python
from soil_mechanics import water_content, plasticity_index

w = water_content(20, 100)
pi = plasticity_index(45, 25)

print("Water content (%) =", w)
print("Plasticity Index =", pi)
```

### Option B: Use in another script
If your script is outside this repo, either:
- add this repository to your `PYTHONPATH`, or
- copy the `soil_mechanics` folder into your project.

---

## Usage examples

### Example 1: Phase relationships
```python
from soil_mechanics import (
    water_content,
    void_ratio_from_porosity,
    degree_of_saturation,
    dry_unit_weight,
)

w = water_content(18, 90)                     # 20.0 %
e = void_ratio_from_porosity(0.40)            # 0.667
s = degree_of_saturation(20, 2.70, 0.667)     # about 81%
gamma_d = dry_unit_weight(2.70, 0.667)        # kN/m^3
```

### Example 2: Atterberg limits
```python
from soil_mechanics import plasticity_index, liquidity_index, consistency_index

ll = 52
pl = 26
w_natural = 30

pi = plasticity_index(ll, pl)                 # 26
li = liquidity_index(w_natural, pl, pi)
ci = consistency_index(ll, w_natural, pi)
```

### Example 3: Compaction checks
```python
from soil_mechanics import (
    zero_air_voids_dry_unit_weight,
    relative_compaction,
    dry_density_index,
)

gamma_d_zav = zero_air_voids_dry_unit_weight(12, 2.68)
rc = relative_compaction(17.8, 18.5)          # %
id_percent = dry_density_index(0.90, 0.50, 0.62)
```

---

## Input conventions and notes

- Water content input is usually **percentage** where function names indicate `_percent`.
- Unit weights use **kN/m³** with default `gamma_w = 9.81 kN/m³`.
- Most functions include basic validity checks and raise `ValueError` for invalid inputs (like division by zero or impossible ranges).
- Always keep units consistent across your calculations.

---

## Quick verification

From repository root:

```bash
python -m compileall .
```

If this completes without errors, your package files are importable.

---

## Future improvements you can add

- Permeability/seepage utilities (Darcy flow, equivalent permeability)
- Consolidation settlement utilities
- Bearing capacity and earth pressure helpers
- Unit tests with `pytest`
- Packaging for installation with `pip`
