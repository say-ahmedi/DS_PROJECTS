# Python Core Fundamentals

## 📖 What this unit consists of

This unit covers the absolute core of writing Python code for Data Science and Data Engineering. It is divided into three pillars:

* **Data types:** Lists, dictionaries, tuples, sets, strings, and booleans. How to store, access, and manipulate data efficiently.
* **Functional programming:** Writing reusable functions, using lambda functions, and utilizing built-in functions like `map()` and `filter()` to process data without writing massive loops.
* **Object-oriented programming (OOP):** Classes, objects, `__init__` methods, and encapsulation. Structuring code into logical "blueprints" rather than messy scripts.

## 🎯 Why I created this (Purpose)

As a Data Engineer/Scientist, Python is my primary tool. Before I can use libraries like Pandas, NumPy, or Scikit-Learn, I must understand how Python handles data natively. Pandas DataFrames are actually just massive combinations of dictionaries and lists under the hood, and Scikit-Learn models are built using Object-Oriented Programming.

I created this set of exercises to **build a solid, unbreakable Python foundation**. By mastering these core concepts, I will be able to write clean, efficient, and scalable code for my Credit Risk & Antifraud Capstone project, rather than slow, messy scripts.

---

## 📁 Files and Project Tasks

### File 1: `01_data_types.ipynb`

**Objective:** Master Python's core data structures (Lists, Dictionaries, Sets, Tuples).

* **Task 1: Universal (The Basics)**
  * *Instructions:* Create a dictionary representing a grocery inventory (keys = item names, values = prices). Add a new item, update the price of an existing item, and remove an item. Then, create a list of fruits and convert it into a `set` to remove any duplicates automatically.
  * *Acceptance Criteria:* The dictionary is successfully mutated (added, updated, removed), and the list successfully becomes a set with duplicates removed.
* **Task 2: Capstone (Antifraud Application)**
  * *Instructions:* Represent 3 credit card transactions using a **List of Dictionaries**. Each dictionary should have keys: `Transaction_ID`, `Amount`, `Merchant`. Write code to iterate through the list and extract only the `Amount`s into a new list. Then, use a `set` to find the unique number of merchants from the transactions.
  * *Acceptance Criteria:* A list of amounts is successfully extracted, and the set of merchants contains no duplicates.

---

### File 2: `02_functional_programming.ipynb`

**Objective:** Write modular functions and use functional tools like `map()`, `filter()`, and `lambda`.

* **Task 1: Universal (The Basics)**
  * *Instructions:* Write a standard function `is_even(n)` that returns True if a number is even, and False if odd. Create a list of numbers from 1 to 10. Use the `filter()` function with your `is_even` function to create a new list containing only the even numbers.
  * *Acceptance Criteria:* The `filter()` function successfully returns `[2, 4, 6, 8, 10]`.
* **Task 2: Capstone (Antifraud Application)**
  * *Instructions:* Create a list of transaction amounts as strings (e.g., `["$150.50", "$20.00", "$5000.00"]`). Write a `lambda` function combined with `map()` to convert this list of strings into a list of floats. Then, write a function `flag_high_risk(amount)` that returns "High Risk" if the amount is over $1000, and "Normal" otherwise. Map this function to your new list of floats.
  * *Acceptance Criteria:* The list of strings is converted to floats successfully. The final output is a list of strings: `["Normal", "Normal", "High Risk"]`.

---

### File 3: `03_object_oriented_programming.ipynb`

**Objective:** Structure code using Classes, Objects, and Methods.

* **Task 1: Universal (The Basics)**
  * *Instructions:* Create a `Car` class. The `__init__` method should set the `make`, `model`, and `speed` (default 0). Create a method `accelerate()` that increases speed by 10, and a method `brake()` that decreases speed by 10. Instantiate a car object and test the methods.
  * *Acceptance Criteria:* Instantiating `Car("Toyota", "Camry")` works. Calling `accelerate()` twice makes the speed 20. Calling `brake()` makes it 10.
* **Task 2: Capstone (The Antifraud Engine)**
  * *Instructions:* Create a `Transaction` class. The `__init__` method should accept `amount`, `location`, and `is_fraud`. Create a method `evaluate_risk()` that returns "Blocked" if the amount is > $10,000 OR if the location is "International", otherwise returns "Approved". Instantiate 3 different `Transaction` objects and call the method on them.
  * *Acceptance Criteria:* The class successfully creates transaction objects. The `evaluate_risk()` method correctly returns "Blocked" or "Approved" based on the logic.

---

## 📝 Capstone Connection

By mastering these Python fundamentals, I am building the exact architecture needed for a production-grade Data Pipeline.

* **Data types** are how I will ingest raw JSON data from an API.
* **Functional programming** is how I will clean and transform thousands of rows of that data efficiently without crashing my computer's memory.
* **OOP** is how I will package my Antifraud logic into a reusable `FraudDetector` class, so I can easily save it and share it with other developers on my team.
