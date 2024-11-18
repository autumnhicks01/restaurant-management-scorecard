# Restaurant Management Scorecard

Welcome to the **Restaurant Management Scorecard**, a Python-based tool designed as my final project for the CS50P course. This application helps restaurant managers and owners monitor and manage key performance metrics, make data-driven decisions, and ensure operational success.

---

## Features

This application enables users to:

- Input and clean key weekly metrics, such as:
  - **Weekly Sales**
  - **Labor Costs**
  - **Food Costs**
  - **Customer Reviews**
- Compare inputs against industry standards and receive actionable recommendations for improvement.
- Calculate:
  - **Labor Costs as a Percentage of Sales**
  - **Food Costs as a Percentage of Sales**
  - **Prime Costs (Labor + Food)**
- Save weekly metrics to a CSV file for future comparisons and projections.
- Receive a summary of results, including targeted feedback and suggestions for improvement.

---

## Installation

1. Clone or download this repository to your local machine.
2. Ensure you have Python installed 
3. Install the required packages using pip:
   ```bash
   pip install colorama
   


## Usage
1. Run the script:
      ```bash
   python restaurant_scorecard.py

Follow the prompts to input:

- **Weekly Sales:** Enter your weekly sales in a format like $3,500.50.
- **Labor Costs:** Enter your weekly labor costs in a format like $1,250.75.
- **Food Costs:** Enter your weekly food costs in a format like $850.00.
- **Average Customer Review Rating:** Enter your average rating (on a scale of 1.0 to 5.0).

Receive:

- A detailed analysis of your metrics, such as:
- Comparisons of your sales to target values.
- Labor costs and food costs as percentages of sales.
- Feedback on customer reviews.
- Recommendations for improving sales, managing costs, and enhancing customer satisfaction.

The input data will be automatically saved to restaurant_metrics.csv for historical tracking and future projections.








