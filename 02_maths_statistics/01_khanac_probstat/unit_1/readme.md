### #Unit 1: Analyzing Categorical Data - Foundations of EDA

## 📖 What this unit consists of

This unit covers the fundamentals of dealing with categorical data (data that represents groups or categories, rather than numbers). It includes:

* Identifying individuals, variables, and categorical vs. quantitative data.
* Creating and reading bar graphs, pie charts, and picture graphs.
* Building **Two-way frequency tables** (contingency tables) to compare two categorical variables.
* Calculating **Marginal distributions** (totals for rows/columns).
* Calculating **Conditional distributions** (probability of A, given B).
* Identifying trends and associations between categories.

## 🎯 Why I created this (Purpose)

I have mastered the theory of this unit on Khan Academy (100% mastery). However, in the real world of Data Science and Data Engineering, I will not be reading pictographs or drawing tables by hand. I will be writing Python code to process millions of rows of categorical data.

I created this set of exercises to **bridge the gap between math theory and Python programming**. To ensure I learn properly, I will first complete a **Universal Task** using simple, everyday examples to grasp the Python logic. Then, I will complete a **Capstone Task** to apply that exact same logic to my Credit Risk & Antifraud project.

---

## 📁 Files and Project Tasks

### File 1: `01_categorical_variables_and_visuals.ipynb`

**Objective:** Translate basic categorical data into Python data structures and visualize it.

* **Task 1: Universal (The Basics)**
  * *Instructions:* Create a Python dictionary representing a survey of 5 people. Keys should be `Name`, `Favorite_Fruit` (e.g., Apple, Banana, Orange), and `Is_Student` (Yes/No). Count the frequency of each fruit and plot a bar chart.
  * *Acceptance Criteria:* A bar chart renders successfully showing the count of each fruit.
* **Task 2: Capstone (Antifraud Application)**
  * *Instructions:* Create a Python dictionary representing 5 credit card transactions. Keys should be `Transaction_ID`, `Merchant_Type` (e.g., Groceries, Electronics, Travel), and `Is_Fraud` (Yes/No). Count the frequency of each `Merchant_Type` and plot a bar chart.
  * *Acceptance Criteria:* A bar chart renders successfully with an X-axis (Merchant Types), a Y-axis (Counts), and a title.

---

### File 2: `02_two_way_frequency_tables.ipynb`

**Objective:** Build contingency tables in Python to analyze the relationship between two categorical variables.

* **Task 1: Universal (The Basics)**
  * *Instructions:* Use Python to generate a synthetic dataset of 100 people. Assign `Gender` (Male/Female) and `Pet_Owner` (Yes/No). Make it so females are slightly more likely to own pets. Build a 2x2 Two-Way Frequency Table using loops or `pandas.crosstab`.
  * *Acceptance Criteria:* A 2x2 matrix prints out showing the counts (Male/Yes, Male/No, Female/Yes, Female/No).
* **Task 2: Capstone (Antifraud Application)**
  * *Instructions:* Generate a dataset of 1,000 transactions. Assign `Transaction_Location` (90% 'Local', 10% 'International'). Assign `Is_Fraud` ('Yes' or 'No'), but make it so 'International' transactions have a higher chance of being 'Yes'. Build the 2x2 frequency table.
  * *Acceptance Criteria:* The table outputs a 2x2 matrix with the total counts for each group. Convert these absolute counts into a Relative Frequency Table (percentages of the grand total). The four cells must sum to exactly `1.0` (or `100%`).

---

### File 3: `03_marginal_and_conditional_distributions.ipynb`

**Objective:** Use the two-way tables from File 2 to calculate Marginal and Conditional probabilities.

* **Task 1: Universal (The Basics)**
  * *Instructions:* Using your Pet_Owner dataset from File 2, calculate the marginal distribution for `Pet_Owner` (What % of people own pets overall?). Then, write a function `probability_pet_given_gender(gender)` that calculates the conditional probability of owning a pet given a specific gender.
  * *Acceptance Criteria:* Marginal percentages sum to 100%. The conditional probability function correctly filters the data and returns a percentage.
* **Task 2: Capstone (The Antifraud Logic)**
  * *Instructions:* Using your Credit Card dataset from File 2, calculate the marginal distribution for `Is_Fraud` (the base rate of fraud). Then, write a Python function called `probability_fraud_given_location(location)` that filters the dataset for the given location and calculates the fraud percentage for that specific group.
  * *Acceptance Criteria:* When you call `probability_fraud_given_location('International')`, the returned percentage must be significantly higher than the base rate (marginal probability) of fraud.

---

## 📝 Capstone Connection

By completing File 3, Task 2, I have essentially built a baseline rule-based Antifraud engine! In Data Science, before building complex Machine Learning models, we calculate conditional probabilities to establish baseline risks. If the conditional probability of fraud given an "International" transaction is 5%, and the base rate (marginal probability) of fraud is only 1%, I have mathematically proven that location is a useful feature for predicting fraud.
