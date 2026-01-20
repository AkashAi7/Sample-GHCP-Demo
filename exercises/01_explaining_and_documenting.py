# Exercise 1: Explaining and Documenting Code
# Feature: Copilot Chat, /explain, and Docstring Generation

# TASK 1: Use Copilot to explain what this function does.
# Highlight the function, open Chat (Ctrl+Alt+I), and type "/explain" or ask "What does this do?"

def process_data(vals):
    if not vals: return []
    m = sum(vals) / len(vals)
    s = (sum((x - m) ** 2 for x in vals) / len(vals)) ** 0.5
    return [round((x - m) / s, 2) for x in vals]

# TASK 2: Generate a docstring for the function above.
# Place your cursor inside the function or highlight it, press Ctrl+I (Cmd+I) and type "generate docstring"
# or simply type '"""' and let Copilot autocomplete.

# TASK 3: Use Copilot to document this complex regex.
# Highlight the pattern and ask Chat to explain it.
import re
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

def validate_email(email):
    return re.match(email_pattern, email) is not None
