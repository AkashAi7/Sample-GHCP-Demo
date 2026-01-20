# Exercise 5: Debugging with Copilot
# Feature: /fix command and smart error suggestions

# This script has several bugs (syntax and logic). 
# Open this file in VS Code. Look for the red squiggly lines or run the script and see errors.

# TASK 1: Use the /fix command.
# Highlight a function with an error, press Ctrl+I and type "/fix".

def divide_numbers(a, b)
    # Syntax error: missing colon
    return a / b

def find_average(data):
    # Logic error: potential division by zero
    total = sum(data)
    count = len(data)
    return total / count

# TASK 2: Use Copilot to add error handling.
# Highlight the 'find_average' function and ask Chat: "Add try-except block to handle empty lists."

# TASK 3: Fix the logical bug in the following check.
# The user wants to check if a number is both even AND prime.
# Copilot can help identify that 2 is the only even prime.

def is_even_and_prime(n):
    if n % 2 == 0 or n > 1: # This logic is wrong
        return True
    return False

# Ask Copilot: "/fix the logic to correctly check if n is an even prime number."
