# 🟢 Beginner Challenge 2: Test Coverage Blitz

**Difficulty**: Beginner  
**Time Estimate**: 45 minutes  
**Skills Practiced**: `/tests`, unit testing, pytest

---

## 🎯 Challenge Overview

The Smart Home Energy Monitor has **0% test coverage**. Your goal is to achieve **80%+ coverage** using GitHub Copilot's test generation capabilities.

## 📋 Requirements

### Task 1: Setup Testing Infrastructure (5 min)
1. Create `tests/` directory
2. Create `tests/conftest.py` with pytest fixtures for:
   - Sample Device objects
   - Sample Reading objects
   - Sample CSV data
3. Create `requirements-test.txt` with pytest and coverage tools

### Task 2: Test Data Models (15 min)
Create `tests/test_models.py` with comprehensive tests for:

**Device Model Tests**:
- Creating valid devices
- Device validation (invalid IDs, names)
- Device string representation
- Edge cases (empty strings, special characters)

**Reading Model Tests**:
- Creating valid readings
- Timestamp validation
- Value ranges (negative values, extreme values)
- Data type validation

### Task 3: Test Services (20 min)
Create `tests/test_services.py` with tests for:

**DataIngestionService**:
- Loading valid CSV files
- Handling missing files
- Parsing malformed CSV data
- Empty file handling

**EnergyAnalytics**:
- Efficiency score calculations
- Edge cases (zero values, very large numbers)
- Monthly cost projections
- Budget checking logic

### Task 4: Run Coverage Report (5 min)
1. Run tests with coverage: `pytest --cov=. --cov-report=html`
2. Aim for **80%+ coverage**
3. Create `TESTING.md` documenting how to run tests

---

## ✅ Success Criteria

- [ ] Tests pass with pytest
- [ ] Achieve 80%+ code coverage
- [ ] All edge cases are tested
- [ ] Tests are well-organized with clear names
- [ ] Fixtures are reused effectively
- [ ] Created `TESTING.md` with instructions

---

## 💡 Copilot Tips

- **Generate tests**: Highlight a function/class + type `/tests` in Chat
- **Test specific scenarios**: "Generate tests for edge cases in calculate_efficiency"
- **Fixtures**: "Create pytest fixtures for Device and Reading objects"
- **Coverage gaps**: "What tests are missing for 100% coverage of analytics.py?"

---

## 🏆 Bonus Challenges

1. **Parametrized Tests**: Use `@pytest.mark.parametrize` for testing multiple inputs
2. **Mock External Dependencies**: If you add file I/O or API calls, mock them properly
3. **Property-Based Testing**: Use `hypothesis` library for property-based tests
4. **CI Integration**: Create a GitHub Actions workflow to run tests automatically

---

## 🔍 Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Test coverage >= 80% | 40 |
| All edge cases covered | 25 |
| Tests are well-structured | 20 |
| Documentation (TESTING.md) | 10 |
| Bonus challenges | 5 |
| **Total** | **100** |

---

## 📚 Related Exercises

This challenge builds on skills from:
- [Exercise 02: Unit Testing](../../exercises/02_unit_testing.py)

---

## 🧪 Example Test Structure

```python
import pytest
from models.device import Device
from models.reading import Reading
from services.analytics import EnergyAnalytics

@pytest.fixture
def sample_device():
    """Fixture providing a standard test device."""
    return Device(id="DEV001", name="Smart Thermostat", device_type="HVAC")

@pytest.fixture
def sample_readings(sample_device):
    """Fixture providing sample energy readings."""
    return [
        Reading(device_id=sample_device.id, timestamp="2024-01-01 10:00", value=2.5),
        Reading(device_id=sample_device.id, timestamp="2024-01-01 11:00", value=3.1),
    ]

def test_efficiency_score_normal_case(sample_device, sample_readings):
    """Test efficiency calculation with normal input values."""
    analytics = EnergyAnalytics()
    score = analytics.calculate_efficiency(sample_device, sample_readings)
    assert 0 <= score <= 100
    assert isinstance(score, float)
```

---

**Good luck! May your tests be green and your coverage be high! 🧪✅**
