# Needed First: Linear Algebra for ML

## Purpose

Learn enough linear algebra to reason about tabular ML data, model inputs, distances, and neural-network computations. This is an implementation lab, not a proof-heavy course.

## Work through in order

| File                                                 | Focus                                                                    | Required deliverable                                                                                                                                       |
| ---------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `01_vectors_matrices_shapes.ipynb`                 | Vectors, matrices, dimensions, axes, reshaping and shape contracts       | Complete all shape exercises, pass the exact assertions in the notebook, and explain what each axis represents.                                            |
| `02_operations_matmul_transpose_dot_product.ipynb` | Elementwise operations, dot product, transpose and matrix multiplication | Implement loop-based matrix multiplication; match NumPy on two valid cases; reject invalid inputs; compute a linear score per observation.                 |
| `03_norms_broadcasting_distances.ipynb`            | L1/L2 norms, cosine similarity, feature-wise broadcasting and distance    | Implement norms, cosine, standardization, pairwise distances, and a small nearest-neighbor comparison with numerical and edge-case checks.                 |
| `04_capstone_content_recommendations.ipynb`        | Content-based recommendation with synthetic movie features               | Build a taste profile, score and rank unseen items, evaluate precision/recall at k, and test feature-weight and cold-start limits.                         |

Notebook 1 contains earlier learner work and needs a fresh-kernel review. Notebooks 2–4 are assignment notebooks, **not completed solutions**. Notebook 3 and the recommendation capstone each have four focused tasks. All explanations, starter data, and checks live in their corresponding `.ipynb` files.

## Exact completion criteria

Use the checklist below and each notebook's own acceptance criteria. Do not check a notebook off until:

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
- Notebook 3: 75–105 minutes.
- Capstone: 90–120 minutes, after the first three notebooks.

These are planning estimates, not deadlines. If an acceptance test fails, fix the cause and record what you learned rather than moving on just to keep a calendar.

## Rules for every notebook

- State each array's shape and what its axes mean.
- Implement at least the functions explicitly requested; do not replace a from-scratch exercise with a one-line library call.
- Verify results with hand calculations, `np.allclose`, and shape/edge-case assertions.
- Write at least 2–4 sentences describing the result and one limitation/common mistake.
- Do not commit private banking data, credentials, or large generated artifacts.

## Capstone boundary

The capstone is a synthetic content-based recommendation exercise. It uses held-out relevance labels for evaluation but does not establish how the approach would perform with real users. Similarity alone is not evidence that a transaction is fraudulent; fraud evaluation belongs in the separate probability and statistics capstone.
