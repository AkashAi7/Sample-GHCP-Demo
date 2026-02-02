# 🟡 Intermediate Challenge 1: Legacy Code Modernization

**Difficulty**: Intermediate  
**Time Estimate**: 60 minutes  
**Skills Practiced**: Refactoring, type hints, modern Python patterns, `@workspace`

---

## 🎯 Challenge Overview

You've inherited a **legacy Python 2.7 codebase** that needs modernization to Python 3.10+. Use GitHub Copilot to refactor the entire project with modern best practices.

## 📋 Requirements

### Task 1: Type Hints Everywhere (20 min)
Add comprehensive type hints to all functions and classes:
- Function parameters
- Return types
- Class attributes
- Use `from typing import List, Dict, Optional, Union` as needed

**Ask Copilot**: `@workspace Add type hints to all functions in this project`

### Task 2: Modern Python Patterns (20 min)
Refactor old patterns to modern equivalents:

| Old Pattern | Modern Pattern |
|-------------|----------------|
| `for i in range(len(items))` | `for item in items` or `enumerate()` |
| String concatenation with `+` | f-strings |
| `dict.has_key()` | `in` operator |
| Manual file closing | Context managers (`with`) |
| List building with loops | List comprehensions |

### Task 3: Dataclasses and Models (15 min)
Convert plain classes to `@dataclass`:
- Update `models/device.py` to use `@dataclass`
- Update `models/reading.py` to use `@dataclass`
- Add proper type annotations
- Implement `__post_init__` for validation

### Task 4: Async/Await for I/O (Optional, 5 min)
If time permits, refactor I/O operations to use async:
- Make CSV loading async
- Use `aiofiles` for file operations

---

## ✅ Success Criteria

- [ ] 100% of functions have type hints
- [ ] No Python 2.x patterns remain
- [ ] Models use `@dataclass` decorator
- [ ] All file operations use context managers
- [ ] Code passes `mypy` type checking
- [ ] Created `MODERNIZATION.md` documenting changes

---

## 💡 Copilot Tips

- **Add type hints**: Highlight function + Ctrl+I + "add type hints"
- **Refactor loops**: `@workspace Convert all range-based loops to enumerate or direct iteration`
- **Dataclass conversion**: "Convert this class to a dataclass"
- **Type check**: "Run mypy and fix all type errors"

---

## 🏆 Bonus Challenges

1. **Pydantic Models**: Use Pydantic instead of dataclasses for advanced validation
2. **Protocol Classes**: Define protocols for service interfaces
3. **Generic Types**: Use TypeVar and Generic for type-safe containers
4. **Strict MyPy**: Pass `mypy --strict` with zero errors

---

## 🔍 Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Type hints on all functions | 30 |
| Modern Python patterns applied | 30 |
| Dataclasses implemented correctly | 20 |
| Type checking passes | 15 |
| Documentation | 5 |
| **Total** | **100** |

---

## 📚 Related Exercises

This challenge builds on skills from:
- [Exercise 04: Refactoring and Modernization](../../exercises/04_refactoring_and_modernization.py)

---

## 🧪 Example: Before & After

**Before (Legacy)**:
```python
class Device:
    def __init__(self, id, name, device_type):
        self.id = id
        self.name = name
        self.device_type = device_type
    
    def get_info(self):
        return "Device: " + self.name + " (" + self.id + ")"
```

**After (Modern)**:
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Device:
    id: str
    name: str
    device_type: str
    
    def __post_init__(self) -> None:
        if not self.id:
            raise ValueError("Device ID cannot be empty")
    
    def get_info(self) -> str:
        return f"Device: {self.name} ({self.id})"
```

---

## 📝 MODERNIZATION.md Template

```markdown
# Code Modernization Report

## Summary
Modernized codebase from Python 2.7 patterns to Python 3.10+ best practices.

## Changes Applied

### Type Hints
- Added type annotations to X functions
- Added return type hints to Y methods
- Mypy compliance: PASS

### Refactorings
- Converted X loops to list comprehensions
- Replaced Y string concatenations with f-strings
- Updated Z file operations to use context managers

### Data Models
- Converted Device to dataclass
- Converted Reading to dataclass
- Added validation in __post_init__

## Impact
- Improved IDE autocomplete
- Caught N type errors before runtime
- Reduced code by X lines
- Improved readability score by Y%
```

---

**Good luck! Transform this legacy code into modern Python! 🐍✨**
