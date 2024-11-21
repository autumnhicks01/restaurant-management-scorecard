import re
import csv
from colorama import Fore, Style
from datetime import datetime

def main():
    print("Welcome to the Restaurant Management Metrics Scorecard!")
    print("This tool helps you monitor key performance metrics such as weekly sales, labor costs, food costs, and customer reviews.")
    print("Let's begin by entering your weekly metrics.\n")

    # Step 1: Collect date input
    date = input("Enter date (YYYY-MM-DD): ")

    # Step 2: Collect metrics input
    try:
        sales = input("Enter weekly sales (e.g., $3,500.50): ")
        labor_costs = input("Enter weekly labor costs (e.g., $1,250.75): ")
        food_costs = input("Enter weekly food costs (e.g., $850.00): ")
        avg_reviews = input("Enter the average rating (1-5): ")

        # Step 3: Instantiate MetricsScorecard
        metrics = MetricsScorecard(date, sales, labor_costs, food_costs, avg_reviews)

        # Step 4: Evaluate metrics
        print("\n--- Metrics Evaluation ---")
        metrics.evaluate_metrics()

        # Step 5: Store the results in a CSV file
        metrics.store_data()
        print("\nThank you for using the Restaurant Management Metrics Scorecard!")
    except ValueError as e:
        print(f"Error: {e}. Please restart and enter the correct values.")


class Metric:
    @staticmethod
    def clean_input(value):
        """Remove dollar signs and commas, then convert to float."""
        value = value.replace('$', '').replace(',', '')
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Invalid input: {value}. Please enter a numeric value.")

    @staticmethod
    def clean_input_review(value):
        """Ensure average reviews are between 1 and 5."""
        try:
            value = float(value)
            if 1 <= value <= 5:
                return value
            else:
                raise ValueError("Review must be between 1 and 5.")
        except ValueError:
            raise ValueError("Invalid review input. Must be a decimal between 1 and 5.")
class SalesMetrics(Metric):
    def __init__(self, sales):
        self._sales = None
        self.sales = sales  # Use the setter for validation

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        self._sales = self.clean_input(value)

    def compare_to_target(self, target=5000):
        difference = self._sales - target
        if difference >= 0:
            print(f"{Fore.GREEN}Great job! You've met your sales goal with ${difference:.2f} over target.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Sales are ${-difference:.2f} below the target. Improve marketing or run promotions.{Style.RESET_ALL}")
        return difference
class LaborMetrics(Metric):
    def __init__(self, labor_costs, sales):
        self._labor_costs = None
        self._sales = None
        self.labor_costs = labor_costs  # Use the setter for validation
        self.sales = sales  # Use the setter for validation

    @property
    def labor_costs(self):
        return self._labor_costs

    @labor_costs.setter
    def labor_costs(self, value):
        self._labor_costs = self.clean_input(value)

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        self._sales = self.clean_input(value)

    def calculate_percent(self):
        return (self._labor_costs / self._sales) * 100

    def evaluate(self):
        labor_percent = self.calculate_percent()
        if labor_percent < 30:
            print(f"{Fore.GREEN}Labor costs are under control at {labor_percent:.2f}% of sales.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Labor costs are high at {labor_percent:.2f}%. Reduce overtime and optimize shifts.{Style.RESET_ALL}")
        return labor_percent
class FoodMetrics(Metric):
    def __init__(self, food_costs, sales):
        self._food_costs = None
        self._sales = None
        self.food_costs = food_costs  # Use the setter for validation
        self.sales = sales  # Use the setter for validation

    @property
    def food_costs(self):
        return self._food_costs

    @food_costs.setter
    def food_costs(self, value):
        self._food_costs = self.clean_input(value)

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        self._sales = self.clean_input(value)

    def calculate_percent(self):
        return (self._food_costs / self._sales) * 100

    def evaluate(self):
        food_percent = self.calculate_percent()
        if food_percent < 25:
            print(f"{Fore.GREEN}Food costs are under control at {food_percent:.2f}% of sales.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Food costs are high at {food_percent:.2f}%. Reduce waste and negotiate better supplier prices.{Style.RESET_ALL}")
        return food_percent
class ReviewMetrics(Metric):
    def __init__(self, avg_reviews):
        self._avg_reviews = None
        self.avg_reviews = avg_reviews  # Use the setter for validation

    @property
    def avg_reviews(self):
        return self._avg_reviews

    @avg_reviews.setter
    def avg_reviews(self, value):
        self._avg_reviews = self.clean_input_review(value)

    def evaluate(self):
        if self._avg_reviews >= 4.8:
            print(f"{Fore.GREEN}Fantastic! Average rating is {self._avg_reviews}. Keep it up!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Average rating is {self._avg_reviews}. Gather feedback to improve.{Style.RESET_ALL}")
        return self._avg_reviews
class MetricsScorecard:
    def __init__(self, date, sales, labor_costs, food_costs, avg_reviews):
        self.date = date
        self.sales_metric = SalesMetrics(sales)
        self.labor_metric = LaborMetrics(labor_costs, sales)
        self.food_metric = FoodMetrics(food_costs, sales)
        self.review_metric = ReviewMetrics(avg_reviews)

    def evaluate_metrics(self):
        print("\n--- Metrics Evaluation ---")
        self.sales_metric.compare_to_target()
        labor_percent = self.labor_metric.evaluate()
        food_percent = self.food_metric.evaluate()
        self.review_metric.evaluate()

        # Evaluate Prime Costs
        prime_costs = labor_percent + food_percent
        if prime_costs <= 65:
            print(f"{Fore.GREEN}Prime Costs (Labor + Food) are {prime_costs:.2f}%, within the target of 65%. Excellent!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Prime Costs (Labor + Food) are {prime_costs:.2f}%, exceeding the target. Focus on cost reduction.{Style.RESET_ALL}")

    def store_data(self):
        try:
            with open('restaurant_metrics.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.date, self.sales_metric.sales, self.labor_metric.labor_costs, self.food_metric.food_costs, self.review_metric.avg_reviews])
            print(f"Data for {self.date} saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

if __name__ == "__main__":
    main()
