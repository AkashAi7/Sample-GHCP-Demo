# Exercise 8: Model Context Protocol (MCP) - Introduction
# Feature: Understanding How to Extend GitHub Copilot

"""
Model Context Protocol (MCP) allows GitHub Copilot to connect to external data.

Think of it as giving Copilot access to:
- Public APIs (weather, news, GitHub, etc.)
- Your local files
- Databases
- Custom tools

This exercise helps you UNDERSTAND MCP with simple examples.
You don't need to set anything up to learn!
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PART 1: What is MCP? (Understanding - No Setup Required!)
# ═══════════════════════════════════════════════════════════════════════════════

# TASK 1: Learn about MCP
# Open Copilot Chat and ask:
# "What is Model Context Protocol and how does it help GitHub Copilot?"

# Expected answer will explain:
# - MCP connects Copilot to external data
# - Makes Copilot aware of your databases, APIs, docs
# - Allows Copilot to answer questions using real data
# - Extends Copilot beyond just code files


# TASK 2: Understand the benefits
# Ask Chat: "What are 5 practical examples where MCP would be useful in development?"

# Examples you might hear:
# ✅ Query your database to understand the schema
# ✅ Check API documentation for endpoint details
# ✅ Access company internal documentation
# ✅ Get real-time data for testing code
# ✅ Validate against production configurations


# ═══════════════════════════════════════════════════════════════════════════════
# PART 2: See MCP in Action (Conceptual Examples)
# ═══════════════════════════════════════════════════════════════════════════════

# TASK 3: Imagine you have MCP configured for a database
# Ask Copilot Chat:
# "If I had an MCP server connected to my energy database, 
# how would I ask Copilot to query it?"

# Example response you'd use:
# "Show me all devices from the database that have readings above 5 kWh"
# "What's the average energy consumption per device type from the database?"


# TASK 4: Conceptual API integration
# Ask Chat:
# "If I set up an MCP server for a weather API, 
# give me an example of how Copilot could use it in my code"

# Copilot might show you:
"""
# With weather MCP configured, Copilot could help you write:

def analyze_temperature_impact(device_id: str, date: str) -> dict:
    # Copilot would know to use the weather MCP to get temperature
    temperature = get_temperature_from_mcp(date)  # Uses weather MCP
    
    # Then use the database MCP to get device readings
    readings = get_device_readings_from_mcp(device_id, date)  # Uses DB MCP
    
    # Calculate correlation
    return calculate_correlation(temperature, readings)
"""


# ═══════════════════════════════════════════════════════════════════════════════
# PART 3: What MCP Can Do (Examples)
# ═══════════════════════════════════════════════════════════════════════════════

# TASK 5: Understand MCP capabilities
# Ask Copilot: "Show me 3 examples of what MCP can do"

# Example 1: Access local files
# MCP can help Copilot read your project files
# "What files are in my models/ directory?"
# "Read the README and summarize the project"

# Example 2: Query databases
# MCP can connect to databases
# "How many devices are in the database?"
# "Show me readings from yesterday"

# Example 3: Call public APIs
# MCP can fetch data from the internet
# "Get current weather data"
# "Search GitHub for Python examples"


# TASK 6: See a simple MCP configuration example
# This is what MCP configuration looks like (just for learning - don't set up yet):

"""
Example MCP config (in VS Code settings):
{
  "github.copilot.chat.mcp.servers": {
    "my-files": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}

Then you can ask Copilot:
"Using my-files, what Python files exist?"
"""


# ═══════════════════════════════════════════════════════════════════════════════
# PART 4: Try Public MCP Servers! (Zero Setup Options)
# ═══════════════════════════════════════════════════════════════════════════════

# 🎁 OPTION 1: Fetch MCP - Access Public APIs (Easiest - No API Key!)

# TASK 7: Set up Fetch MCP (30 seconds!)
# 
# Add this to your VS Code User Settings (settings.json):
"""
{
  "github.copilot.chat.mcp.servers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    }
  }
}
"""
#
# Reload VS Code → You're done!


# TASK 8: Try these public API queries (after setup)
# Once configured, ask Copilot Chat:

# Weather (public API - no key needed):
# "Using fetch MCP, get weather for London from wttr.in/London?format=j1"
# "Fetch weather data and create a Python function to parse it"

# GitHub public API:
# "Using fetch MCP, get details about the Python repository from api.github.com"
# "Fetch trending repos and create a summary"

# Jokes API:
# "Using fetch MCP, get a random joke from official-joke-api.appspot.com/random_joke"

# Country data:
# "Fetch country information from restcountries.com/v3.1/name/france"


# 🎁 OPTION 2: Filesystem MCP - Your Local Files (Also No Setup!)

# TASK 9: Try Filesystem MCP
# Add this config:
"""
{(Optional) Try MCP Yourself
# ═══════════════════════════════════════════════════════════════════════════════

# Want to try MCP? Here's the SIMPLEST way:

# TASK 7: Optional - Set up one simple MCP server
# 
# Ask Copilot Chat to help you:
# "Help me set up the filesystem MCP server to access files in this workspace"
#
# Copilot will guide you through:
# 1. Adding config to VS Code settings
# 2. Reloading VS Code
# 3. Trying your first MCP query
#
# That's it! Copilot does the heavy lifting.


# TASK 8: If you set up MCP, try these questions
# Once configured, ask Copilot Chat:

# "What files are in the models/ directory?"
# "Read the data/readings.csv file"
# "Show me all Python files in this project"


# TASK 9: Understand when to use MCP
# Ask Chat: "When should I use MCP vs just writing regular code?"

# MCP is great for:
# ✅ Getting data while you code
# ✅ Exploring unfamiliar codebases
# ✅ Quick prototypes with real data

# Regular code is better for:
# ✅ Production applications
# ✅ Performance-critical code
# ✅ Complex business logic


# TASK 10: Learn more
# Ask Copilot: "What are some cool things I could build with MCP?data
✅ Fetch MCP = access ANY public API with zero setup!
✅ Filesystem MCP = access your local files
✅ Brave Search MCP = web search (free API key)
✅ Just add config to VS Code settings and reload
✅ Ask Copilot questions and it fetches real data!

💡 EASIEST START (30 seconds): 
   1. Copy the Fetch MCP config from TASK 7
   2. Add to VS Code User Settings (settings.json)
   3. Reload VS Code
   4. Ask: "Using fetch MCP, get weather from wttr.in/Paris?format=j1"
   
🎁 FREE PUBLIC MCP SERVERS:
   - @modelcontextprotocol/server-fetch (ANY public API!)
   - @modelcontextprotocol/server-filesystem (local files)
   - @modelcontextprotocol/server-brave-search (web search)
   - @modelcontextprotocol/server-github (GitHub repos)
   
🌐 PUBLIC APIs YOU CAN TRY:
   - wttr.in - Weather data
   - api.github.com - GitHub public data
   - restcountries.com - Country information
   - official-joke-api.appspot.com - Random jokes
   - Any public REST API!
   
🚀 NEXT STEPS:
   - Try Fetch MCP with public APIs (recommended!)
   - Get free Brave API key for web search
   - Move to Exercise 09 to learn about Custom Agents
   - Tackle Advanced Hackathon Challenge 2 to build custom MCP servers

Next Exercise: 09_building_custom_agents.py - Create specialized AI assistants!
"""
lets Copilot access external data (APIs, files, databases)
✅ You don't need to set it up to understand the concept
✅ If you want to try: ask Copilot to help you set up filesystem MCP
✅ Building complex MCP servers → Advanced Hackathon Challenge

💡 KEY IDEA: 
   MCP = giving Copilot access to data beyond your code files
   
🚀 NEXT STEPS:
   - Optionally try MCP setup (ask Copilot for help!)
   - Move to Exercise 09 to learn about Custom Agents
   - For advanced MCP: see Hackathon Challenge 2