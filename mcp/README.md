# MCP Servers for Smart Home Energy Monitor

This directory contains **ready-to-use MCP servers** for learning Model Context Protocol with GitHub Copilot.

---

## 📦 Available MCP Servers

### 1. Energy Data Server (`energy_data_server.py`)

A simple MCP server that provides access to Smart Home Energy Monitor data.

**Tools Available**:
- `get_devices` - List all smart home devices
- `get_readings` - Get recent energy readings
- `get_device_summary` - Get stats for a specific device
- `search_data` - Search through energy data

**No dependencies required!** Uses only Python standard library.

---

## 🚀 Quick Setup (2 minutes!)

### Step 1: Configure MCP in VS Code

Create or edit your VS Code settings file:

**Windows**: `%APPDATA%\Code\User\settings.json`  
**Mac/Linux**: `~/.config/Code/User/settings.json`

Add this configuration:

```json
{
  "github.copilot.chat.mcp.servers": {
    "energy-data": {
      "command": "python",
      "args": ["mcp/energy_data_server.py"],
      "cwd": "${workspaceFolder}"
    }
  }
}
```

### Step 2: Reload VS Code

Press `Ctrl+Shift+P` (Cmd+Shift+P on Mac) → Type "Reload Window" → Press Enter

### Step 3: Test It!

Open GitHub Copilot Chat and try:

```
Using the energy-data MCP, show me all devices
```

or

```
Get the summary for device DEV001 using MCP
```

---

## 💡 Example Queries

Once configured, ask Copilot Chat:

### Get Device List
```
"Show me all the smart home devices using the energy-data server"
```

### Check Energy Readings
```
"Get the latest 5 energy readings"
```

### Device Summary
```
"What's the summary for device DEV001?"
```

### Search Functionality
```
"Search for HVAC devices in the energy data"
```

### Use in Code Generation
```
"Write a function that uses the MCP server to get all devices 
and filter for HVAC types with consumption above 3 kWh"
```

---

## 🔧 Troubleshooting

### MCP Server Not Found
- Make sure you're in the correct workspace folder
- Check that the path to `energy_data_server.py` is correct
- Verify Python is in your PATH: `python --version`

### No Response from MCP
- Reload VS Code window
- Check VS Code Developer Tools (Help → Toggle Developer Tools) for errors
- Try restarting VS Code completely

### Python Version
- Requires Python 3.7+
- Check version: `python --version`

---

## 📚 What's Happening Under the Hood?

1. **VS Code starts the MCP server** when Copilot needs it
2. **Copilot sends requests** to the server via JSON
3. **Server responds** with data from your energy monitor
4. **Copilot uses the data** to answer your questions or generate code

---

## 🎯 Learning Exercises

Try these progressively harder tasks:

### Beginner
1. List all devices
2. Get recent readings
3. Get summary for one device

### Intermediate
4. Ask Copilot to create a chart of device consumption
5. Generate code that uses multiple MCP tools
6. Have Copilot explain the data patterns

### Advanced
7. Ask Copilot to create a dashboard using MCP data
8. Generate analytics code that queries MCP in real-time
9. Create automated alerts using MCP data

---

## 🔒 Security Note

This is a **learning/demo server** with hardcoded data. For production:
- ✅ Add authentication
- ✅ Validate all inputs
- ✅ Use proper database connections
- ✅ Add rate limiting
- ✅ Log all access

---

## 🚀 Next Steps

1. **Try the basic setup** to understand MCP
2. **Complete Exercise 08** to learn MCP concepts
3. **Attempt Advanced Hackathon Challenge 2** to build your own MCP servers

---

**Happy learning! 🎉**
