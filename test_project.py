import pytest

from project import compare_sales_to_target, display_labor_costs, display_food_costs, display_reviews

def test_compare_sales_to_target():
    assert compare_sales_to_target(6000) == 1000
    assert compare_sales_to_target(4000) == -1000

def test_display_labor_costs():
    assert display_labor_costs(1000, 5000) == 20.0
    assert display_labor_costs(2000, 5000) == 40.0

def test_display_food_costs():
    assert display_food_costs(1000, 5000) == 20.0
    assert display_food_costs(1500, 5000) == 30.0

def test_display_reviews():
    assert display_reviews(4.9) == 4.9
    assert display_reviews(4.7) == 4.7
