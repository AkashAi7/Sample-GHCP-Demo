# 🟢 Beginner Challenge 3: Bug Hunt

**Difficulty**: Beginner  
**Time Estimate**: 30 minutes  
**Skills Practiced**: `/fix`, debugging, error handling

---

## 🎯 Challenge Overview

We've intentionally introduced **10 bugs** into the codebase. Your mission: find and fix them all using GitHub Copilot's debugging capabilities!

## 🐛 The Bugs

### Bug 1: Syntax Error in data_ingestion.py
**Location**: `services/data_ingestion.py`, line ~15  
**Symptom**: Code won't run at all  
**Hint**: Missing colon or parenthesis

### Bug 2: Type Error in analytics.py
**Location**: `services/analytics.py`, efficiency calculation  
**Symptom**: TypeError when dividing  
**Hint**: Mixing strings and numbers

### Bug 3: Logic Error in Budget Check
**Location**: `services/analytics.py`, budget checking  
**Symptom**: Budget alerts trigger incorrectly  
**Hint**: Wrong comparison operator

### Bug 4: IndexError in CSV Parsing
**Location**: `services/data_ingestion.py`, parse method  
**Symptom**: Crashes on certain CSV lines  
**Hint**: Assuming all lines have the same number of columns

### Bug 5: Off-by-One Error
**Location**: `services/analytics.py`, loop iteration  
**Symptom**: Missing the last data point  
**Hint**: Range calculation error

### Bug 6: None Type Error
**Location**: `models/reading.py`, validation  
**Symptom**: AttributeError when value is None  
**Hint**: Missing null check

### Bug 7: Division by Zero
**Location**: `services/analytics.py`, average calculation  
**Symptom**: ZeroDivisionError  
**Hint**: Empty list handling

### Bug 8: File Not Found Handling
**Location**: `services/data_ingestion.py`, file loading  
**Symptom**: Crashes when file doesn't exist  
**Hint**: Missing try-except block

### Bug 9: Incorrect Variable Name
**Location**: `main.py`, variable reference  
**Symptom**: NameError  
**Hint**: Typo in variable name

### Bug 10: Float Precision Issue
**Location**: `services/analytics.py`, cost calculation  
**Symptom**: Costs displayed with 10 decimal places  
**Hint**: Need rounding

---

## 📋 Requirements

### Task 1: Create Buggy Version (5 min)
Use Copilot to help you create these bugs in a new branch:
```bash
git checkout -b bug-hunt-challenge
```

Ask Copilot: "Help me introduce the bugs listed in hackathon/beginner/03_bug_hunt.md"

### Task 2: Find and Fix Bugs (20 min)
1. Use `/fix` to identify and correct each bug
2. Create a new file `BUGFIXES.md` documenting:
   - Bug description
   - Root cause
   - Fix applied
   - How to prevent it in the future

### Task 3: Prevent Future Bugs (5 min)
Add defensive programming:
- Input validation
- Error handling
- Type checking
- Assertions

---

## ✅ Success Criteria

- [ ] All 10 bugs identified and fixed
- [ ] Code runs without errors
- [ ] Created `BUGFIXES.md` with detailed explanations
- [ ] Added error handling to prevent similar bugs
- [ ] Tests pass (if you completed Challenge 2)

---

## 💡 Copilot Tips

- **Identify bugs**: Highlight problematic code + `/fix` in Chat
- **Explain errors**: Copy error message and ask "What's causing this error?"
- **Prevent bugs**: "Add input validation to prevent this error"
- **Error handling**: "Add try-except blocks to handle file errors"

---

## 🏆 Bonus Challenges

1. **Automated Bug Detection**: Set up a linter (pylint/flake8) to catch bugs automatically
2. **Custom Validation**: Create a `validators.py` module for input validation
3. **Logging**: Add proper logging instead of print statements for errors
4. **Type Hints**: Add type hints everywhere to catch type errors early

---

## 🔍 Evaluation Rubric

| Criteria | Points |
|----------|--------|
| All bugs fixed correctly | 50 |
| BUGFIXES.md documentation | 20 |
| Added error handling | 20 |
| Bonus improvements | 10 |
| **Total** | **100** |

---

## 📚 Related Exercises

This challenge builds on skills from:
- [Exercise 05: Debugging with Fix](../../exercises/05_debugging_with_fix.py)

---

## 🧪 Testing Your Fixes

After fixing the bugs, verify with:

```bash
# Run the main application
python main.py

# Run tests (if you completed Challenge 2)
pytest

# Run with edge cases
python -c "from services.analytics import EnergyAnalytics; print(EnergyAnalytics().calculate_efficiency([], []))"
```

---

## 📝 Example BUGFIXES.md Entry

```markdown
### Bug 3: Logic Error in Budget Check

**Description**: Budget alerts trigger even when costs are below budget

**Root Cause**: Used `>` instead of `>=` in budget comparison at line 45

**Fix Applied**:
```python
# Before
if projected_cost > budget:
    
# After
if projected_cost >= budget:
```

**Prevention**: Add unit tests for boundary conditions (equal values)
```

---

**Good luck hunting! 🐛🔍 Every bug you fix makes you a better developer!**
