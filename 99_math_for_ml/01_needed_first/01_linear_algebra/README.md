# Needed First: Linear Algebra for ML

## Purpose

Learn enough linear algebra to reason about tabular ML data, model inputs, distances, and neural-network computations. This is an implementation lab, not a proof-heavy course.

## Work through in order

| File                                                 | Focus                                                                    | Required deliverable                                                                                                                                       |
| ---------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `01_vectors_matrices_shapes.ipynb`                 | Vectors, matrices, dimensions, axes, reshaping and shape contracts       | Complete all shape exercises, pass the exact assertions in the notebook, and explain what each axis represents.                                            |
| `02_operations_matmul_transpose_dot_product.ipynb` | Elementwise operations, dot product, transpose and matrix multiplication | Implement loop-based matrix multiplication; match NumPy on two valid cases; reject invalid inputs; compute a linear score per observation.                 |
| `03_norms_broadcasting_distances.ipynb`            | L1/L2 norms, cosine similarity, broadcasting and pairwise distance       | Implement and test norms, cosine similarity (including zero-vector behavior), and pairwise Euclidean distances; demonstrate the effect of feature scaling. |
| `04_capstone_transaction_similarity.ipynb`         | Combine all three topics                                                 | Produce a reproducible similarity analysis for synthetic transactions, comparing raw and standardized features and reporting nearest neighbours.           |

## Exact completion criteria

Use `ACCEPTANCE_CRITERIA.md` as the grading checklist. Each notebook also ends with a checklist and executable assertions. Do not check a notebook off until:

1. Every task has been attempted and every `TODO` / `NotImplementedError` relevant to that notebook has been resolved.
2. The notebook executes from top to bottom after **Kernel → Restart Kernel and Run All**.
3. All acceptance assertions pass without being commented out or weakened.
4. The requested printed results, comparisons, and written explanations are present.
5. You can explain the implementation without reading the code line by line.
6. You have saved your work and made a meaningful Git commit.

A notebook with the correct headings but unfinished code is **not complete**. A notebook that runs only because earlier cells were executed out of order is **not complete**.

## Suggested pacing

- Notebook 1: 60–90 minutes.
- Notebook 2: 90–120 minutes.
- Notebook 3: 90–120 minutes.
- Capstone: 2–3 hours.

These are planning estimates, not deadlines. If an acceptance test fails, fix the cause and record what you learned rather than moving on just to keep a calendar.

## Rules for every notebook

- State each array's shape and what its axes mean.
- Implement at least the functions explicitly requested; do not replace a from-scratch exercise with a one-line library call.
- Verify results with hand calculations, `np.allclose`, and shape/edge-case assertions.
- Write at least 2–4 sentences describing the result and one limitation/common mistake.
- Do not commit private banking data, credentials, or large generated artifacts.

## Capstone boundary

The capstone ranks synthetic transactions by feature-space similarity. It **does not detect fraud** and has no fraud labels. Similarity alone is not evidence that a transaction is fraudulent. These mathematical concepts can later support separate feature analysis in your Anti-Fraud project.
