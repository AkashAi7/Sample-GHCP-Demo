# Exercise 4: Refactoring and Modernization
# Feature: Inline Chat Refactoring and Type Hinting

# TASK 1: Refactor this loop into a list comprehension.
# Highlight the code below, press Ctrl+I (Cmd+I) and type "refactor to list comprehension"

def get_squares(numbers):
    squares = []
    for n in numbers:
        if n % 2 == 0:
            squares.append(n * n)
    return squares

# TASK 2: Add Type Hints.
# Highlight the function below, press Ctrl+I (Cmd+I) and type "add type hints"

def calculate_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        return price
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount

# TASK 3: Modernize Code.
# This function uses old-style string formatting. Use Copilot to change it to f-strings.
# Highlight the function, press Ctrl+I and type "use f-strings"

def greet_user(user_info):
    message = "Hello, %s! You have %d new messages." % (user_info['name'], user_info['messages'])
    return message
