
# 📊 Unit 2 Applied: Displaying & Comparing Quantitative Data in Python for ML

Here is the analytical curriculum designed to bridge your Khan Academy statistical theory with Machine Learning workflows. As requested, no Python code is provided—you are the coder here!

---

## 📝 PART 1: Hands-On Tasks

### 🧪 Task 1: Frequency Tables & Dot Plots — Discretizing Continuous Features

**Title & Scenario:** You are working for an e-commerce platform and want to understand the distribution of customer purchase amounts. Because purchase amounts are continuous, you need to discretize them into meaningful bins to understand common spending tiers.
**Learning Objectives:** Building frequency tables from raw continuous data, creating dot plots to visualize discrete counts, and understanding the trade-off between bin granularity and information loss.
**ML Connection:** Many ML models (like Naive Bayes or Decision Trees) sometimes benefit from *binned* (discretized) features rather than raw continuous ones. Frequency tables are the first step in deciding bin boundaries for feature engineering.
**Step-by-Step Analytical Instructions:**

1. Load the Titanic dataset using Seaborn and drop rows with missing 'fare' values.
2. Round the 'fare' column to the nearest integer to create discrete observations.
3. Build a frequency table using Pandas that counts the occurrences of each rounded fare value, sorted by the fare amount.
4. Create a dot plot manually using Matplotlib. For each unique fare value in your frequency table, plot a stack of dots vertically. The x-axis is the fare value, the y-axis is the frequency (count).
5. Repeat the process, but this time group the fares into bins of width 10 (e.g., 0-10, 11-20). Compare the visual readability of the two plots.
   **Expected Output/Visualization:** A printed frequency table showing fare values and their counts, followed by a dot plot with dots stacked vertically at various x-coordinates. The second plot will look much less cluttered.
   **Key Takeaway:** Dot plots preserve every observation's identity, but they don't scale well to large datasets. Binning (discretizing) is a necessary compromise for both visualization and feature engineering.

---

### 🧪 Task 2: Histograms & Shapes of Distributions

**Title & Scenario:** You are analyzing the physical measurements of different flower species to build a classifier. You need to understand the underlying shape of your features to see if they follow a normal distribution or if they require transformation.
**Learning Objectives:** Creating histograms with multiple bin sizes, identifying distribution shapes (symmetric, right-skewed, left-skewed, bimodal), and calculating skewness.
**ML Connection:** Many ML algorithms (Linear/Logistic Regression, K-Means) assume features are roughly symmetric. Detecting skew guides whether you should apply log or Box-Cox transforms during your preprocessing pipeline.
**Step-by-Step Analytical Instructions:**

1. Load the Iris dataset using Seaborn.
2. Using Matplotlib, plot a 2x2 grid of histograms for all 4 numeric features (sepal_length, sepal_width, petal_length, petal_width). Use 10 bins for each.
3. Focus on the 'petal_length' column. Create a single figure with three overlapping histograms for this feature, using 5, 15, and 30 bins respectively. Use different colors and transparency so they overlay clearly.
4. Visually classify the shape of 'petal_length'. Is it symmetric, skewed, or bimodal?
5. Programmatically calculate and print the skewness score for all 4 features using Pandas.
   **Expected Output/Visualization:** A 2x2 grid of histograms. A single overlay plot showing three different bin configurations for petal length. A printed text output of 4 skewness numbers.
   **Key Takeaway:** Histograms reveal **shape**, but shape depends heavily on bin choice. The 'petal_length' feature is **bimodal**—a signal that the data contains distinct sub-populations (different species), which is highly informative for clustering tasks.

---

### 🧪 Task 3: Stem-and-Leaf Plots — Compact Textual Summaries

**Title & Scenario:** You are SSH'd into a remote server debugging a data pipeline. You don't have access to a graphical interface, but you need a quick summary of a sensor's latency readings to ensure the data isn't corrupted.
**Learning Objectives:** Implementing a stem-and-leaf plot from scratch, and reading off quantiles, modes, and spread from a purely textual representation.
**ML Connection:** In real-world ML engineering, you often debug data in terminal-only environments. Building custom textual summaries is a vital skill when you can't rely on Jupyter notebooks and GUI plots.
**Step-by-Step Analytical Instructions:**

1. Load the Iris dataset and select the 'sepal_width' column.
2. Multiply the values by 10 and round them to the nearest integer to remove decimals.
3. Write a custom function (using standard Python loops/dictionaries, no built-in stem-leaf library exists) to split each value into a "stem" (the tens digit) and a "leaf" (the ones digit).
4. Group the leaves by their stems, sort the leaves in ascending order, and print them in the standard `stem | leaf leaf leaf` text format.
5. Look at your printed text and manually identify the modal class (the stem with the most leaves) and approximate the median.
   **Expected Output/Visualization:** A purely text-based console output looking something like:
   ` 2 | 234`
   ` 3 | 0112334`
   ` 4 | 012`
   **Key Takeaway:** Stem-and-leaf plots preserve every data point *and* show the distribution shape, making them the perfect quick-look tool for terminal-based data validation.

---

### 🧪 Task 4: Clusters, Gaps, Peaks & Outliers — The 4-Feature Diagnosis

**Title & Scenario:** You are preparing data for a K-Means clustering model. K-Means is highly sensitive to outliers because it uses mean calculations. You need to visually and statistically identify anomalies and gaps in your data before feeding it to the model.
**Learning Objectives:** Visually detecting clusters (multimodality), gaps, peaks, and outliers. Using box plots and implementing IQR (Interquartile Range) outlier detection.
**ML Connection:** Outliers distort mean-based models. Detecting them visually *first*—before applying statistical filters—prevents blindly deleting meaningful data. Gaps often signal missing sub-populations in your training data.
**Step-by-Step Analytical Instructions:**

1. Load the Iris dataset.
2. Plot a histogram of 'petal_length' with 20 bins. Visually identify the large gap (an area on the x-axis with zero or very few observations). Use Matplotlib to highlight this gap region with a shaded background color.
3. Create a boxplot of all 4 features using Seaborn. Note which features show black outlier dots outside the "whiskers".
4. Focus on 'sepal_width'. Calculate Q1 (25th percentile) and Q3 (75th percentile). Compute the IQR (Q3 - Q1).
5. Calculate the lower bound (Q1 - 1.5 * IQR) and upper bound (Q3 + 1.5 * IQR).
6. Filter your DataFrame to find and print the rows where 'sepal_width' falls outside these bounds.
   **Expected Output/Visualization:** A histogram with a clearly shaded gap. A boxplot showing outlier dots. A printed DataFrame containing only the statistical outlier rows.
   **Key Takeaway:** Visual + statistical outlier detection must be paired. The gap in 'petal_length' isn't an error—it's a biological fact (setosa vs. others). Not all outliers are noise; some are natural signal.

---

### 🧪 Task 5: Comparing Distributions & Misleading Graphs

**Title & Scenario:** You are evaluating whether a specific feature is useful for predicting a target variable. You also need to present your findings to stakeholders, but you want to ensure your visualizations are honest and not accidentally misleading.
**Learning Objectives:** Comparing distributions across categorical groups (class-conditional analysis) and understanding how axis scaling and bin choices mislead viewers.
**ML Connection:** If a feature's distribution is identical across target classes, it is useless for a classifier. If they are clearly separated, it is a strong predictor. Visualizing this before training guides feature selection.
**Step-by-Step Analytical Instructions:**

1. Load the Titanic dataset using Seaborn and drop missing 'age' and 'fare' values.
2. Compare the 'age' distributions across the three 'class' categories (First, Second, Third). Create an overlayed histogram where all three are plotted on the same axes with transparency.
3. Next, create a "misleading" visualization: Plot a histogram of 'fare' for survivors only. Force the y-axis to only show a very small range (e.g., 0 to 5) to make it look like an extreme spike.
4. Fix the visualization: Plot the 'fare' distribution for survivors vs. non-survivors side-by-side using Seaborn boxplots, letting the axes scale automatically to the data.
5. Compare the medians of the boxplots. Does fare seem to correlate with survival?
   **Expected Output/Visualization:** An overlayed histogram of ages by class. A "bad" chart with a truncated y-axis. A "good" boxplot comparing fares by survival outcome.
   **Key Takeaway:** Always plot class-conditional distributions before modeling to gauge predictive power. And always check your axes—a truncated y-axis is the #1 way data visualizations lie.

---

## 🚀 PART 2: Capstone Project

**Domain:** 🍷 **Classic Machine Learning**

**Project Brief:**
You are tasked with predicting the quality of red wine based on its chemical properties (like acidity, sugar, and alcohol content). Before feeding the data into a Logistic Regression model to classify wines as "High Quality" (score 6 or above) vs "Low Quality" (score 5 or below), you must use Unit 2 visualization concepts to explore feature distributions, detect outliers that could skew the model, and compare chemical properties across the two quality classes.

**Dataset Suggestion:**

* **Wine Quality Dataset (Red Wine)** from UCI Machine Learning Repository.
* Direct Link: `https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv`
* *(Note: Use the semicolon `;` as the separator when loading this CSV).*

**Analytical Workflow (No Code):**

1. **Data Loading & Target Creation:** Load the dataset. Create a new binary column called 'high_quality' where the value is 1 if the 'quality' column is 6 or greater, and 0 otherwise. Build a frequency table for this new binary column to check for class imbalance.
2. **Shapes of Distributions:** Plot histograms for the 'alcohol' and 'volatile acidity' columns. Observe their shapes. Calculate and print their skewness scores to confirm if they are right or left-skewed.
3. **Outlier Detection:** Create a boxplot for 'residual sugar'. Implement the IQR (Interquartile Range) method to calculate the upper and lower bounds for this column. Count how many rows are considered statistical outliers. Decide if you should drop these rows or use a RobustScaler later.
4. **Comparing Distributions (Class-Conditional EDA):** Using Seaborn boxplots, compare the distributions of 'alcohol' and 'volatile acidity' across your new 'high_quality' binary classes. Look at the medians and the overlap between the boxes.
5. **Preprocessing & Modeling:** Drop the original 'quality' column. Split your data into training and testing sets (make sure to stratify by your target variable to maintain the class ratio). Apply `StandardScaler` to your features. Train a `LogisticRegression` model (using `class_weight='balanced'` to handle the imbalance you found in step 1). Print the classification report.

**Expected Insights:**

1. **Target Imbalance:** The frequency table will show that the dataset is moderately imbalanced (more low quality than high quality), justifying the use of `class_weight='balanced'` in the model.
2. **Skewness:** 'Alcohol' is likely right-skewed. A log transform might improve model performance, but standard scaling is a good baseline.
3. **Outliers:** 'Residual sugar' has extreme outliers on the high end. These likely represent sweet specialty wines and will distort mean-based scaling, suggesting `RobustScaler` might be a better preprocessing choice than `StandardScaler`.
4. **Class Separation:** The boxplots will clearly show that High-Quality wines have a higher median alcohol content and a lower median volatile acidity. These are your strongest predictive features, and visualizing them first confirms the model should easily pick up on these signals.

---

## 📁 PART 3: Project Directory Structure (SIMPLE & FLAT)

Since you have already created the files, here is how your flat repository is structured, along with a 1-sentence description of what belongs in each notebook:

* `01_frequency_tables_and_dotplots.ipynb` - *Contains the analytical steps to create a frequency table and a manual dot plot from the Titanic 'fare' dataset.*
* `02_histograms_and_distribution_shapes.ipynb` - *Contains the steps to plot overlapping histograms of the Iris 'petal_length' with different bin sizes and calculate skewness.*
* `03_stem_and_leaf_plots.ipynb` - *Contains the logic to build a custom text-based stem-and-leaf plot for Iris 'sepal_width' for terminal-based EDA.*
* `04_outliers_gaps_and_peaks.ipynb` - *Contains the steps to visualize a bimodal gap in Iris 'petal_length' and use IQR to detect outliers in 'sepal_width'.*
* `05_comparing_distributions_and_misleading_graphs.ipynb` - *Contains the steps to compare Titanic 'age'/'fare' by class and intentionally create/fix a misleading truncated y-axis graph.*
* `06_capstone_wine_quality_eda_and_modeling.ipynb` - *Contains the full end-to-end EDA, outlier detection, class comparison, and Logistic Regression baseline for the UCI Wine Quality dataset.*
* `readme.md` - *A brief overview of Unit 2 learning objectives, dataset sources, and instructions on how to run the notebooks sequentially.*
