# Exercise 7: Advanced Configuration (Custom Instructions & Agents)
# Feature: .github/copilot-instructions.md and Custom Agents (.agent.md)

# GitHub Copilot can be customized for your specific repository needs.

# TASK 1: Discover Custom Instructions.
# We have added custom instructions in `.github/copilot-instructions.md`.
# These instructions tell Copilot to ALWAYS use type hints and f-strings.

# Test it:
# 1. Open a new line below.
# 2. Start typing a function 'def calculate_total(price, tax):'
# 3. See if Copilot suggests type hints automatically (e.g., 'price: float, tax: float) -> float:').

def calculate_total(price, tax):
    # Copilot should suggest the body with an f-string print due to our custom instructions.
    pass

# TASK 2: Use a Custom Agent.
# We have defined a custom agent called '@GitExpert' in `.github/agents/GitExpert.agent.md`.
# This agent knows our specific git conventions.

# Test it:
# 1. Open GitHub Copilot Chat (Ctrl+Alt+I).
# 2. Type '@GitExpert how should I format my commit message for adding this exercise?'
# 3. Observe how it responds based on the goals defined in the .agent.md file.

# TASK 3: Verify Architectural Rules.
# Our instructions say logic belongs in `services/`.
# Ask Chat: "Where should I add a new logic for calculating peak energy hours?"
# Observe if it correctly points to the `services/` folder.
