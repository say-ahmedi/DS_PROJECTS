# Unit 1: Analyzing Categorical Data - Foundations of EDA

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

I created this set of exercises to **bridge the gap between math theory and Python programming**. By completing these tasks, I am building the foundational skills needed for **Exploratory Data Analysis (EDA)**. Specifically for my Credit Risk & Antifraud Capstone project, I need to know how to group data by categories (e.g., "Fraud" vs "Not Fraud", or "Local" vs "International") to find patterns and calculate baseline probabilities.

---

## 📁 Files and Project Tasks

### File 1: `01_categorical_variables_and_visuals.ipynb`

**Objective:** Translate basic categorical data into Python data structures and visualize it.

* **Task 1: Data Representation**
  * *Instructions:* Create a Python dictionary representing a mini-dataset of 5 credit card transactions. The keys should be `Transaction_ID`, `Merchant_Type` (e.g., Groceries, Electronics, Travel), and `Is_Fraud` (Yes/No).
  * *Acceptance Criteria:* The dictionary is successfully created and can be printed in a readable format.
* **Task 2: Bar Chart Visualization**
  * *Instructions:* Count the frequency of each `Merchant_Type` in your dataset. Use `matplotlib.pyplot` to create a bar chart showing the count of each category.
  * *Acceptance Criteria:* A bar chart renders successfully with an X-axis (Merchant Types), a Y-axis (Counts), and a title.

---

### File 2: `02_two_way_frequency_tables.ipynb`

**Objective:** Build contingency tables in Python to analyze the relationship between two categorical variables.

* **Task 1: Generate Synthetic Data**
  * *Instructions:* Use Python's `random` module to generate a dataset of 1,000 transactions. Assign a category for `Transaction_Location` (90% 'Local', 10% 'International'). Assign `Is_Fraud` ('Yes' or 'No'), but make it so that 'International' transactions have a higher chance of being 'Yes'.
  * *Acceptance Criteria:* A list or dictionary containing 1,000 paired records of (Location, Fraud Status).
* **Task 2: Build the Frequency Table**
  * *Instructions:* Write a Python script (using loops or the `pandas.crosstab` function) to count the occurrences and build a 2x2 Two-Way Frequency Table. Rows = Location, Columns = Fraud Status.
  * *Acceptance Criteria:* The table outputs a 2x2 matrix with the total counts for each group (e.g., Local/Yes, Local/No, International/Yes, International/No).
* **Task 3: Relative Frequency Table**
  * *Instructions:* Convert your absolute counts into percentages of the grand total (divide each cell by 1,000).
  * *Acceptance Criteria:* The four cells of the new table sum up to exactly `1.0` (or `100%`).

---

### File 3: `03_marginal_and_conditional_distributions.ipynb`

**Objective:** Use the two-way table from File 2 to calculate Marginal and Conditional probabilities.

* **Task 1: Marginal Distributions**
  * *Instructions:* Using your frequency table from File 2, write code to calculate the marginal distribution for `Is_Fraud`. (i.e., What is the total percentage of Fraud vs. No Fraud in the entire dataset regardless of location?).
  * *Acceptance Criteria:* Two percentages are printed that sum to 100%.
* **Task 2: Conditional Distribution (The Capstone Logic)**
  * *Instructions:* Write a Python function called `probability_fraud_given_location(location)`. This function should filter the dataset for the given location and calculate the percentage of those specific transactions that are fraud.
  * *Acceptance Criteria:* When you call `probability_fraud_given_location('International')`, the returned percentage must be significantly higher than when you call `probability_fraud_given_location('Local')`.

---

## 📝 Capstone Connection

By completing File 3, Task 2, I have essentially built a baseline rule-based Antifraud engine! In Data Science, before building complex Machine Learning models, we calculate conditional probabilities to establish baseline risks. If the conditional probability of fraud given an "International" transaction is 5%, and the base rate (marginal probability) of fraud is only 1%, we have mathematically proven that location is a useful feature for predicting fraud.
