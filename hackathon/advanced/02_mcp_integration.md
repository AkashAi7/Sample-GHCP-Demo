# 🔴 Advanced Challenge 2: MCP Integration

**Difficulty**: Advanced  
**Time Estimate**: 120 minutes  
**Skills Practiced**: Model Context Protocol, API development, system integration

---

## 🎯 Challenge Overview

Build a **complete MCP server ecosystem** that extends GitHub Copilot with real-world integrations: databases, weather APIs, utility rate providers, and smart home platforms. Make Copilot truly context-aware of your energy environment.

## 📋 Requirements

### Task 1: MCP Architecture Design (15 min)

Design 4 MCP servers:

1. **Energy Database Server** - SQLite/PostgreSQL access
2. **Weather API Server** - OpenWeatherMap integration
3. **Utility Rate Server** - Dynamic pricing data
4. **Smart Home Hub Server** - Device control and status

Create `mcp/ARCHITECTURE.md` documenting:
- Server responsibilities
- Data models
- API contracts
- Security considerations

### Task 2: Implement Energy Database MCP Server (30 min)

Create `mcp/servers/energy_database.py`:

```python
from mcp.server import Server
from mcp.types import Tool, Resource, TextContent
import sqlite3
from typing import Any

app = Server("energy-database")

@app.list_resources()
async def list_resources() -> list[Resource]:
    """List available database tables and views."""
    return [
        Resource(
            uri="sqlite://devices",
            name="Devices Table",
            description="Smart home devices"
        ),
        Resource(
            uri="sqlite://readings",
            name="Readings Table",  
            description="Energy consumption readings"
        ),
        Resource(
            uri="sqlite://analytics_view",
            name="Analytics View",
            description="Pre-computed analytics"
        )
    ]

@app.list_tools()
async def list_tools() -> list[Tool]:
    """Define available database operations."""
    return [
        Tool(
            name="query_readings",
            description="Query energy readings with filters",
            inputSchema={
                "type": "object",
                "properties": {
                    "device_id": {"type": "string"},
                    "start_date": {"type": "string"},
                    "end_date": {"type": "string"},
                    "limit": {"type": "integer", "default": 100}
                }
            }
        ),
        Tool(
            name="aggregate_consumption",
            description="Aggregate consumption by time period",
            inputSchema={
                "type": "object",
                "properties": {
                    "device_id": {"type": "string"},
                    "period": {"type": "string", "enum": ["hour", "day", "week", "month"]}
                },
                "required": ["period"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Execute database queries."""
    if name == "query_readings":
        # Implementation
        results = query_database(arguments)
        return [TextContent(type="text", text=format_results(results))]
    # ... other tools
```

**Requirements**:
- Connection pooling
- SQL injection prevention
- Query result caching
- Error handling

### Task 3: Implement Weather API MCP Server (25 min)

Create `mcp/servers/weather_api.py`:

Features:
- Current weather conditions
- Historical weather data
- Forecast retrieval
- Weather alerts
- Temperature correlation with energy use

**API**: Use OpenWeatherMap (free tier)

### Task 4: Implement Utility Rate MCP Server (20 min)

Create `mcp/servers/utility_rates.py`:

Features:
- Time-of-use rate lookup
- Peak/off-peak detection
- Rate schedule management
- Cost calculation tools
- Rate comparison across utilities

**Data**: Support multiple utility providers

### Task 5: Implement Smart Home Hub MCP Server (25 min)

Create `mcp/servers/smarthome_hub.py`:

Features:
- Device status queries
- Device control (mock or real)
- Scene/automation triggers
- Energy mode switching
- Device grouping

**Integration**: Support Home Assistant, SmartThings, or mock API

### Task 6: MCP Configuration (5 min)

Create `.copilot/mcp-config.json`:

```json
{
  "mcpServers": {
    "energy-db": {
      "command": "python",
      "args": ["mcp/servers/energy_database.py"],
      "env": {
        "DATABASE_PATH": "${workspaceFolder}/data/energy.db"
      }
    },
    "weather": {
      "command": "python",
      "args": ["mcp/servers/weather_api.py"],
      "env": {
        "WEATHER_API_KEY": "${env:OPENWEATHER_API_KEY}"
      }
    },
    "utility-rates": {
      "command": "python",
      "args": ["mcp/servers/utility_rates.py"],
      "env": {
        "RATE_DATA_PATH": "${workspaceFolder}/data/rates.json"
      }
    },
    "smarthome": {
      "command": "python",
      "args": ["mcp/servers/smarthome_hub.py"],
      "env": {
        "HUB_URL": "${env:SMARTHOME_HUB_URL}",
        "HUB_TOKEN": "${env:SMARTHOME_HUB_TOKEN}"
      }
    }
  }
}
```

---

## ✅ Success Criteria

- [ ] 4 MCP servers fully implemented
- [ ] All servers follow MCP specification
- [ ] Copilot can query all data sources
- [ ] Error handling and validation
- [ ] Security best practices (API keys, SQL injection)
- [ ] Comprehensive documentation
- [ ] Demonstrated multi-MCP workflows

---

## 💡 Copilot Tips

- **Design MCP**: `@workspace Help me design an MCP server for weather data`
- **Implement tool**: "Create an MCP tool to query energy readings by date range"
- **Test MCP**: "Using the energy-db MCP, show me all readings from device DEV001"
- **Multi-MCP**: "Using weather and energy-db MCP, correlate temperature with consumption"

---

## 🏆 Bonus Challenges

1. **MCP Monitoring**: Build a dashboard showing MCP server health
2. **MCP Caching Layer**: Implement intelligent caching for API calls
3. **MCP Load Balancing**: Support multiple instances of same MCP server
4. **MCP Security**: Implement authentication and authorization
5. **MCP Testing**: Create comprehensive test suite for MCP servers
6. **MCP Documentation**: Auto-generate API docs from MCP schemas
7. **Real Integration**: Connect to actual smart home devices

---

## 🔍 Evaluation Rubric

| Criteria | Points |
|----------|--------|
| All 4 MCP servers implemented | 40 |
| MCP specification compliance | 20 |
| Security and error handling | 15 |
| Copilot integration working | 15 |
| Documentation | 5 |
| Bonus features | 5 |
| **Total** | **100** |

---

## 📚 Related Exercises

This challenge builds on skills from:
- [Exercise 08: Model Context Protocol](../../exercises/08_model_context_protocol.py)
- Intermediate Challenge 2: API Integration

---

## 🧪 Example: Using MCP with Copilot

```markdown
User: @workspace Analyze the correlation between outdoor temperature and HVAC energy usage for the past week

GitHub Copilot (using MCP):
[Query: weather MCP for past 7 days temperature data]
[Query: energy-db MCP for HVAC readings past 7 days]
[Analyze correlation]

Here's the analysis:

```python
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Data retrieved via MCP servers
weather_data = [
    {"date": "2024-01-25", "temp": 35, "condition": "clear"},
    {"date": "2024-01-26", "temp": 28, "condition": "snow"},
    # ... (retrieved from weather MCP)
]

energy_data = [
    {"timestamp": "2024-01-25 10:00", "device_id": "HVAC001", "value": 3.2},
    {"timestamp": "2024-01-26 10:00", "device_id": "HVAC001", "value": 4.8},
    # ... (retrieved from energy-db MCP)
]

# Correlation analysis
temps = [d['temp'] for d in weather_data]
consumption = [d['value'] for d in energy_data]

correlation, p_value = pearsonr(temps, consumption)

print(f"Correlation: {correlation:.2f}")
print(f"P-value: {p_value:.4f}")
print(f"Interpretation: {'Strong' if abs(correlation) > 0.7 else 'Moderate'} negative correlation")

# Visualization
plt.scatter(temps, consumption)
plt.xlabel('Temperature (°F)')
plt.ylabel('Energy Consumption (kWh)')
plt.title('Temperature vs HVAC Energy Use')
plt.savefig('correlation.png')
```

**Results:**
- Correlation: -0.87 (strong negative correlation)
- P-value: 0.0023 (statistically significant)
- **Interpretation**: As temperature decreases, HVAC energy consumption increases significantly.

**Recommendations** (via @CostOptimizer agent):
- Improve insulation to reduce temperature impact
- Use programmable thermostat during coldest hours
- Projected savings: $45/month with better insulation
```

---

## 📝 Deliverables

1. **4 MCP Server Implementations** (mcp/servers/*.py)
2. **MCP Configuration** (.copilot/mcp-config.json)
3. **ARCHITECTURE.md** - System design
4. **SECURITY.md** - Security considerations and best practices
5. **API_REFERENCE.md** - Complete API documentation for each server
6. **TESTING_GUIDE.md** - How to test MCP servers
7. **EXAMPLES.md** - 20+ usage examples with Copilot

---

## 🔒 Security Checklist

- [ ] API keys stored in environment variables
- [ ] SQL queries use parameterized statements
- [ ] Input validation on all MCP tools
- [ ] Rate limiting on API calls
- [ ] Error messages don't expose sensitive data
- [ ] Audit logging for all MCP calls
- [ ] HTTPS for external API calls

---

**Good luck integrating! Make Copilot omniscient! 🔌🌐**
