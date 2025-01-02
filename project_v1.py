import re
import csv
from colorama import Fore, Style
from datetime import datetime

def main():
    # Introduction to user
    print("Welcome to the Restaurant Management Metrics Scorecard!")
    print("This tool helps you monitor key performance metrics such as weekly sales, labor costs, food costs, and customer reviews.")
    print("Based on your input, the scorecard will provide feedback and suggestions for improvement.")
    print("Let's begin by entering your weekly metrics.\n")

    # Ask for date
    date = input("Enter date (YYYY-MM-DD): ")

    # Gather input
    sales, labor_costs, food_costs, avg_reviews = get_float()

    # Functions
    compare_sales_to_target(sales)
    labor_percent = display_labor_costs(labor_costs, sales)
    food_percent = display_food_costs(food_costs, sales)
    display_reviews(avg_reviews)

    # Weekly review
    weekly_review(labor_percent, food_percent, avg_reviews)

    # Store data in CSV
    store_data_in_csv(date, sales, labor_costs, food_costs, avg_reviews)


def get_float():
    while True:
        try:
            sales = input("Enter weekly sales (e.g., $3,500.50): ")
            labor_costs = input("Enter weekly labor costs (e.g., $1,250.75): ")
            food_costs = input("Enter weekly food costs (e.g., $850.00): ")
            avg_reviews = input("Enter the average rating on Google, DoorDash, UberEats, and Grubhub (in decimal form): ")

            # Remove dollar signs and commas, then convert to float
            sales = clean_input(sales)
            labor_costs = clean_input(labor_costs)
            food_costs = clean_input(food_costs)
            avg_reviews = clean_input_review(avg_reviews)

            return sales, labor_costs, food_costs, avg_reviews
        except ValueError as e:
            print(f"Invalid input. Please ensure all fields are entered correctly: {e}")

def clean_input(value):
    # Remove dollar sign and commas, then convert to float
    value = value.replace('$', '').replace(',', '')
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Could not convert {value} to a number. Ensure no other characters are included.")

def clean_input_review(value):
    # Ensure average reviews are between 1 and 5
    try:
        value = float(value)
        if 1 <= value <= 5:
            return value
        else:
            raise ValueError("Review should be between 1 and 5.")
    except ValueError:
        raise ValueError("Average rating should be a decimal number between 1 and 5.")

def compare_sales_to_target(sales, target=5000):
    # Compares sales to a target and gives feedback
    difference = sales - target
    if difference >= 0:
        print(f"{Fore.GREEN}Great job! You've met your sales goal with ${difference} over target.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Sales are ${-difference} below the target. Consider strategies like running promotions or improving marketing.{Style.RESET_ALL}")
    return difference

def display_labor_costs(labor_costs, sales):
    # Calculates labor costs percentage, returns status, and provides suggestions
    labor_percent = (labor_costs / sales) * 100
    if labor_percent < 30:
        print(f"{Fore.GREEN}Labor costs are under control at {labor_percent:.2f}% of sales.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Labor costs are high at {labor_percent:.2f}%. Consider reducing overtime, adjusting shifts, or using more efficient scheduling.{Style.RESET_ALL}")
    return labor_percent

def display_food_costs(food_costs, sales):
    # Calculates food costs percentage, returns status, and provides suggestions
    food_percent = (food_costs / sales) * 100
    if food_percent < 25:
        print(f"{Fore.GREEN}Food costs are under control at {food_percent:.2f}% of sales.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Food costs are high at {food_percent:.2f}%. Consider reducing food waste, improving inventory tracking, or negotiating supplier prices.{Style.RESET_ALL}")
    return food_percent

def display_reviews(avg_reviews):
    # Displays feedback based on average review score and provides suggestions
    if avg_reviews >= 4.8:
        print(f"{Fore.GREEN}Fantastic! Your average 5-star rating is {avg_reviews}. Keep up the great service!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Your average rating is {avg_reviews}. To improve, consider gathering feedback, improving customer service, or enhancing product quality.{Style.RESET_ALL}")
    return avg_reviews

def weekly_review(labor_percent, food_percent, avg_reviews):
    # Evaluates Prime Costs (Labor + Food) and Reviews for weekly goals
    prime_costs = labor_percent + food_percent

    print("\n--- Weekly Review ---")

    # Evaluate Prime Costs
    if prime_costs <= 65:
        print(f"{Fore.GREEN}Your Prime Costs (Labor + Food) are {prime_costs:.2f}%, which is within the target of 65%. Excellent job managing your costs!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Your Prime Costs (Labor + Food) are {prime_costs:.2f}%, which exceeds the target of 65%. Focus on reducing labor and food costs to improve next week.{Style.RESET_ALL}")

    # Evaluate Reviews
    if avg_reviews >= 4.8:
        print(f"{Fore.GREEN}Your average 5-star rating is {avg_reviews}. Keep up the great customer service!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Your average 5-star rating is {avg_reviews}. Focus on customer service improvements, product quality, or gathering feedback for next week.{Style.RESET_ALL}")

    # Suggest improvement plan if goals are not met
    if prime_costs > 65 or avg_reviews < 4.8:
        print(f"{Fore.YELLOW}\nImprovement Plan for Next Week:\n- Analyze labor shifts and reduce overtime where possible.\n- Focus on reducing food waste and monitoring inventory closely.\n- Gather customer feedback and improve service quality to raise your reviews.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}\nYou're on track! Keep up the great work next week!{Style.RESET_ALL}")

def store_data_in_csv(date, sales, labor_costs, food_costs, avg_reviews):
    # Store the data in a CSV file
    try:
        with open('restaurant_metrics.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, sales, labor_costs, food_costs, avg_reviews])
        print(f"Your data for {date} has been saved to the CSV file.")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

if __name__ == "__main__":
    main()
