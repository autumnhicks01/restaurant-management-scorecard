# Restaurant Management Metrics Scorecard

## **Overview**
The Restaurant Management Metrics Scorecard is a Python-based tool designed to help restaurant managers and owners monitor key performance metrics. The tool evaluates weekly sales, labor costs, food costs, and customer reviews, providing feedback and suggestions for improvement. Additionally, the metrics are saved to a CSV file for future analysis, allowing users to track trends and predict performance.

This project was developed as part of a Harvard Python class (CS50P), demonstrating skills in object-oriented programming (OOP), data validation, error handling, and file operations. The project serves as a practical application of programming concepts learned in the course.

---

## **Features**
- **Metrics Evaluation**: Analyze sales, labor costs, food costs, and average reviews with feedback based on industry benchmarks.
- **Data Validation**: Ensures all inputs are cleaned and validated for accurate calculations.
- **Error Handling**: Identifies and handles user input errors gracefully using `try/except` blocks and `ValueError`.
- **File Storage**: Saves metrics to a CSV file, enabling further data analysis and trend tracking.
- **Object-Oriented Design**: Leverages Python’s OOP principles to encapsulate functionality into reusable and maintainable classes.

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
   - To address these issues, I refactored the project into a cleaner design with a base class (`Metric`) and a second class (`MetricScorecard`). This allowed me to centralize input validation and calculations in the base class while focusing on higher-level operations, like storing data and generating reports in the other class.
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

## **How to Use the Project**
1. Run the program:
   ```bash
   python project.py
2. Enter weekly metrics as prompted.
3. Review the evaluation and feedback.
4. Check the restaurant_metrics.csv file for stored data.









