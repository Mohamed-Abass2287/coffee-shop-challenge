# coffee-shop-challenge-phase3
In this repo i am working with a Coffee shop-style domain. We have three models: Coffee, Customer, and Order. For our purposes, a Coffee has many Orders, a Customer has many Orders, and an Order belongs to a Customer and to a Coffee. Coffee - Customer is a many-to-many relationship

# Project structure
coffee-shop-challenge/ ├── Pipfile ├── debug.py ├── customer.py ├── coffee.py ├── order.py └── tests/ ├── customer_test.py ├── coffee_test.py └── order_test.py

# Features
Creation of customers and coffee types.
Creation of orders linking customers and coffees with price validation.
Type checking to ensure correct object types are used.
Price validation to ensure prices are within a reasonable range .
Error handling for invalid inputs.

# How to Run
1.Ensure you have Python 3 installed.
2.Run the debug.py script to see example usage and output:
 python3 debug.py
 3.To run tests (if any), use your preferred test runner, for example:
  pytest tests/

# Error Cases
Creating an order with invalid customer or coffee types will raise a TypeError.
Creating an order with a price outside the range 1.0 to 10.0 will raise a ValueError.
Creating a coffee with a name shorter than 2 characters will raise a ValueError.




