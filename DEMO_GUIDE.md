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

**Foundations (Exercises 1-4)**:
- [01_explaining_and_documenting.py](exercises/01_explaining_and_documenting.py) - `/explain` and docstring generation
- [02_unit_testing.py](exercises/02_unit_testing.py) - Generate tests with `/tests`
- [03_regex_and_data_transform.py](exercises/03_regex_and_data_transform.py) - Pattern matching and data pipelines
- [04_refactoring_and_modernization.py](exercises/04_refactoring_and_modernization.py) - Modernize code with type hints

**Productivity (Exercises 5-7)**:
- [05_debugging_with_fix.py](exercises/05_debugging_with_fix.py) - Fix bugs with `/fix`
- [06_terminal_and_cli.py](exercises/06_terminal_and_cli.py) - Leverage `@terminal`
- [07_advanced_configuration.py](exercises/07_advanced_configuration.py) - Custom instructions

**Advanced Extensions (Exercises 8-9)**:
- [08_model_context_protocol.py](exercises/08_model_context_protocol.py) - Connect Copilot to databases and APIs
- [09_building_custom_agents.py](exercises/09_building_custom_agents.py) - Create specialized AI assistants

**Capstone Lab (Exercise 10)**:
- [10_end_to_end_sdlc_lab.py](exercises/10_end_to_end_sdlc_lab.py) - Practice an end-to-end SDLC workflow with Copilot

---

## 6. 🏆 Hackathon Challenges

Test your GitHub Copilot mastery with real-world coding challenges! Organized by difficulty and skillset:

### 🟢 Beginner Challenges (Core Features)
Perfect for developers new to GitHub Copilot. Focus on fundamental features like code explanation, testing, and debugging.

1. **[Documentation Sprint](hackathon/beginner/01_documentation_sprint.md)** (30 min)
   - **Skills**: `/explain`, docstring generation, comments
   - **Goal**: Document the entire codebase using Copilot
   - **Challenge**: Achieve comprehensive documentation for all functions and modules

2. **[Test Coverage Blitz](hackathon/beginner/02_test_coverage_blitz.md)** (45 min)
   - **Skills**: `/tests`, pytest, unit testing
   - **Goal**: Achieve 80%+ test coverage from 0%
   - **Challenge**: Generate comprehensive test suites for all services

3. **[Bug Hunt](hackathon/beginner/03_bug_hunt.md)** (30 min)
   - **Skills**: `/fix`, debugging, error handling
   - **Goal**: Find and fix 10 intentional bugs
   - **Challenge**: Use Copilot to identify and correct all bugs

### 🟡 Intermediate Challenges (Multi-File & Architecture)
For developers comfortable with Copilot basics. Focus on refactoring, API design, and performance.

4. **[Legacy Code Modernization](hackathon/intermediate/01_legacy_modernization.md)** (60 min)
   - **Skills**: Refactoring, type hints, modern Python patterns, `@workspace`
   - **Goal**: Modernize Python 2.7 code to Python 3.10+
   - **Challenge**: Apply modern patterns and pass strict type checking

5. **[API Integration](hackathon/intermediate/02_api_integration.md)** (75 min)
   - **Skills**: `@workspace`, API design, FastAPI, Pydantic
   - **Goal**: Build a complete REST API for the energy monitor
   - **Challenge**: Implement 6 endpoints with proper validation and docs

6. **[Performance Optimization](hackathon/intermediate/03_performance_optimization.md)** (60 min)
   - **Skills**: Profiling, optimization, vectorization
   - **Goal**: Achieve 10x performance improvement
   - **Challenge**: Optimize code to handle 100,000+ readings efficiently

### 🔴 Advanced Challenges (Custom Agents & MCP)
For expert developers ready to push Copilot to its limits. Focus on custom agents, MCP integration, and system design.

7. **[Custom Agent Development](hackathon/advanced/01_custom_agent.md)** (90 min)
   - **Skills**: Custom agents, domain modeling, AI orchestration
   - **Goal**: Build 5 specialized agents that work together
   - **Challenge**: Create an agent ecosystem for energy management

8. **[MCP Integration](hackathon/advanced/02_mcp_integration.md)** (120 min)
   - **Skills**: Model Context Protocol, API development, system integration
   - **Goal**: Build 4 MCP servers extending Copilot's capabilities
   - **Challenge**: Connect Copilot to databases, weather APIs, and smart home platforms

9. **[Multi-Agent System](hackathon/advanced/03_multi_agent_system.md)** (150 min)
   - **Skills**: All previous skills combined
   - **Goal**: Build a complete AI-powered energy management platform
   - **Challenge**: Autonomous system with 7 agents, 4 MCP servers, and intelligent workflows

---

### 🎯 Hackathon Skill Matrix

| Challenge | Core Features | Testing | Refactoring | API Design | MCP | Custom Agents | Difficulty |
|-----------|---------------|---------|-------------|------------|-----|---------------|------------|
| Documentation Sprint | ✅✅✅ | | | | | | 🟢 |
| Test Coverage Blitz | ✅ | ✅✅✅ | | | | | 🟢 |
| Bug Hunt | ✅✅ | | | | | | 🟢 |
| Legacy Modernization | ✅ | | ✅✅✅ | | | | 🟡 |
| API Integration | ✅ | ✅ | ✅ | ✅✅✅ | | | 🟡 |
| Performance Optimization | ✅ | | ✅✅ | | | | 🟡 |
| Custom Agent | ✅ | | | | ✅ | ✅✅✅ | 🔴 |
| MCP Integration | ✅ | | | ✅✅ | ✅✅✅ | | 🔴 |
| Multi-Agent System | ✅ | ✅ | ✅ | ✅ | ✅✅ | ✅✅✅ | 🔴 |

---

## Summary
- **Ask**: "What does this complex math do?" (`analytics.py`)
- **Plan**: "How do I add an alert system?" (Architecture)
- **Edit**: "Fix this CSV parser." (`data_ingestion.py`)
- **Agent**: "Wire it all together." (`main.py`)
- **Hackathon**: Test your skills with 9 progressive challenges!
