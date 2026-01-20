# Exercise 2: Unit Testing with Copilot
# Feature: /tests command and generating test cases

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    @staticmethod
    def kelvin_to_celsius(k):
        if k < 0:
            raise ValueError("Temperature below absolute zero")
        return k - 273.15

# TASK 1: Generate unit tests for the TemperatureConverter class.
# Highlight the class or individual methods, press Ctrl+I (Cmd+I) and type "/tests"
# or open Chat and type "/tests using pytest".

# TASK 2: Add more edge cases.
# Ask Copilot Chat: "What are some edge cases for TemperatureConverter that I should test?"
