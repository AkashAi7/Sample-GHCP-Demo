# 🟡 Intermediate Challenge 2: API Integration

**Difficulty**: Intermediate  
**Time Estimate**: 75 minutes  
**Skills Practiced**: `@workspace`, API design, error handling, testing

---

## 🎯 Challenge Overview

Add a **RESTful API** to the Smart Home Energy Monitor using FastAPI, enabling external systems to query device data and analytics. Use GitHub Copilot to build the entire API layer.

## 📋 Requirements

### Task 1: Setup FastAPI (10 min)
1. Create `api/` directory
2. Create `api/main.py` with FastAPI app
3. Add dependencies to `requirements.txt`:
   - fastapi
   - uvicorn[standard]
   - pydantic

### Task 2: Implement Endpoints (40 min)

#### Endpoint 1: GET /devices
- Returns list of all devices
- Optional query param: `device_type` filter
- Response: `List[DeviceSchema]`

#### Endpoint 2: GET /devices/{device_id}
- Returns single device by ID
- 404 if not found
- Response: `DeviceSchema`

#### Endpoint 3: GET /devices/{device_id}/readings
- Returns readings for a device
- Query params: `start_date`, `end_date`, `limit`
- Response: `List[ReadingSchema]`

#### Endpoint 4: POST /devices/{device_id}/readings
- Add new reading for a device
- Request body: `ReadingCreate`
- Validation: device exists, value is positive
- Response: Created reading with 201 status

#### Endpoint 5: GET /analytics/efficiency
- Calculate efficiency score for a device
- Query params: `device_id`, `start_date`, `end_date`
- Response: `EfficiencySchema` with score and details

#### Endpoint 6: GET /analytics/cost-projection
- Project monthly cost for a device
- Query params: `device_id`, `rate_per_kwh`
- Response: `CostProjectionSchema`

### Task 3: Pydantic Schemas (10 min)
Create `api/schemas.py` with:
- `DeviceSchema`
- `ReadingSchema`
- `ReadingCreate`
- `EfficiencySchema`
- `CostProjectionSchema`

### Task 4: Error Handling (10 min)
Implement proper error responses:
- 400 Bad Request (invalid input)
- 404 Not Found (device doesn't exist)
- 422 Unprocessable Entity (validation errors)
- 500 Internal Server Error (unexpected errors)

### Task 5: API Documentation (5 min)
- Add docstrings to all endpoints
- Add example responses
- Add tags for API organization
- Test Swagger UI at `/docs`

---

## ✅ Success Criteria

- [ ] All 6 endpoints implemented and working
- [ ] Pydantic schemas with validation
- [ ] Proper HTTP status codes
- [ ] Error handling for edge cases
- [ ] API documentation via Swagger
- [ ] Created `API_GUIDE.md` with usage examples

---

## 💡 Copilot Tips

- **Generate endpoint**: "Create a FastAPI endpoint to get all devices"
- **Pydantic schema**: "Create a Pydantic schema for Device model"
- **Error handling**: "Add error handling for device not found"
- **Full API**: `@workspace Create a complete FastAPI app for this project`

---

## 🏆 Bonus Challenges

1. **Authentication**: Add JWT token authentication
2. **Rate Limiting**: Implement rate limiting with slowapi
3. **Pagination**: Add cursor-based pagination to list endpoints
4. **CORS**: Configure CORS for frontend integration
5. **Database**: Replace in-memory data with SQLAlchemy + PostgreSQL
6. **Testing**: Create API tests with TestClient
7. **Docker**: Containerize the API

---

## 🔍 Evaluation Rubric

| Criteria | Points |
|----------|--------|
| All endpoints implemented | 40 |
| Pydantic validation working | 20 |
| Error handling comprehensive | 15 |
| API documentation complete | 10 |
| Code quality and structure | 10 |
| Bonus features | 5 |
| **Total** | **100** |

---

## 📚 Related Exercises

This challenge builds on skills from:
- [Exercise 03: Regex and Data Transform](../../exercises/03_regex_and_data_transform.py)
- [Exercise 04: Refactoring](../../exercises/04_refactoring_and_modernization.py)

---

## 🧪 Example: API Endpoint

```python
from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from api.schemas import DeviceSchema, ReadingSchema
from services.data_ingestion import DataIngestionService

app = FastAPI(title="Smart Home Energy API", version="1.0.0")

@app.get("/devices/{device_id}", response_model=DeviceSchema)
async def get_device(device_id: str):
    """
    Get a single device by ID.
    
    Args:
        device_id: Unique device identifier
        
    Returns:
        Device details
        
    Raises:
        HTTPException: 404 if device not found
    """
    device = device_service.get_by_id(device_id)
    if not device:
        raise HTTPException(status_code=404, detail=f"Device {device_id} not found")
    return device

@app.get("/analytics/efficiency")
async def calculate_efficiency(
    device_id: str = Query(..., description="Device ID"),
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
):
    """Calculate efficiency score for a device over a time period."""
    # Implementation with Copilot
    pass
```

---

## 📝 API_GUIDE.md Template

```markdown
# Smart Home Energy API Guide

## Base URL
```
http://localhost:8000
```

## Authentication
Currently no authentication required (add for production!)

## Endpoints

### Get All Devices
```bash
GET /devices
GET /devices?device_type=HVAC
```

**Response**:
```json
[
  {
    "id": "DEV001",
    "name": "Smart Thermostat",
    "device_type": "HVAC"
  }
]
```

### Calculate Efficiency
```bash
GET /analytics/efficiency?device_id=DEV001&start_date=2024-01-01
```

**Response**:
```json
{
  "device_id": "DEV001",
  "efficiency_score": 87.5,
  "measurement_period": "2024-01-01 to 2024-01-31"
}
```

## Error Responses
```json
{
  "detail": "Device DEV999 not found"
}
```

## Running the API
```bash
uvicorn api.main:app --reload
```

Visit http://localhost:8000/docs for interactive API documentation.
```

---

**Good luck building your API! May your endpoints be RESTful and your responses be swift! 🚀**
