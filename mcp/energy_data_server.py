#!/usr/bin/env python3
"""
Simple MCP Server for Energy Data
==================================

This is a basic Model Context Protocol server that provides access to 
the Smart Home Energy Monitor data. It's designed to be easy to set up
and use for learning purposes.

No complex dependencies - just Python standard library!
"""

import json
import sys
import csv
from pathlib import Path
from typing import Any

# Simple MCP Server Implementation (no external dependencies!)
class SimpleMCPServer:
    def __init__(self, name: str):
        self.name = name
        self.tools = []
        
    def handle_request(self, request: dict) -> dict:
        """Handle MCP protocol requests"""
        method = request.get("method")
        
        if method == "initialize":
            return {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": self.name,
                    "version": "1.0.0"
                }
            }
        
        elif method == "tools/list":
            return {"tools": self.tools}
        
        elif method == "tools/call":
            tool_name = request["params"]["name"]
            arguments = request["params"].get("arguments", {})
            return self.call_tool(tool_name, arguments)
        
        return {"error": "Unknown method"}
    
    def call_tool(self, name: str, args: dict) -> dict:
        """Execute a tool and return results"""
        if name == "get_devices":
            return self.get_devices()
        elif name == "get_readings":
            return self.get_readings(args.get("limit", 10))
        elif name == "get_device_summary":
            return self.get_device_summary(args.get("device_id"))
        elif name == "search_data":
            return self.search_data(args.get("query", ""))
        
        return {"error": f"Unknown tool: {name}"}
    
    def get_devices(self) -> dict:
        """Get list of all devices from the models"""
        # Simple hardcoded device data for demo
        devices = [
            {"id": "DEV001", "name": "Smart Thermostat", "type": "HVAC"},
            {"id": "DEV002", "name": "Living Room Lights", "type": "Lighting"},
            {"id": "DEV003", "name": "Kitchen Refrigerator", "type": "Appliance"},
            {"id": "DEV004", "name": "Water Heater", "type": "HVAC"},
            {"id": "DEV005", "name": "Bedroom AC", "type": "HVAC"}
        ]
        
        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(devices, indent=2)
                }
            ]
        }
    
    def get_readings(self, limit: int = 10) -> dict:
        """Get recent energy readings from CSV"""
        csv_path = Path(__file__).parent.parent / "data" / "readings.csv"
        
        readings = []
        try:
            with open(csv_path, 'r') as f:
                reader = csv.DictReader(f)
                for i, row in enumerate(reader):
                    if i >= limit:
                        break
                    readings.append(row)
        except FileNotFoundError:
            return {
                "content": [{
                    "type": "text",
                    "text": "Sample readings:\n" + json.dumps([
                        {"device_id": "DEV001", "timestamp": "2024-01-01 10:00", "value": "2.5"},
                        {"device_id": "DEV002", "timestamp": "2024-01-01 10:00", "value": "0.8"},
                        {"device_id": "DEV003", "timestamp": "2024-01-01 10:00", "value": "1.2"}
                    ], indent=2)
                }]
            }
        
        return {
            "content": [{
                "type": "text",
                "text": f"Latest {len(readings)} readings:\n" + json.dumps(readings, indent=2)
            }]
        }
    
    def get_device_summary(self, device_id: str = None) -> dict:
        """Get summary information for a device"""
        if not device_id:
            return {
                "content": [{
                    "type": "text",
                    "text": "Please provide a device_id parameter"
                }]
            }
        
        summary = {
            "device_id": device_id,
            "status": "active",
            "avg_consumption": "2.3 kWh",
            "efficiency_score": 85,
            "last_reading": "2024-01-15 14:30"
        }
        
        return {
            "content": [{
                "type": "text",
                "text": f"Device Summary for {device_id}:\n" + json.dumps(summary, indent=2)
            }]
        }
    
    def search_data(self, query: str) -> dict:
        """Search through energy data"""
        results = f"Search results for: '{query}'\n\n"
        
        if "hvac" in query.lower() or "thermostat" in query.lower():
            results += "Found HVAC devices:\n"
            results += "- DEV001: Smart Thermostat (avg: 3.2 kWh)\n"
            results += "- DEV004: Water Heater (avg: 4.5 kWh)\n"
            results += "- DEV005: Bedroom AC (avg: 2.8 kWh)\n"
        elif "high" in query.lower() or "consumption" in query.lower():
            results += "Devices with high consumption:\n"
            results += "- DEV004: Water Heater (4.5 kWh - highest)\n"
            results += "- DEV001: Smart Thermostat (3.2 kWh)\n"
        else:
            results += "Try searching for: 'HVAC', 'high consumption', 'efficiency'\n"
        
        return {
            "content": [{
                "type": "text",
                "text": results
            }]
        }


# Define available tools
def create_energy_server():
    server = SimpleMCPServer("energy-data")
    
    server.tools = [
        {
            "name": "get_devices",
            "description": "Get a list of all smart home devices",
            "inputSchema": {
                "type": "object",
                "properties": {},
                "required": []
            }
        },
        {
            "name": "get_readings",
            "description": "Get recent energy readings from devices",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "number",
                        "description": "Number of readings to return (default: 10)"
                    }
                },
                "required": []
            }
        },
        {
            "name": "get_device_summary",
            "description": "Get summary statistics for a specific device",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "device_id": {
                        "type": "string",
                        "description": "The device ID (e.g., DEV001)"
                    }
                },
                "required": ["device_id"]
            }
        },
        {
            "name": "search_data",
            "description": "Search through energy data and devices",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query (e.g., 'HVAC', 'high consumption')"
                    }
                },
                "required": ["query"]
            }
        }
    ]
    
    return server


def main():
    """Main MCP server loop"""
    server = create_energy_server()
    
    print("Energy Data MCP Server started", file=sys.stderr)
    print("Available tools: get_devices, get_readings, get_device_summary, search_data", file=sys.stderr)
    
    # Simple stdio-based MCP protocol
    for line in sys.stdin:
        try:
            request = json.loads(line)
            response = server.handle_request(request)
            print(json.dumps(response))
            sys.stdout.flush()
        except json.JSONDecodeError:
            error = {"error": "Invalid JSON"}
            print(json.dumps(error))
            sys.stdout.flush()
        except Exception as e:
            error = {"error": str(e)}
            print(json.dumps(error))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
