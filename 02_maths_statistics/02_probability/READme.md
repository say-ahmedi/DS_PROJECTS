* [ ] 

### File 1: `01_basic_probability_simulations.ipynb`

**Task 1: Calculate Theoretical Probability**

* **Explanation:** Write pure Python code to calculate the exact probability of rolling a sum of 7 on two dice. Iterate through all possible outcomes (1-6 for die 1, 1-6 for die 2), count how many pairs equal 7, and divide by the total number of combinations (36).
* **Expected Result:** Your code should print exactly `0.1666...` or `16.67%`.

**Task 2: Monte Carlo Simulation**

* **Explanation:** Write a Python function that simulates rolling two dice 10,000 times using Python's `random` module (specifically `random.randint(1, 6)`). Keep a counter for every time the sum equals 7. Divide the final count by 10,000.
* **Expected Result:** The printed output should be a decimal between `0.15` and `0.18`. (If it is outside this range, your simulation logic is flawed).

**Purpose in your Capstone (Credit Risk & Antifraud):**

* **Why it matters:** Fraud datasets are heavily imbalanced (e.g., only 1% of transactions are fraud). Monte Carlo simulations are used to test how your fraud detection model performs under random noise. If you randomly sample transactions, what is the probability of catching a fraudster by pure luck? This exercise teaches you how to simulate random events, which is exactly how you will generate synthetic data to test your capstone models.

---

### File 2: `02_bayes_theorem.ipynb`

**Task 1: Build a 2x2 Confusion Matrix (Two-way table)**

* **Explanation:** Assume a population of 10,000 people. 1% have a disease. A test is 99% accurate. Build a 2x2 nested Python list representing True Positives, False Positives, False Negatives, and True Negatives.
* **Expected Result:** Your nested list should calculate to: `[[99, 99], [1, 9801]]`. (Total positive tests = 198).

**Task 2: Write a Bayes Theorem Function**

* **Explanation:** Write a reusable Python function called `bayes_theorem(prior, likelihood, marginal)` that takes these three inputs and returns the posterior probability. Call this function using the values from Task 1.
* **Expected Result:** The function must return exactly `0.5` (or `50%`).

**Purpose in your Capstone (Credit Risk & Antifraud):**

* **Why it matters:** This is the literal foundation of antifraud systems. Your model will "test" a transaction to see if it is fraudulent (the disease). Because fraud is rare (the 1% prior), a transaction flagged as "Fraud" by your model has a high chance of being a False Positive (a legitimate transaction blocked by mistake). Bayes' theorem is how you calculate the actual probability that a flagged transaction is truly fraudulent, which banks use to decide whether to automatically block the card or send a text message to the customer.

---

### File 3: `03_random_variables_distributions.ipynb`

**Task 1: Calculate Expected Value (Expected Loss)**

* **Explanation:** Write code to calculate the expected return of a $2 lottery ticket where the odds of winning the $500 prize are 1 in 1,000 (0.001). Calculate: `(Probability of Winning * Payout) - Cost of Ticket`.
* **Expected Result:** The code should print exactly `-1.5`.

**Task 2: Simulate and Plot a Binomial Distribution**

* **Explanation:** Simulate flipping a biased coin (60% chance of heads) 10 times. Repeat this entire experiment 1,000 times. Plot the results as a bar chart using `matplotlib` (X-axis = number of heads, Y-axis = frequency).
* **Expected Result:** A bell-shaped bar chart where the highest bar is exactly at `6` heads.

**Task 3: Simulate and Plot a Poisson Distribution**

* **Explanation:** Use `numpy.random.poisson(lam=5, size=1000)` to simulate 1,000 minutes of call center data (average 5 calls per minute). Plot a histogram of this data.
* **Expected Result:** A bell-shaped histogram that peaks around the numbers `4`, `5`, and `6` on the X-axis.

**Purpose in your Capstone (Credit Risk & Antifraud):**

* **Expected Value (Task 1):** This is the exact formula used in Credit Risk! Banks calculate **Expected Loss (EL)**. `EL = Probability of Default (PD) * Exposure at Default (EAD) * Loss Given Default (LGD)`. If you lend $500 to someone with a 0.1% chance of defaulting, what is your expected loss? It is the exact same math as the lottery ticket.
* **Binomial (Task 2):** Models binary outcomes. A transaction is either Fraud (1) or Not Fraud (0). You will use this to predict the probability of getting $X$ number of fraudulent transactions out of $N$ total transactions.
* **Poisson (Task 3):** Models the rate of events over time. Hackers often attack in bursts. A Poisson distribution is used in anomaly detection to establish a "normal" baseline of transactions per minute for a user. If a user suddenly makes 50 transactions in a minute when their Poisson baseline is 5, your antifraud system triggers an alarm.
