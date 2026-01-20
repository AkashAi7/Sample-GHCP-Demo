# Exercise 3: Regex and Data Transformation
# Feature: Natural Language to Code (Regex, JSON, etc.)

import json

# TASK 1: Create a regex to extract Phone Numbers from a string.
# Ask Copilot Chat: "Generate a Python regex to find phone numbers in the format (XXX) XXX-XXXX or XXX-XXX-XXXX"
# Write your code below using Copilot's suggestion:

text = "Call me at (555) 123-4567 or 987-654-3210."

# TASK 2: Data Transformation.
# We have a list of raw user data. Use Copilot to convert this into a list of clean JSON objects.
# Use Inline Chat (Ctrl+I) on the variable below and say "Convert these raw strings into a list of dictionaries with keys: id, name, and role"

raw_users = [
    "ID: 001, Name: Alice Smith, Role: Admin",
    "ID: 002, Name: Bob Jones, Role: User",
    "ID: 003, Name: Charlie Brown, Role: Guest"
]

# TASK 3: Format the JSON output.
# Use Copilot to write a function that takes the list above and returns a pretty-printed JSON string.
# Start typing 'def format_users_to_json(users):' and see the magic.
