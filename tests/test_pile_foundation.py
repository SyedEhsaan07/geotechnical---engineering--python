import unittest

from soil_mechanics.pile_foundation import (
    analyze_pile_options,
    capacity_vs_depth,
    optimize_pile_configuration,
    pile_area,
    pile_group_efficiency,
    required_number_of_piles,
    single_pile_capacity,
)


class TestPileFoundation(unittest.TestCase):
    def test_pile_area(self):
        self.assertAlmostEqual(pile_area(0.5), 0.1963495408, places=7)

    def test_single_pile_capacity(self):
        result = single_pile_capacity(
            diameter_m=0.5,
            length_m=15,
            end_bearing_pressure_kpa=2400,
            skin_friction_kpa=70,
            safety_factor=2.5,
        )
        self.assertGreater(result.ultimate_capacity_kN, result.allowable_capacity_kN)
        self.assertAlmostEqual(
            result.ultimate_capacity_kN,
            result.base_capacity_kN + result.shaft_capacity_kN,
            places=6,
        )

    def test_capacity_vs_depth_monotonic(self):
        profile = capacity_vs_depth(
            diameter_m=0.5,
            depths_m=[8, 10, 12, 14],
            end_bearing_gradient_kpa_per_m=100,
            skin_friction_kpa=60,
            base_end_bearing_kpa=900,
        )
        capacities = [capacity for _, capacity in profile]
        self.assertEqual(capacities, sorted(capacities))

    def test_required_number_of_piles(self):
        self.assertEqual(required_number_of_piles(1000, 260), 4)

    def test_group_efficiency_bounds(self):
        eff = pile_group_efficiency(rows=3, cols=3, spacing_m=1.5, diameter_m=0.5)
        self.assertGreaterEqual(eff, 0.1)
        self.assertLessEqual(eff, 1.0)

    def test_analyze_pile_options_count(self):
        options = analyze_pile_options(
            diameters_m=[0.4, 0.5],
            lengths_m=[10, 12, 14],
            end_bearing_pressure_kpa=2000,
            skin_friction_kpa=65,
        )
        self.assertEqual(len(options), 6)

    def test_optimize_pile_configuration(self):
        result = optimize_pile_configuration(
            service_load_kN=5000,
            diameters_m=[0.4, 0.5, 0.6],
            lengths_m=[10, 12, 14],
            end_bearing_pressure_kpa=2200,
            skin_friction_kpa=70,
            soil_modulus_kpa=30000,
            settlement_limit_m=0.05,
            unit_cost_per_meter=100,
        )
        self.assertGreaterEqual(result.group_allowable_capacity_kN, result.service_load_kN)
        self.assertGreater(result.utilization_ratio, 0)
        self.assertLessEqual(result.utilization_ratio, 1)


if __name__ == "__main__":
    unittest.main()
