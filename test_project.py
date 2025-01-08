iimport pytest
from project import Metric, MetricScorecard

def test_clean_input_valid():
    assert Metric.clean_input("1000") == 1000.0
    assert Metric.clean_input("$1,234.56") == 1234.56

def test_clean_input_invalid():
    with pytest.raises(ValueError):
        Metric.clean_input("")
    with pytest.raises(ValueError):
        Metric.clean_input("abc")


def test_clean_input_review_valid():
    assert Metric.clean_input_review("4.5") == 4.5
    assert Metric.clean_input_review("1") == 1.0


def test_clean_input_review_invalid():
    with pytest.raises(ValueError):
        Metric.clean_input_review("")
    with pytest.raises(ValueError):
        Metric.clean_input_review("6")  # Out of range
    with pytest.raises(ValueError):
        Metric.clean_input_review("abc")


def test_evaluate_sales():
    metric = Metric(6000, 0, 0, 0)  # Pass strings as inputs
    assert "Great job! You've met your sales goal." in metric.evaluate_sales()

def test_evaluate_labor_costs():
    metric = Metric(10000, 2500, 0, 0)  # Pass strings as inputs
    assert "Labor costs are 25.00% of sales. Great job!" in metric.evaluate_labor_costs()

def test_evaluate_food_costs():
    metric = Metric(10000, 0, 2000, 0)  # Pass strings as inputs
    assert "Food costs are under control at 20.00% of sales." in metric.evaluate_food_costs()

def test_evaluate_reviews():
    metric = Metric(0, 0, 0, 4.9)  # Pass strings as inputs
    assert "Fantastic! Average rating is 4.9." in metric.evaluate_reviews()


def test_scorecard_str():
    scorecard = MetricScorecard(8500.0, 2344.0, 1233.0, 4.5)
    output = str(scorecard)
    assert "Metrics Scorecard" in output
    assert "Sales: $8500.00" in output
    assert "Labor Costs: $2344.00" in output
    assert "Food Costs: $1233.00" in output
    assert "Average Reviews: 4.5" in output

