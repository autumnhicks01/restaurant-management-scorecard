# Restaurant Management Scorecard

## **Welcome**
Welcome to the Restaurant Management Scorecard, a Python-based tool designed as my final project for Harvard's CS50P course. This application helps restaurant managers and owners monitor and manage key performance metrics, make data-driven decisions, and ensure operational success.

---

## **Features**
This application enables users to:
- **Input and Clean Key Weekly Metrics**:
  - Weekly Sales
  - Labor Costs
  - Food Costs
  - Customer Reviews
- **Analyze and Compare Metrics**:
  - Compare inputs against industry standards and receive actionable recommendations for improvement.
- **Perform Key Calculations**:
  - Labor Costs as a Percentage of Sales
  - Food Costs as a Percentage of Sales
  - Prime Costs (Labor + Food)
- **Save and Track Data**:
  - Save weekly metrics to a CSV file for future comparisons and projections.
- **Receive Feedback and Suggestions**:
  - Targeted recommendations to improve operational efficiency and customer satisfaction.

---

## **Installation**
1. Clone or download this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required packages:
   - `colorama`

---

## **Usage**
1. Run the script `restaurant_scorecard.py`.
2. Follow the prompts to input:
   - **Weekly Sales**: Enter your weekly sales in a format like `$3,500.50`.
   - **Labor Costs**: Enter your weekly labor costs in a format like `$1,250.75`.
   - **Food Costs**: Enter your weekly food costs in a format like `$850.00`.
   - **Average Customer Review Rating**: Enter your average rating (on a scale of 1.0 to 5.0).

3. **Receive**:
   - A detailed analysis of your metrics, including:
     - Comparisons of your sales to target values.
     - Labor costs and food costs as percentages of sales.
     - Feedback on customer reviews.
   - Recommendations for improving sales, managing costs, and enhancing customer satisfaction.

4. The input data will be automatically saved to `restaurant_metrics.csv` for historical tracking and future projections.

---

## **Lessons Learned**

### **Versioning and Project Evolution**
This project went through several iterations as I learned more about programming concepts, particularly object-oriented programming (OOP). Below is a summary of the journey:

1. **Initial Version: Function-Based Design**
   - The first version of the project was implemented using multiple standalone functions to handle different aspects, such as data input, validation, and calculations. While this approach worked for smaller tasks, the code quickly became repetitive and difficult to scale.
   - For example, sales data had to be passed manually between multiple functions, and any changes to the logic required updates across several parts of the code. Although functional, it was inefficient and error-prone.

2. **Transition to OOP: Initial Attempts**
   - After learning about OOP concepts, I decided to rewrite the project to encapsulate functionality into classes. Initially, I tried to create a single class (`Metric`) with getter and setter methods for each metric (sales, labor costs, etc.). However, this approach resulted in a fragmented design where similar logic was unnecessarily repeated across multiple methods and properties.
   - Understanding the role of `self` and the use of underscores for private attributes was challenging at first. I ended up copying code multiple times, especially for handling sales data. This version worked but was still overly complex and not scalable.

3. **Refined OOP: Multiple Classes with Inheritance**
   - To address these issues, I refactored the project into a cleaner design with a base class (`Metric`) and a derived class (`MetricScorecard`). This allowed me to centralize input validation and calculations in the base class while focusing on higher-level operations, like storing data and generating reports, in the derived class.
   - By applying inheritance, I reduced code duplication and improved the organization of the program. This version marked a breakthrough in understanding OOP concepts and implementing a more maintainable structure.

4. **Final Version: Polished and Simplified**
   - The final version streamlined the code further, ensuring that repetitive logic was abstracted into reusable methods and properties. I leveraged setters and getters effectively, ensuring consistent data validation.
   - Error handling was also refined, using `try/except` blocks and `ValueError` to catch and address invalid inputs. This made debugging much easier and improved the program's overall robustness.

### **Key Takeaways**

#### **Object-Oriented Programming**
- OOP transformed the way I approached this project. Initially, the concepts of `self`, private attributes, and encapsulation were challenging, but they eventually became intuitive after working on a few class projects.
- Using inheritance and reusable methods drastically reduced code duplication and made the program easier to maintain and extend.

#### **Avoiding Repetition**
- A major lesson was realizing that if I was copying code, there was likely a more efficient way to implement the functionality. This helped me focus on simplifying the logic and improving the overall structure.

#### **Error Handling**
- Debugging became a systematic process by raising specific exceptions and narrowing down issues using `try/except` blocks. This approach saved significant time and helped identify and resolve bugs effectively.

#### **Iterative Development**
- Iterative development was key to improving the project. Each version built upon the previous one, incorporating new concepts and techniques as I learned them. This iterative process reinforced the value of continuous improvement and refactoring.

---

## **Project Workflow**

### **Step 1: Data Input**
Users are prompted to input weekly sales, labor costs, food costs, and the average review score. Inputs are validated and cleaned using static methods (`clean_input` and `clean_input_review`) to ensure accurate calculations.

### **Step 2: Metrics Evaluation**
- **Sales**: Compared against a default target ($5000).
- **Labor Costs**: Evaluated as a percentage of sales (target: ≤ 30%).
- **Food Costs**: Evaluated as a percentage of sales (target: ≤ 25%).
- **Reviews**: Benchmarked against an ideal average score (≥ 4.8).

### **Step 3: Feedback and Suggestions**
For each metric, the program provides detailed feedback, highlighting achievements or areas for improvement.

### **Step 4: Data Storage**
Metrics are saved to a CSV file with a timestamp, enabling users to analyze performance trends over time.

---

## **Technical Concepts Demonstrated**
- **Object-Oriented Programming**: The program uses inheritance, property setters/getters, and private attributes for encapsulation and clean design.
- **Error Handling**: Comprehensive `try/except` blocks and custom exception raising make the program resilient to invalid inputs.
- **Data Cleaning**: Input sanitization ensures robust handling of real-world data, including removing special characters and validating numeric ranges.
- **File I/O**: Data is stored in CSV format, demonstrating practical file operations.

---

## **What I Learned**
1. **Efficiency in Code**:
   - Repeating code is a sign of inefficiency. This lesson was reinforced when refactoring the initial procedural version to use OOP principles.
   - Simplifying code through reusable methods made debugging and extending functionality easier.

2. **Mastering OOP Syntax**:
   - Concepts like `self`, underscores, and encapsulation initially felt complex but became second nature after iterative practice.
   - OOP improved the organization of the code, making it easier to follow and extend.

3. **Error Handling is Critical**:
   - Identifying errors using `ValueError` and `try/except` blocks saved significant debugging time.
   - Debugging became a methodical process rather than trial and error.

4. **Practical Data Validation**:
   - Cleaning user inputs (e.g., removing `$` and ensuring valid scores) is critical for real-world applications.
   - Using lessons from the class problem sets helped implement practical solutions for input validation.

---









