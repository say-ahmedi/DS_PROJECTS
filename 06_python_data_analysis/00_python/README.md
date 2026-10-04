# Python Core Fundamentals

## 📖 What this unit consists of

This unit covers the absolute core of writing Python code for Data Science and Data Engineering. Based on the core knowledge table, it is divided into three files:

1. **Data Types:** Names, how/when to use them, and implementation (Lists, Dictionaries, Sets, Tuples).
2. **Functional Programming:** `if/else` logic, `loops`, standard `functions`, and `advanced functions` (lambda, map, filter).
3. **Object Oriented Programming (OOP):** Definitions, `classes/objects`, `OOP principles` (Encapsulation, Inheritance), and `multiclass project implementation`.

## 🎯 Why I created this (Purpose)

As a Data Engineer/Scientist, Python is my primary tool. Before using Pandas or Scikit-Learn, I must understand how Python handles data natively. I created these exercises to build an unbreakable Python foundation for my Credit Risk & Antifraud Capstone project.

---

## 📁 Files and Project Tasks

### File 1: `01_data_types.ipynb`

**Objective:** Master Python's core data structures (How and when to use them).

* **Task 1: Universal (Lists, Tuples, and Sets)**
  * *Instructions:* Create a `list` of numbers. Convert it to a `tuple` to lock it from being changed. Convert it to a `set` to remove duplicates automatically. Print all three to see the differences.
  * *Acceptance Criteria:* The code successfully runs and prints the list, the tuple, and the set. The set must have fewer items than the list if there were duplicates.
* **Task 2: Universal (Dictionaries)**
  * *Instructions:* Create a dictionary representing a phone book (Keys = Names, Values = Phone Numbers). Add a new contact, update an existing number, and delete a contact.
  * *Acceptance Criteria:* The dictionary is mutated correctly (added, updated, deleted) and the final dictionary prints without errors.
* **Task 3: Capstone (Antifraud Application)**
  * *Instructions:* Represent 3 credit card transactions using a **List of Dictionaries**. Each dictionary should have keys: `Transaction_ID`, `Amount`, and `Merchant`. Write a loop to extract only the `Amount`s into a new list. Then, use a `set` to find the unique number of merchants.
  * *Acceptance Criteria:* A list of amounts is successfully extracted, and the set of merchants contains no duplicates.

---

### File 2: `02_functional_programming.ipynb`

**Objective:** Master control flow, iteration, and functional tools.

* **Task 1: Universal (if/else and loops)**
  * *Instructions:* Create a list of temperatures in Celsius. Use a `for` loop to iterate through them. Use `if/elif/else` statements to print "Hot" if > 30, "Warm" if between 15 and 30, and "Cold" if < 15.
  * *Acceptance Criteria:* The loop successfully iterates, and the `if/else` logic correctly categorizes each temperature.
* **Task 2: Universal (Functions and Modularity)**
  * *Instructions:* Write a standard function `calculate_discount(price, discount_percentage)` that returns the final price. Include a default argument for `discount_percentage` (e.g., 10%). Call the function with and without the second argument.
  * *Acceptance Criteria:* The function returns the correct math. Calling it with one argument works (uses default), and calling it with two arguments overrides the default.
* **Task 3: Capstone (Advanced Functions)**
  * *Instructions:* Create a list of transaction amounts as strings (e.g., `["$150.50", "$20.00", "$5000.00"]`). Write a `lambda` function combined with `map()` to convert this list of strings into a list of floats. Then, write a function `flag_high_risk(amount)` that returns "High Risk" if > 1000, else "Normal". Use `filter()` to keep only the "High Risk" transactions.
  * *Acceptance Criteria:* The `map()` successfully converts strings to floats. The `filter()` successfully returns only the high-risk amounts.

---

### File 3: `03_OOP.ipynb`

**Objective:** Structure code using Classes, Objects, and OOP Principles.

* **Task 1: Universal (Definition, Classes, and Objects)**
  * *Instructions:* Create a `Car` class. The `__init__` method (constructor) should set the `make`, `model`, and `speed` (default 0). Create a method `accelerate()` that increases speed by 10. Instantiate (create) a car object and call the accelerate method.
  * *Acceptance Criteria:* The class is defined. Instantiating `Car("Toyota", "Camry")` works. Calling `accelerate()` twice makes the speed 20.
* **Task 2: Universal (OOP Principles: Inheritance & Encapsulation)**
  * *Instructions:* Create a parent class `Vehicle` with an attribute `wheels`. Create a child class `Motorcycle` that inherits from `Vehicle` but sets `wheels = 2`. Add a "private" attribute in `Vehicle` (e.g., `__engine_id`) to demonstrate encapsulation.
  * *Acceptance Criteria:* The `Motorcycle` class successfully inherits from `Vehicle`. Accessing `__engine_id` directly from outside the class throws an error (encapsulation).
* **Task 3: Capstone (Multiclass Project Implementation)**
  * *Instructions:* Create two classes that interact: `Transaction` and `FraudDetector`.
    * `Transaction` takes `amount` and `location`.
    * `FraudDetector` has a method `evaluate(transaction)`. If `transaction.amount > 10000` OR `transaction.location == "International"`, it returns "Blocked", else "Approved".
    * Create 3 `Transaction` objects, pass them to a `FraudDetector` object, and print the results.
  * *Acceptance Criteria:* The multiclass system works. The `FraudDetector` correctly evaluates the `Transaction` objects and returns "Blocked" or "Approved" based on the rules.

---

## 📝 Capstone Connection

By mastering these Python fundamentals, I am building the exact architecture needed for a production-grade Data Pipeline.

* **Data types** are how I ingest raw JSON data from APIs.
* **Functional programming** is how I clean and transform thousands of rows efficiently.
* **OOP Multiclass implementation** is how I package my Antifraud logic into a reusable `FraudDetector` engine, separating the data (`Transaction`) from the business logic (`FraudDetector`), which is exactly how enterprise software is built.
