# Unit 1: Analyzing Categorical Data - Foundations of EDA

## 📖 What this unit consists of

This unit covers the fundamentals of dealing with categorical data (data that represents groups or categories, rather than numbers). It includes:

* Identifying individuals, variables, and categorical vs. quantitative data.
* Creating and reading bar graphs, pie charts, and picture graphs.
* Using **Venn Diagrams** and Set logic to find overlaps between groups.
* Building **Two-way frequency tables** (contingency tables) to compare two categorical variables.
* Calculating **Marginal distributions** (totals for rows/columns).
* Calculating **Conditional distributions** (probability of A, given B).
* Identifying trends, associations, and **independence** between categories.

## 🎯 Why I created this (Purpose)

I have mastered the theory of this unit on Khan Academy (100% mastery). However, in the real world of Data Science and Data Engineering, I will not be reading pictographs or drawing tables by hand. I will be writing Python code to process millions of rows of categorical data.

I created this set of exercises to **bridge the gap between math theory and Python programming**. To ensure I learn properly, I will first complete a **Universal Task** using simple, everyday examples to grasp the Python logic. Then, I will complete a **Capstone Task** to apply that exact same logic to my Credit Risk & Antifraud project.

---

## 📁 Files and Project Tasks

### File 1: `01_categorical_variables_and_set_logic.ipynb`

**Objective:** Translate basic categorical data into Python data structures, visualize it, and use Set logic (Venn Diagrams concept).

* **Task 1: Universal (The Basics)**
  * *Instructions:* Create a Python dictionary representing a survey of 5 people. Keys: `Name`, `Favorite_Fruit`, `Is_Student`. Count the frequency of each fruit and plot a bar chart.
  * *Acceptance Criteria:* A bar chart renders successfully showing the count of each fruit.
* **Task 2: Universal (Set Logic / Venn Diagrams)**
  * *Instructions:* Create two lists: `math_students` and `science_students`. Use Python `set` operations (`intersection`, `union`, `difference`) to find: 1) Students taking both, 2) Students taking at least one, 3) Students taking *only* math.
  * *Acceptance Criteria:* The script successfully prints the three distinct lists using set operators (`&`, `|`, `-`).
* **Task 3: Capstone (Antifraud Application)**
  * *Instructions:* Create a dictionary representing 5 credit card transactions. Keys: `Transaction_ID`, `Merchant_Type`, `Is_Fraud`. Count the frequency of each `Merchant_Type` and plot a bar chart. Then, create two sets: `high_value_transactions` and `international_transactions`. Use set logic to find transactions that are BOTH high value AND international.
  * *Acceptance Criteria:* A bar chart renders successfully. The set logic correctly identifies the overlap.

---

### File 2: `02_two_way_frequency_tables.ipynb`

**Objective:** Build contingency tables in Python and visualize the relationship between two categorical variables.

* **Task 1: Universal (The Basics)**
  * *Instructions:* Generate a synthetic dataset of 100 people. Assign `Gender` and `Pet_Owner`. Make females slightly more likely to own pets. Build a 2x2 Two-Way Frequency Table using loops or `pandas.crosstab`.
  * *Acceptance Criteria:* A 2x2 matrix prints out showing the counts (Male/Yes, Male/No, Female/Yes, Female/No). Convert to Relative Frequency (percentages summing to 100%).
* **Task 2: Capstone (Antifraud Application)**
  * *Instructions:* Generate a dataset of 1,000 transactions. `Transaction_Location` (90% Local, 10% Int). `Is_Fraud` (Yes/No), with Int having higher fraud risk. Build the 2x2 frequency table.
  * *Acceptance Criteria:* The table outputs a 2x2 matrix with total counts. Convert to Relative Frequency Table (sums to 1.0).
* **Task 3: Hidden Concept (Visualizing Relationships)**
  * *Instructions:* Using the Antifraud table from Task 2, create a **Stacked Bar Chart** using `pandas.DataFrame.plot(kind='bar', stacked=True)`. The X-axis is Location, the bars are stacked with Fraud vs No Fraud proportions.
  * *Acceptance Criteria:* A stacked bar chart renders. You must normalize the data so the bars represent 100% proportions, allowing you to visually compare the fraud rate between Local and International.


---

### File 3: `03_marginal_conditional_and_independence.ipynb`

**Objective:** Use two-way tables to calculate probabilities and statistically test if variables are independent.

* **Task 1: Universal (The Basics)**
  * *Instructions:* Using your Pet_Owner dataset, calculate the marginal distribution for `Pet_Owner`. Write a function `probability_pet_given_gender(gender)` to calculate the conditional probability.
  * *Acceptance Criteria:* Marginal percentages sum to 100%. The function correctly filters data and returns a percentage.
* **Task 2: Capstone (Antifraud Logic)**
  * *Instructions:* Using your Credit Card dataset, calculate the marginal distribution for `Is_Fraud` (base rate). Write a function `probability_fraud_given_location(location)`.
  * *Acceptance Criteria:* `probability_fraud_given_location('International')` returns a percentage significantly higher than the base rate.
* **Task 3: Hidden Concept (Testing for Independence)**
  * *Instructions:* Two variables are **independent** if P(A|B) = P(A). Write a Python function `check_independence(dataset, var1, var2)` that calculates the marginal probability of var1, and the conditional probability of var1 given var2. Print whether they are "Independent" or "Associated".
  * *Acceptance Criteria:* When you run `check_independence` on Gender vs Pet_Owner (if you made the probabilities identical), it prints "Independent". When you run it on Location vs Fraud, it prints "Associated".
* **Task 4: Capstone (Product Analytics - Feature Adoption)**
  * *Context:* Before building a Machine Learning model to predict user churn, a Product Analyst needs to verify if a user's subscription tier affects their likelihood of adopting a new UI feature.
  * *Instructions:* Generate a synthetic dataset of 1,000 users. Assign `Subscription_Tier` (20% 'Premium', 80% 'Free'). Assign `Adopted_New_Feature` ('Yes' or 'No'), but bias the data so 'Premium' users are 3x more likely to adopt the feature than 'Free' users. Build a two-way table. Use your `check_independence` function to evaluate if `Subscription_Tier` and `Adopted_New_Feature` are associated.
  * *Acceptance Criteria:* The script generates the biased dataset, builds the frequency table, and correctly prints "Associated" (because the conditional probability of adopting the feature given Premium status will be significantly higher than the marginal probability of adopting the feature overall). This proves to the ML team that `Subscription_Tier` is a valid categorical feature to include in their churn prediction model.

By completing File 3, Task 3, you are doing exactly what Machine Learning models do under the hood! Before building a complex neural network, a Data Scientist checks for independence. If `P(Fraud | International) == P(Fraud)`, then location gives you zero new information, and the AI model won't use it. By proving they are *associated*, you have mathematically justified why your Capstone model should use "Transaction Location" as a feature to predict fraud.
