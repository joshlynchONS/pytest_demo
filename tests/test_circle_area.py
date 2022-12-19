from pytestpackage.calc_areas import calc_area_circle
import pytest
import math


class TestCircle:
    def test_circ_area(self):
        assert calc_area_circle(2) == (math.pi * (2) ** 2)

    def test_zero_radius(self):
        assert calc_area_circle(0) == 0

    def test_float_radius(self):
        assert calc_area_circle(2.0) == (math.pi * (2.0) ** 2)

    def test_string_radius(self):
        with pytest.raises(TypeError):
            calc_area_circle("two")
