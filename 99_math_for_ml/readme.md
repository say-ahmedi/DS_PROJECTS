# Math for Machine Learning

This directory is a practical math track for ML. The folders describe learning priority; a notebook file alone is not evidence of completion. Work through the needed-first notebooks in order, test results in NumPy, and explain their use for data or a model.

## Learning path

| Stage                        | Directory                                                                     | Exit skill                                                                                                                                     |
| ---------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Linear algebra            | [01_linear_algebra](01_needed_first/01_linear_algebra/README.md)               | Shapes and axes; elementwise operations, dot products, transpose, matrix multiplication, L1/L2 norms, distances, and input validation.         |
| 2. Probability               | [02_probability](01_needed_first/02_probability/README.md)                     | Conditional probability, Bayes' rule, independence, random variables, expectation, variance, covariance, correlation, and basic distributions. |
| 3. Applied statistics        | [03_applied_statistics](01_needed_first/03_applied_statistics/README.md)       | Mean, median, quantiles, standard deviation, outliers, confidence intervals, basic hypothesis tests, and p-values.                             |
| 4. Calculus and optimization | [04_calculus_optimization](01_needed_first/04_calculus_optimization/README.md) | Derivatives, partial derivatives, gradients, chain rule, gradient descent, and simple extrema.                                                 |
| 5. Model math                | [05_classical_ml_math](01_needed_first/05_classical_ml_math/README.md)         | Linear/logistic scores and loss; tree-split measures.                                                                                          |
| 6. Evaluation                | [06_fraud_metrics](01_needed_first/06_fraud_metrics/README.md)                 | Precision, recall, and threshold trade-offs for imbalanced classification.                                                                     |

Stages 1–4 are early foundations in the original notes. Stages 5–6 are practical bridges to study alongside their models. You can begin tabular ML once the relevant basics are usable; finishing every notebook in this directory is not a prerequisite.

## Priorities

### Essential for initial practical ML

- **Linear algebra:** vector and matrix meaning, shapes, matrix operations and multiplication, transpose, dot product, and L1/L2 norms. Learn broadcasting and distances for preprocessing or similarity work.
- **Probability:** events, conditional probability, Bayes' rule, independence, random variables, expectation, variance, covariance, correlation, and basic distributions.
- **Statistics:** mean, median, quantiles, standard deviation, outliers, confidence intervals, introductory hypothesis tests, and interpretation of p-values.
- **Optimization:** derivatives, partial derivatives, gradient, chain rule, and gradient descent. An intuitive understanding of convexity is sufficient at first.

### Recommended when needed

- Linear/logistic loss, tree-split criteria, class-imbalance metrics, and threshold selection while building those models.
- Scaling, cosine similarity, and pairwise distances for similarity or nearest-neighbor methods.
- Eigenvector intuition and PCA when using dimensionality reduction.
- Bootstrap, permutation tests, power, effect size, and multiple-testing correction for deeper experimental analysis.

### Can wait

[02_needed_later](02_needed_later/) holds SVD, spectral decomposition, QR, pseudoinverse, matrix condition number, Hessian, Jacobian, Taylor expansion, convex optimization, Lagrange multipliers, maximum likelihood/MAP, entropy, KL divergence, cross-entropy, CLT/LLN, and Bayesian inference. These topics are useful, but they are not prerequisites for the current linear algebra notebook. The older README called eigenvalues/eigenvectors “absolutely mandatory” for PCA; their intuition is useful when reaching PCA, while full derivation can be deferred.

## Applied bridges

[03_applied_ml_bridges](03_applied_ml_bridges/) connects math to small implementations: PCA from scratch, NumPy backpropagation, convolution/pooling, and softmax/cross-entropy/drift. Use each bridge when the associated ML work creates a concrete need. These are focused exercises rather than extra portfolio projects.

## Study resources from the original notes

- **For first-pass linear algebra:** Khan Academy's vectors/spaces and matrix transformations. Use its precalculus vector/matrix material if the linear algebra course feels too fast.
- **For first-pass calculus:** introductory differentiation followed by multivariable partial derivatives and gradients.
- **For later depth:** the original notes suggest StatQuest and 3Blue1Brown for eigenvector/PCA intuition, MIT 18.06 and Gilbert Strang for linear algebra, and *Mathematics for Machine Learning* for matrix decompositions. Treat these as optional references for a specific question, not a separate course sequence to finish before doing ML.

## Completion rule

1. Finish task code and written interpretation.
2. Run the notebook from a fresh kernel, top to bottom, without unexpected errors.
3. Keep shape, numerical, and invalid-input assertions.
4. Compare at least one manual result with NumPy or a hand calculation.
5. Record the completed notebook or commit. A placeholder or saved output alone is not completion.

Assignments and self-checks are now inside the notebooks. Follow the [linear algebra sequence](01_needed_first/01_linear_algebra/README.md), then the [probability sequence](01_needed_first/02_probability/README.md), and use [weekly_notes](weekly_notes/README.md) for short reflections. The [earlier assessment](PROGRESS_REPORT.md) records the state before the notebook rebuild.

## Capstones

1. [Content-based movie recommendations](01_needed_first/01_linear_algebra/04_capstone_content_recommendations.ipynb) follows the three linear algebra lessons. It combines vectors, matrix shapes, norms, cosine scores, ranking, and top-k evaluation.
2. [Fraud alert evaluation](01_needed_first/03_applied_statistics/03_capstone_fraud_alert_evaluation.ipynb) follows the three probability lessons and the two applied-statistics topics. It combines base rates, conditional probability, distribution summaries, correlation, confidence intervals, and held-out threshold evaluation.

The capstones use different synthetic datasets and can be completed independently once their listed prerequisites are understood. They require NumPy and basic Python only.

## Original reference images

The source images distinguish topics needed early from those needed later: [linear algebra](image/readme/1793117432317.png), [calculus](image/readme/1793117482978.png), [probability](image/readme/1793117496023.png), and [statistics](image/readme/1793117541318.png).
