import csv
from colorama import Fore as f
from colorama import Style as s
from datetime import datetime

def main():
    #user intro
    print("Welcome to the Restaurant Management Metrics Scorecard!")
    print("This tool helps you monitor key performance metrics such as weekly sales, labor costs, food costs, and customer reviews.")
    print("Based on your input, the scorecard will provide feedback and suggestions for improvement.")
    print("Let's begin by entering your weekly metrics.\n")
    try:
        #get input from user
        sales = get_input("Enter weekly sales: ", Metric.clean_input)
        labor_costs = get_input("Enter labor costs: ", Metric.clean_input)
        food_costs = get_input("Enter food costs: ", Metric.clean_input)
        avg_reviews = get_input("Enter average review score (1-5): ", Metric.clean_input_review)

        #create scorecard
        scorecard = MetricScorecard(sales, labor_costs, food_costs, avg_reviews)
        print(scorecard)
        scorecard.evaluate_metrics()
        scorecard.store_data()

        print("Thank you for using the Restaurant Management Scorecard!")
    except ValueError:
        print(f"bug1")
    except Exception:
        print(f"bug2")

def get_input(prompt, validation):
    #input validation
    while True:
        user_input = input(prompt)
        try:
            return validation(user_input)
        except ValueError:
            print("Input can not be empty. Please provide a value.")
class Metric:
    def __init__(self, sales, labor_costs, food_costs, avg_reviews):
        self._sales = sales
        self._labor_costs = labor_costs
        self._food_costs = food_costs
        self._avg_reviews = avg_reviews


    @property
    def sales(self):
        return self._sales
    @sales.setter
    def sales(self, value):
        self._sales = self.clean_input(value)

    @property
    def labor_costs(self):
        return self._labor_costs
    @labor_costs.setter
    def labor_costs(self, value):
        self._labor_costs = self.clean_input(value)

    @property
    def food_costs(self):
        return self._food_costs
    @food_costs.setter
    def food_costs(self, value):
        self._food_costs = self.clean_input(value)

    @property
    def avg_reviews(self):
        return self._avg_reviews
    @avg_reviews.setter
    def avg_reviews(self, value):
        self._avg_reviews = self.clean_input_review(value)
        
    @staticmethod
    def clean_input(value):
        if not value.strip():
            raise ValueError("Input can not be empty. Please provide a value")
        try:
            value = value.replace("$", "").replace(",", "")
            return float(value)
        except ValueError:
            raise ValueError("Input is not valid. Please provide a numeric value.")
    @staticmethod
    def clean_input_review(value):
        if not value.strip():
            raise ValueError("Input can not be empty. Please provide a value.")
        try:
            score = float(value)
            if 1 <= score <= 5:
                return score
            else:
                raise ValueError("Review score must be between 1 and 5")
        except ValueError:
            raise ValueError("Invalid review score.")
    def evaluate_sales(self, target=5000):
        difference = self.sales - target
        if difference >= 0:
            return f"{f.GREEN}Great job! You've met your sales goal.{s.RESET_ALL}"
        else:
            return f"{f.RED}Sales are ${-difference:.2f} below the sales goal. Run a promotion or increase marketing efforts.{s.RESET_ALL}"

    def evaluate_labor_costs(self):
        labor_percent = (self.labor_costs / self.sales) * 100
        if labor_percent <= 30:
            return f"{f.GREEN}Labor costs are {labor_percent:.2f}% of sales. Great job!{s.RESET_ALL}"
        else:
            return f"{f.RED}Labor costs are {labor_percent:.2f}% of sales. Optimize scheduling or reduce overtime.{s.RESET_ALL}"
    def evaluate_food_costs(self):
        food_percent = (self.food_costs / self.sales) * 100
        if food_percent < 25:
            return f"{f.GREEN}Food costs are under control at {food_percent:.2f}% of sales.{s.RESET_ALL}"
        else:
            return f"{f.RED}Food costs are high at {food_percent:.2f}% of sales. Reduce waste and negotiate better supplier prices.{s.RESET_ALL}"

    def evaluate_reviews(self):
        if self.avg_reviews >= 4.8:
            return f"{f.GREEN}Fantastic! Average rating is {self.avg_reviews}. Continue encouraging guests to leave reviews.{s.RESET_ALL}"
        else:
            return f"{f.RED}Average rating is below benchmark at {self.avg_reviews}. Gather feedback from customers to improve.{s.RESET_ALL}"

class MetricScorecard(Metric):
    def __init__(self, sales, labor_costs, food_costs, avg_reviews):
        Metric.__init__(self, sales, labor_costs, food_costs, avg_reviews)
        self.date = datetime.now().strftime("%Y-%m-%d")
    def __str__(self):
        return(

            f"\nMetrics Scorecard ({self.date}):\n"
            f"  Sales: ${self.sales:.2f}\n"
            f"  Labor Costs: ${self.labor_costs:.2f}\n"
            f"  Food Costs: ${self.food_costs:.2f}\n"
            f"  Average Reviews: {self.avg_reviews:.1f}\n"
        )
    def evaluate_metrics(self):
        print("\n--- Weekly Restaurant Metrics Evaluation ---")
        print(self.evaluate_sales())
        print(self.evaluate_labor_costs())
        print(self.evaluate_food_costs())
        print(self.evaluate_reviews())

    def store_data(self):
        try:
            with open("restaurant_metrics.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow([
                    self.date,
                    self.sales,
                    self.labor_costs,
                    self.food_costs,
                    self.avg_reviews
                ])
                print(f"\nData for {self.date} saved successfully to CSV file.")
        except Exception:
            raise Exception("Failed to save data.")

if __name__ == "__main__":
    main()

