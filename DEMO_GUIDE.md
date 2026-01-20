# GitHub Copilot Demo Guide: Smart Home Energy Monitor

This guide demonstrates the 4 key modes of GitHub Copilot: **Ask**, **Plan**, **Edit**, and **Agent** using a multi-file Python project.

## Project Structure
- `main.py`: Entry point (currently incomplete).
- `models/`: Data classes for Devices and Readings.
- `services/analytics.py`: Complex math logic.
- `services/data_ingestion.py`: Data parsing logic (contains bugs).
- `data/readings.csv`: Sample data.

---

## 1. Ask Mode (Chat)
**Goal:** Understand complex logic in a specific file.

1. Open `services/analytics.py`.
2. Highlight the `calculate_complex_efficiency_score` method.
3. Open **Copilot Chat** (Ctrl+Alt+I / Cmd+Opt+I).
4. Type: `Explain the mathematical formula used in this efficiency calculation.`
5. **Observe:** Copilot breaks down the use of `acos`, `sin`, and `exp` to explain the heuristic.

---

## 2. Plan Mode (Copilot Edits)
**Goal:** Architect a new feature across the project.

1. In the Chat panel, switch to **Copilot Edits** (Ctrl+Shift+I / Cmd+Shift+I).
2. Type: `Plan a new feature to alert the user if the projected monthly cost exceeds a budget.`
3. **Observe:** Copilot outlines a plan:
    - Update `EnergyAnalytics` to implement `project_monthly_cost`.
    - Create a new `AlertService`.
    - Update `main.py` to check the cost against a threshold.

---

## 3. Edit Mode (Inline Chat)
**Goal:** Fix buggy code and refactor in-place.

1. Open `services/data_ingestion.py`.
2. Notice the `parse_csv_line` method uses simple `split(',')`. This will fail on the last line of `data/readings.csv` which has quotes: `"2023-10-01 09:00:00"`.
3. Highlight the `parse_csv_line` method.
4. Press **Ctrl+I** (Cmd+I) to open Inline Chat.
5. Type: `Refactor this to use the csv module or regex to correctly handle quoted strings in the CSV.`
6. **Observe:** Copilot rewrites the method to be robust.
7. Click **Accept**.

---

## 4. Agent Mode (@workspace)
**Goal:** Implement the main application logic by understanding the relationships between files.

1. Open `main.py`.
2. Open the **Copilot Chat** panel.
3. Type: `@workspace Implement the TODOs in main.py. Load the data using DataIngestionService, run the analytics, and print a formatted report of the efficiency score.`
4. **Observe:** 
    - Copilot scans `services/` to understand the available methods.
    - It generates the code to instantiate the classes, call `load_file`, and pass the data to `analytics`.
    - It adds the print statements.
5. Click **Apply in Editor** to finish the application.

---

## 5. Self-Paced Learning Exercises
For a deeper dive into specific features, explore the `exercises/` folder:
- **Regex & Data**: [03_regex_and_data_transform.py](exercises/03_regex_and_data_transform.py)
- **Refactoring**: [04_refactoring_and_modernization.py](exercises/04_refactoring_and_modernization.py)
- **Debugging**: [05_debugging_with_fix.py](exercises/05_debugging_with_fix.py)
- **CLI/Terminal**: [06_terminal_and_cli.py](exercises/06_terminal_and_cli.py)

---

## Summary
- **Ask**: "What does this complex math do?" (`analytics.py`)
- **Plan**: "How do I add an alert system?" (Architecture)
- **Edit**: "Fix this CSV parser." (`data_ingestion.py`)
- **Agent**: "Wire it all together." (`main.py`)
