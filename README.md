## 1. General IT

Your roadmap includes programming paradigms, development methodologies, Git, data structures/algorithms, and bug-tracking systems.

| Subject                            | Project                                                            |
| ---------------------------------- | ------------------------------------------------------------------ |
| Programming principles             | **CLI Task Manager**                                         |
| Imperative/declarative programming | Implement the same data-processing problem in different styles     |
| Git                                | Maintain every project through branches, commits, PRs, tags        |
| Agile/Jira                         | Manage one project using a backlog, sprints, issues and milestones |
| Data structures                    | **Mini Algorithms Repository**                               |
| Algorithms / Big-O                 | Search, sorting, stacks, queues, trees, hash maps                  |

### Main project: CLI Task Manager

Build:

```text
Task Manager
├── create task
├── update task
├── delete task
├── search tasks
├── priorities
├── deadlines
└── save/load JSON
```

Use:

- Python
- OOP
- Git
- unit tests
- GitHub Issues
- branches
- README

This becomes your first **software-engineering project**, not a data-science project.

---

# 2. Mathematics

Your curriculum includes linear algebra, statistics, probability and A/B testing.

You don't need four major GitHub projects here.

### Project: Math for ML Notebook Collection

Create one repository:

```text
math-for-machine-learning/
│
├── linear_algebra.ipynb
├── probability.ipynb
├── statistics.ipynb
└── ab_testing.ipynb
```

### Linear Algebra

Implement:

- vectors
- matrices
- dot products
- matrix multiplication
- eigenvalues/eigenvectors
- PCA intuition

Use NumPy.

### Statistics

Take a real dataset and calculate:

- mean
- median
- variance
- standard deviation
- correlations
- confidence intervals
- hypothesis tests

### Probability

Simulate:

- coin tosses
- dice
- normal distributions
- binomial distributions
- Bayes' theorem

### A/B Testing

Build a small:

**Website Conversion A/B Test**

Example:

```text
Version A: 10,000 users → 780 conversions
Version B: 10,000 users → 850 conversions
```

Determine whether the improvement is statistically significant.

This is particularly useful for a Data Scientist portfolio.

---

# 3. Databases

Your roadmap covers normalization, ACID/BASE, relational vs NoSQL databases and SQL from basic through advanced.

### Project: E-commerce Database

Create a realistic PostgreSQL database.

Tables:

```text
users
products
categories
orders
order_items
payments
reviews
```

Practice:

- normalization
- primary/foreign keys
- constraints
- indexes
- joins
- subqueries
- CTEs
- window functions
- transactions
- views
- query optimization

Then answer business questions such as:

```text
Which products generate the most revenue?

Which customers have the highest lifetime value?

What is monthly revenue growth?

What percentage of customers return?

Which categories have the highest average order value?
```

This should become one of your important foundational projects.

---

# 4. Data Warehouse

Your roadmap then introduces Kimball/Inmon, DWH structures, ETL/ELT and structured data formats.

### Project: Retail Analytics Data Warehouse

Build:

```text
Operational databases
        ↓
       ETL
        ↓
    PostgreSQL
        ↓
Data Warehouse
        ↓
    Dashboard
```

Use a star schema:

```text
FactSales
│
├── DimCustomer
├── DimProduct
├── DimDate
└── DimStore
```

Learn:

- facts
- dimensions
- surrogate keys
- slowly changing dimensions
- ETL
- CSV/JSON/Parquet
- incremental loading

Technology:

- PostgreSQL
- Python
- Pandas
- dbt
- optionally Airflow later

Your **Taxi Analytics DWH** idea would also fit perfectly here.

---

# 5. Cloud

Your roadmap includes cloud fundamentals, AWS, security, serverless, architecture patterns, Redshift and QuickSight.

Don't create a completely new application.

Take an existing project and **deploy it to the cloud**.

### Project: Cloud Data Pipeline

For example:

```text
CSV
 ↓
Amazon S3
 ↓
Lambda
 ↓
Transformation
 ↓
Redshift
 ↓
QuickSight
```

Learn:

- IAM
- S3
- Lambda
- EC2 basics
- security groups
- Redshift
- serverless architecture
- monitoring

That is much better than making a meaningless "AWS demo."

---

# 6. Python Core

Your curriculum next covers Python fundamentals, functional programming, OOP, Pandas, NumPy, Matplotlib, Jupyter, EDA, preprocessing and visualization.

I would make **three projects**.

### Project 1 — File/Data Processing Application

Example:

**Automated CSV Analyzer**

Input:

```text
dataset.csv
```

Output:

```text
Dataset dimensions
Missing values
Duplicates
Column types
Summary statistics
Outliers
Correlations
Plots
```

Use:

- Python
- OOP
- Pandas
- NumPy
- Matplotlib

---

### Project 2 — Full EDA

Pick a dataset such as:

- telecom customers
- banking
- e-commerce
- housing
- transport

Perform:

```text
Data understanding
     ↓
Data cleaning
     ↓
Missing values
     ↓
Outliers
     ↓
Univariate analysis
     ↓
Bivariate analysis
     ↓
Correlation
     ↓
Visualization
     ↓
Business conclusions
```

This is where you learn to **think like a Data Scientist**, rather than merely use Pandas.

---

### Project 3 — Data Dashboard

For example:

**Kazakhstan Economic Dashboard**

Track:

- GDP
- inflation
- unemployment
- wages
- population

Use:

- Pandas
- Plotly
- Power BI or Streamlit

---

# 7. Machine Learning — Classification

Your roadmap covers classification, regression, clustering, PCA and evaluation metrics.

This is where serious portfolio projects should begin.

### Project: Fraud Detection

Models:

```text
Logistic Regression
Decision Tree
Random Forest
XGBoost
LightGBM
```

Learn:

- preprocessing
- pipelines
- class imbalance
- cross-validation
- hyperparameter tuning
- precision
- recall
- F1
- ROC-AUC
- PR-AUC
- SHAP

This is an excellent **ML Engineer/Data Scientist project**.

---

# 8. Machine Learning — Regression

### Project: House Price Prediction

Predict property prices using:

- Linear Regression
- Ridge
- Lasso
- Random Forest
- XGBoost/CatBoost

Focus on:

- feature engineering
- categorical variables
- RMSE
- MAE
- R²
- residual analysis

---

# 9. Unsupervised Learning

### Project: Customer Segmentation

Use:

- K-Means
- DBSCAN
- hierarchical clustering
- PCA

Pipeline:

```text
Customer data
      ↓
Cleaning
      ↓
Scaling
      ↓
Clustering
      ↓
PCA visualization
      ↓
Segment profiling
      ↓
Business recommendations
```

This is another strong Data Science portfolio project.

---

# 10. Time-Series Forecasting

Your roadmap explicitly includes preprocessing and ARIMA.

### Project: Kazakhstan Economic Forecasting

Predict:

- inflation
- unemployment
- electricity demand
- exchange rate
- sales

Compare:

```text
Naive baseline
Moving average
ARIMA
SARIMA
Prophet
XGBoost with lag features
```

Evaluate using:

- MAE
- RMSE
- MAPE

Your existing Kazakhstan macroeconomic project is already appropriate for this subject.

---

# 11. NLP Fundamentals

Your roadmap specifically includes stemming, tokenization, vectorization and NLP modeling.

This is where your **NLP specialization begins**.

### Project 1 — Spam/Sentiment Classifier

Pipeline:

```text
Raw text
 ↓
Cleaning
 ↓
Tokenization
 ↓
Lemmatization
 ↓
TF-IDF
 ↓
Logistic Regression / SVM
 ↓
Evaluation
```

Do this **before BERT**.

---

# 12. Modern NLP

Then create progressively stronger projects.

### Project 2 — Transformer Text Classifier

Compare:

```text
TF-IDF + Logistic Regression
           VS
BERT / DistilBERT / multilingual BERT
```

That comparison demonstrates that you understand both classical and modern NLP.

---

### Project 3 — Semantic Search Engine

Build something like:

> Search university documents using natural-language questions.

Architecture:

```text
Documents
   ↓
Sentence Transformers
   ↓
Embeddings
   ↓
Vector database
   ↓
Semantic similarity
   ↓
Relevant documents
```

Use:

- Hugging Face
- Sentence Transformers
- FAISS/Qdrant
- FastAPI

---

### Project 4 — Kazakh NLP

This is one I particularly recommend.

For example:

**Kazakh/Russian/English News Classifier**

or:

**Kazakh Named Entity Recognition**

or:

**Kazakh Semantic Search Engine**

A multilingual project is much more distinctive than another generic English sentiment classifier.

---

# 13. Deep Learning

Before going deeply into Transformers, create one fundamental neural-network project.

### Project: Neural Network From Scratch

Implement a small network using NumPy:

```text
Input
 ↓
Linear layer
 ↓
ReLU
 ↓
Linear layer
 ↓
Softmax
```

Implement:

- forward propagation
- loss
- backpropagation
- gradient descent

Then recreate it using PyTorch.

This will make Transformers much easier to understand later.

---

# 14. Computer Vision

Your roadmap contains image preprocessing/matrix transformations and CV modeling.

You don't need many CV projects if NLP is your main specialization.

### CV Project 1 — Image Classification

Example:

**Plant Disease Classifier**

Use:

```text
CNN baseline
      ↓
ResNet transfer learning
      ↓
augmentation
      ↓
evaluation
```

Learn:

- PyTorch
- CNNs
- image transformations
- transfer learning
- precision/recall/F1

---

### CV Project 2 — Object Detection

Later:

**Vehicle/Object Detection**

Use YOLO.

Pipeline:

```text
Images
 ↓
Annotation
 ↓
Augmentation
 ↓
YOLO training
 ↓
mAP evaluation
 ↓
Inference API
```

That's sufficient CV exposure for an NLP-oriented ML Engineer.

---

# 15. MLOps — combine everything

Your other ML curriculum goes further into experiment tracking, DVC, CI/CD, FastAPI and monitoring.

Don't create a separate MLOps toy project.

Take your **best NLP or ML model** and productionize it.

For example:

### Production NLP Service

```text
GitHub
  ↓
DVC
  ↓
Training pipeline
  ↓
MLflow
  ↓
Model registry
  ↓
FastAPI
  ↓
Docker
  ↓
GitHub Actions
  ↓
Cloud
  ↓
Monitoring
```

That can become your strongest ML Engineer project.

---

# The portfolio I would ultimately aim for

You may create many small exercises while learning, but your final GitHub portfolio doesn't need 30 major projects.

I would aim for these **8 substantial projects**:

| # | Project                                | Demonstrates                 |
| -: | -------------------------------------- | ---------------------------- |
| 1 | **E-commerce SQL Analytics**     | SQL + DB                     |
| 2 | **Analytics Data Warehouse**     | DWH + ETL                    |
| 3 | **Fraud Detection**              | Classification               |
| 4 | **Customer Segmentation**        | Clustering                   |
| 5 | **Economic Forecasting**         | Time series                  |
| 6 | **Multilingual NLP Classifier**  | Classical NLP + Transformers |
| 7 | **Semantic Search / RAG System** | Advanced NLP                 |
| 8 | **Computer Vision Project**      | CNN + transfer learning      |

And eventually turn **one of #6 or #7 into an end-to-end production ML system** with FastAPI, Docker, MLflow, CI/CD and cloud deployment.

The overall sequence should therefore be:

**General IT → Python → Math/Statistics → SQL → EDA → ML → Deep Learning → NLP → CV basics → MLOps**

For your intended direction, once you reach Deep Learning, I would allocate much more project time to **NLP than C**

# What should you do next?

Your roadmap starts General IT with programming principles, paradigms, development methodologies, Git, data structures/algorithms, and tracking systems.

So after:

```text
01_general_it/01_cli/
```

your next target should be:

```text
01_general_it/02_dsa/
```

And I would **not** build another full application immediately.

Make `02_dsa` a problem-solving module.

Study and implement:

```text
Big-O
arrays/lists
stack
queue
hash table/dictionary
set
linked list
binary search
sorting
recursion
trees basics
graphs basics
```

For each one, have:

```text
notes.md
implementation.py
problems/
```

Then solve perhaps **25–40 carefully selected problems**, rather than 300 LeetCode problems whose answers eventually become muscle memory while your brain quietly leaves the building.

Once you're comfortable there, continue through the roadmap.

---

# One project for every major part of your roadmap

Your actual training matrix supports this structure nicely. Mathematics emphasizes linear algebra, statistics, probability and A/B testing.  Databases cover normalization, ACID/BASE, relational/NoSQL databases, SQL levels and database creation.  DWH covers Kimball/Inmon, warehouse structure, ETL/ELT and common data formats.  Cloud then covers fundamentals, AWS, security, serverless and architecture.

I would structure the practical roadmap like this:

| Section                     | Main project                              | Core things you prove                                |
| --------------------------- | ----------------------------------------- | ---------------------------------------------------- |
| `01_general_it`           | **DevFlow CLI** ✅                  | Python, OOP, CLI, Git, basic architecture            |
| `02_maths_statistics`     | **StatLab**                         | probability, statistics, linear algebra, A/B testing |
| `03_databases_sql`        | **E-Commerce Database**             | PostgreSQL, schema design, SQL, indexing             |
| `04_data_warehouse_etl`   | **Taxi Analytics Warehouse**        | ETL, dimensional modeling, dbt, DWH                  |
| `05_cloud`                | **Cloud Analytics API**             | Docker, AWS/cloud, deployment, security basics       |
| `06_python_data_analysis` | **Retail Analytics**                | Pandas, NumPy, EDA, visualization                    |
| `07_machine_learning`     | **Customer Churn**                  | classification, preprocessing, evaluation            |
| `08_deep_learning`        | **Image Classifier**                | PyTorch, neural networks, CNNs                       |
| `09_nlp`                  | **Review Sentiment Analyzer**       | TF-IDF, embeddings, transformers                     |
| `10_computer_vision`      | **Object Detection Project**        | preprocessing, augmentation, detection               |
| `11_time_series`          | **Kazakhstan Economic Forecasting** | ARIMA, feature engineering, forecasting              |
| `12_mlops`                | **Production Churn Service**        | FastAPI, Docker, CI/CD, model monitoring             |

The later parts also match your matrix: Python covers Pandas, NumPy, Matplotlib, notebooks, EDA, preprocessing and visualization, while ML/DL covers classification, regression, clustering, PCA and evaluation metrics.  Time series, NLP and computer vision then appear as separate areas at the end.

## Your Mathematics project: `StatLab`

Don't try to create a gigantic mathematics platform.

Build one repository/notebook collection that answers questions such as:

```text
How do mean and variance work?
What does covariance tell us?
What does correlation actually measure?
How does a probability distribution behave?
How does Bayes' theorem update probability?
How does a confidence interval work?
How do we perform a hypothesis test?
How does an A/B test work?
How do vectors and matrices relate to ML?
How does PCA reduce dimensions?
```

Implement some formulas manually, then compare them with NumPy/SciPy.

Completion condition:

> You can explain the concept, calculate it, and show a small practical application.

Done. Move on.

## Database project: `E-Commerce Database`

Tables:

```text
customers
products
categories
orders
order_items
payments
```

Implement PostgreSQL and answer real analytical questions:

```text
Monthly revenue
Best-selling products
Revenue by category
Average order value
Most valuable customers
Repeat customers
Customers without recent purchases
Running monthly revenue
```

Use:

```text
JOIN
GROUP BY
HAVING
CTEs
subqueries
window functions
indexes
views
transactions
```

Completion condition:

> Schema designed + 30 meaningful queries + README explaining decisions.

Done.

## Data Warehouse project: `Taxi Analytics Warehouse`

This is where your database knowledge turns into data engineering.

```text
Raw taxi CSV/JSON
       ↓
staging tables
       ↓
ETL/ELT
       ↓
warehouse
       ↓
dbt transformations
       ↓
analytics
```

Create something like:

```text
fact_trips

dim_date
dim_driver
dim_location
dim_customer
dim_payment
```

Learn fact/dimension tables, star schemas, surrogate keys, ETL/ELT and basic slowly changing dimensions.

Completion condition:

> Raw data can be transformed reproducibly into an analytics-ready warehouse.

Done.

## Cloud project: `Cloud Analytics API`

Reuse something you've already created instead of inventing another business.

Take a Python analytics/ML service:

```text
Python API
↓
Docker
↓
Cloud VM/service
↓
PostgreSQL
↓
public endpoint
```

Learn deployments, environment variables, basic networking, IAM/security concepts, logs and containerization.

Completion condition:

> Another device can send a request to the deployed application and get a response.

Done.

## Python Data Analysis: `Retail Analytics`

Take a messy retail dataset.

Perform:

```text
cleaning
missing-value handling
duplicate detection
outlier analysis
EDA
aggregation
visualization
business interpretation
```

Deliver:

```text
analysis.ipynb
README.md
charts/
data/
```

And finish with 5–10 actual conclusions about the business.

## Machine Learning: `Customer Churn`

You've already worked with this type of project, so don't unnecessarily reinvent it.

Compare models such as:

```text
Logistic Regression
KNN
Decision Tree
Random Forest
```

Evaluate using:

```text
precision
recall
F1
ROC-AUC
```

Explain why customers churn and what the model can realistically do.

## Deep Learning: `Image Classifier`

Use PyTorch.

Start with a simple network, then CNN.

Learn:

```text
Dataset
DataLoader
training loop
loss
optimizer
backpropagation
validation
overfitting
regularization
CNN
```

A CIFAR-10 or similar dataset is enough.

## NLP: `Sentiment Analyzer`

Do it in two stages.

First classical NLP:

```text
cleaning
tokenization
TF-IDF
Logistic Regression
```

Then:

```text
embeddings
transformer model
```

Now you have an excellent comparison between traditional NLP and modern NLP.

## Computer Vision: `Object Detection`

Since image classification is already in Deep Learning, don't duplicate it.

Use a small object-detection dataset and learn:

```text
bounding boxes
IoU
augmentation
precision
recall
detection pipeline
```

## Time Series: `Kazakhstan Economic Forecasting`

Use an economic indicator.

For example:

```text
unemployment
inflation
GDP-related indicator
```

Compare:

```text
baseline
ARIMA
lag-based regression
another ML model
```

Evaluate with MAE/RMSE/MAPE.

## MLOps: `Production Churn Service`

Do **not train another model**.

Take your completed ML model:

```text
trained model
↓
FastAPI
↓
Docker
↓
tests
↓
GitHub Actions
↓
deployment
↓
basic monitoring
```

That's how the entire roadmap finally joins together.

---

Your rule from this point onward should be:

> **Each project exists to teach a defined set of concepts. Once it has taught them, finish it and move forward.**

DevFlow has taught you what it needed to teach.

So assuming the real files run without the two paste/syntax issues I mentioned:
My Task Checkbox Progress:

**`01_cli = COMPLETE ✅`**
**`02_maths_statistics is being done right now 🔄`""
