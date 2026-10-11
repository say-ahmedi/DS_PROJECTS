# Linear Algebra: Unit 1 - Vectors and Spaces

## 📖 What this unit consists of

This unit covers the absolute foundation of Linear Algebra. Based on the Khan Academy curriculum, it includes:

* **Vector Introduction:** What vectors are, how to represent them in Python, and their geometric intuition.
* **Real Coordinate Spaces:** Understanding $\mathbb{R}^2$, $\mathbb{R}^3$, and $\mathbb{R}^n$ dimensions.
* **Vector Addition:** Adding vectors algebraically (component-by-component) and graphically (tip-to-tail).
* **Scalar Multiplication:** Stretching or shrinking vectors by a constant number.
* **Vector Examples:** Combining these operations to solve real-world geometric problems.

## 🎯 Why I created this (Purpose)

In Data Science and Machine Learning, data is represented as vectors. A house's features (bedrooms, bathrooms, square footage) is a vector in $\mathbb{R}^3$. A user's movie ratings is a vector in $\mathbb{R}^{1000}$. Before I can use libraries like NumPy or PyTorch, I must understand how to manipulate these vectors natively in Python.

---

## 📁 Files and Project Tasks

### File 1: `01_vector_intro_for_linear_algebra.ipynb`

**Objective:** Understand what a vector is and how to represent it in Python.

* **Task 1: Universal (Algebraic Representation)**
  * *Instructions:* Create a 2D vector `[3, 4]` using a Python list. Calculate its magnitude (length) using the Pythagorean theorem formula: $\sqrt{x^2 + y^2}$.
  * *Acceptance Criteria:* The code correctly calculates the magnitude as `5.0`.
* **Task 2: Universal (Geometric Representation)**
  * *Instructions:* Use `matplotlib.pyplot` to plot the vector `[3, 4]` as an arrow starting from the origin `(0,0)`. Use `plt.quiver` or `plt.arrow`.
  * *Acceptance Criteria:* A plot renders showing an arrow pointing from (0,0) to (3,4) with appropriate axes scaling.
* **Task 3: Deep Concept (Vectors vs. Scalars)**
  * *Instructions:* Write a Python function `is_vector(obj)` that returns `True` if the object is a list or tuple of numbers (a vector), and `False` if it is a single number (a scalar).
  * *Acceptance Criteria:* Passing `[1, 2]` returns True. Passing `5` returns False.
* **Task 4: ML Domain (Natural Language Processing - NLP)**
  * *Context:* In NLP, a sentence can be represented as a "vector" of word counts.
  * *Instructions:* Create a vocabulary list of 5 words `["the", "cat", "sat", "on", "mat"]`. Represent the sentence "the cat sat on the mat" as a numerical vector where each element is the count of the corresponding vocabulary word.
  * *Acceptance Criteria:* The code outputs the list `[1, 1, 1, 1, 1]` (or `[2, 1, 1, 1, 1]` depending on how you count "the").

---

### File 2: `02_real_coordinate_spaces.ipynb`

**Objective:** Understand dimensions and vectors in $\mathbb{R}^n$.

* **Task 1: Universal (2D and 3D Spaces)**
  * *Instructions:* Create a vector in $\mathbb{R}^2$ (2 dimensions) and a vector in $\mathbb{R}^3$ (3 dimensions) using Python lists. Write a function `get_dimension(vec)` that returns the number of dimensions.
  * *Acceptance Criteria:* `get_dimension([4, 5])` returns 2. `get_dimension([4, 5, 6])` returns 3.
* **Task 2: Universal (High-Dimensional Space)**
  * *Instructions:* Create a vector in $\mathbb{R}^{10}$ using a list comprehension (e.g., all 1s). Try to print it.
  * *Acceptance Criteria:* The code successfully generates and prints a list of 10 numbers.
* **Task 3: Deep Concept (Magnitude in $\mathbb{R}^n$)**
  * *Instructions:* Write a generalized function `calculate_magnitude(vector)` that works for ANY dimension (2D, 3D, 10D, etc.) by looping through the components, squaring them, summing them, and taking the square root.
  * *Acceptance Criteria:* Passing `[3, 4]` returns 5.0. Passing `[1, 2, 2]` returns 3.0.
* **Task 4: ML Domain (Recommendation Systems)**
  * *Context:* In RecSys, a user's profile is a vector in a high-dimensional space representing their ratings for 5 different movies.
  * *Instructions:* Create an $\mathbb{R}^5$ vector for User A representing their ratings (1 to 5 stars) for 5 movies. Create an $\mathbb{R}^5$ vector for User B. Calculate the magnitude of both user vectors to see who has a higher "overall engagement" score.
  * *Acceptance Criteria:* Two 5-dimensional vectors are created. The script correctly prints which user has the higher magnitude.

---

### File 3: `03_adding_vectors_algebraically_and_graphically.ipynb`

**Objective:** Master vector addition (component-by-component and tip-to-tail).

* **Task 1: Universal (Algebraic Addition)**
  * *Instructions:* Write a function `add_vectors(v1, v2)` that takes two lists of the same length and returns a new list where the components are added together (e.g., `[1, 2] + [3, 4] = [4, 6]`).
  * *Acceptance Criteria:* The function successfully adds the components and handles vectors of any dimension (e.g., $\mathbb{R}^3$).
* **Task 2: Universal (Graphical Addition - Tip to Tail)**
  * *Instructions:* Plot vector A `[2, 1]` starting from the origin. Plot vector B `[1, 3]` starting from the *tip* of vector A. Plot the resulting vector C (A+B) starting from the origin.
  * *Acceptance Criteria:* A matplotlib plot shows the three vectors forming a triangle, proving the geometric rule of addition.
* **Task 3: Deep Concept (Vector Subtraction)**
  * *Instructions:* Subtracting a vector is adding its negative. Write a function `subtract_vectors(v1, v2)`. Then, graphically plot `v1 - v2` to see the resulting displacement vector.
  * *Acceptance Criteria:* Algebraically `[5, 5] - [2, 3] = [3, 2]`. The graph correctly reflects this.
* **Task 4: ML Domain (Classical ML - K-Means Clustering)**
  * *Context:* In K-Means, you calculate the new center of a cluster (centroid) by taking the average of all data point vectors in that cluster.
  * *Instructions:* You have 3 data points in $\mathbb{R}^2$: `[1,2]`, `[3,4]`, and `[5,6]`. Use your `add_vectors` function to add them all together, then divide by 3 to find the new centroid vector.
  * *Acceptance Criteria:* The code outputs the centroid vector `[3.0, 4.0]`.

---

### File 4: `04_multiplying_a_vector_by_a_scalar.ipynb`

**Objective:** Understand scalar multiplication and vector scaling.

* **Task 1: Universal (Algebraic Scaling)**
  * *Instructions:* Write a function `scale_vector(scalar, vector)` that multiplies a number (scalar) by a vector. It should multiply every component inside the vector by that scalar.
  * *Acceptance Criteria:* `scale_vector(3, [1, 2])` returns `[3, 6]`.
* **Task 2: Universal (Graphical Scaling)**
  * *Instructions:* Plot the original vector `[2, 2]`. Then, plot the same vector scaled by 2 (it should stretch) and scaled by 0.5 (it should shrink) on the same graph.
  * *Acceptance Criteria:* The graph shows three arrows of different lengths along the same direction line.
* **Task 3: Deep Concept (Linear Combinations)**
  * *Instructions:* A linear combination is $c_1\mathbf{v}_1 + c_2\mathbf{v}_2$. Let $\mathbf{v}_1 = [1, 0]$ and $\mathbf{v}_2 = [0, 1]$. Calculate the linear combination where $c_1 = 3$ and $c_2 = 4$.
  * *Acceptance Criteria:* The code correctly scales both vectors and adds them together, resulting in `[3, 4]`.
* **Task 4: ML Domain (Computer Vision)**
  * *Context:* In Computer Vision, an image is a grid of pixels (a matrix, which is a list of vectors). To change the brightness of an image, you multiply the pixel vector by a scalar.
  * *Instructions:* Create a 1D vector representing a row of 3 grayscale pixels: `[100, 150, 200]`. Use your `scale_vector` function to increase the brightness by 50% (multiply by 1.5). Ensure no pixel exceeds 255 (the max for an 8-bit image).
  * *Acceptance Criteria:* The output vector is `[150, 225, 255]`. (Note: 200 * 1.5 = 300, but it must be clamped/capped at 255).

---

### File 5: `05_vector_examples.ipynb`

**Objective:** Combine all previous concepts to solve real geometric problems.

* **Task 1: Universal (Distance Between Two Points)**
  * *Instructions:* The distance between point A and point B is the magnitude of the vector $(B - A)$. Let A = `[1, 1]` and B = `[4, 5]`. Write code to calculate this distance using your previously built `subtract_vectors` and `calculate_magnitude` functions.
  * *Acceptance Criteria:* The code outputs `5.0`.
* **Task 2: Universal (Centering Data)**
  * *Instructions:* You have a list of 3 vectors: `[2,4]`, `[4,6]`, `[6,8]`. Find the mean vector (average of all 3). Then, subtract the mean vector from all 3 original vectors to "center" the data around the origin.
  * *Acceptance Criteria:* The mean vector is calculated as `[4.0, 6.0]`. The centered vectors are `[-2, -2]`, `[0, 0]`, `[2, 2]`.
* **Task 3: Deep Concept (Unit Vectors)**
  * *Instructions:* A unit vector has a length of 1. To normalize a vector, you divide it by its own magnitude. Write a function `normalize(vector)` that returns the unit vector.
  * *Acceptance Criteria:* Passing `[3, 4]` returns `[0.6, 0.8]`. If you calculate the magnitude of the result, it equals `1.0`.
* **Task 4: ML Domain (Antifraud - Anomaly Detection)**
  * *Context:* In Antifraud, a user's "normal" transaction behavior can be represented as a mean vector (e.g., `[Amount, TimeOfDay]`). A new transaction is an anomaly if the distance from this mean vector is too large.
  * *Instructions:* Define a user's historical mean behavior vector as `[50.0, 14.0]` ($50 at 2PM). Define 3 new incoming transactions as vectors. Calculate the Euclidean distance from the mean for each. Flag any transaction with a distance > 30 as "Anomaly".
  * *Acceptance Criteria:* A transaction vector like `[500.0, 14.0]` is correctly flagged as "Anomaly", while `[55.0, 15.0]` is ignored.

---

## 📝 Capstone Connection

By completing these 5 files, I am building the mathematical foundation for all Machine Learning.

* **NLP (File 1):** Text becomes vectors.
* **RecSys (File 2):** Users and items exist in high-dimensional coordinate spaces.
* **Classical ML (File 3):** Models update by adding and averaging data vectors.
* **Computer Vision (File 4):** Images are scaled using scalar multiplication.
* **Antifraud (File 5):** Distances between vectors are used to detect anomalies.
