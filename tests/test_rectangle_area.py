from pytestpackage.calc_areas import calc_area_rectangle
import pytest


class TestRectanglea:
    def test_rect_area(self):
        assert calc_area_rectangle(2, 3) == 6

    def test_zero_side(self):
        assert calc_area_rectangle(0, 2) == 0

    def test_float_sides(self):
        assert calc_area_rectangle(2.0, 6.0) == 12

    def test_string_radius(self):
        with pytest.raises(TypeError):
            calc_area_rectangle("two", "six")
