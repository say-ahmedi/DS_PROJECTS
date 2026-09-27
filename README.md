
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

**`01_cli = COMPLETE ✅`**

Your next destination is **`02_dsa`**, not DevFlow v2.7 Enterprise Edition.
