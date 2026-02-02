# Exercise 9: Building Custom Agents
# Feature: Creating Specialized AI Assistants with .agent.md Files

"""
Custom Agents allow you to create specialized AI assistants tailored to specific domains,
workflows, or team needs. They have:

- Custom instructions and personality
- Specific knowledge domains
- Predefined tools and capabilities
- Focused conversation context

This exercise teaches you how to build and use custom agents effectively.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PART 1: Understanding Custom Agents
# ═══════════════════════════════════════════════════════════════════════════════

# TASK 1: Discover existing custom agents
# Open Copilot Chat and type '@' to see available agents
# You should see '@GitExpert' (defined in .github/agents/GitExpert.agent.md)

# TASK 2: Test the GitExpert agent
# Ask: "@GitExpert How should I format my commit message for this exercise?"
# Observe how it responds based on its custom instructions


# ═══════════════════════════════════════════════════════════════════════════════
# PART 2: Creating Your First Custom Agent
# ═══════════════════════════════════════════════════════════════════════════════

# TASK 3: Create a "TestingExpert" agent
# Ask Copilot to help you:
# "Create a custom agent called TestingExpert in .github/agents/TestingExpert.agent.md
# that specializes in Python testing best practices, pytest, and test coverage"

# Copilot should create a file like:
"""
---
title: TestingExpert
description: Expert in Python testing, pytest, and test coverage strategies
---

You are TestingExpert, a specialized AI assistant focused on Python testing.

## Your Expertise
- pytest framework and fixtures
- Test-driven development (TDD)
- Test coverage analysis
- Mocking and patching
- Integration vs unit testing

## Your Goals
- Help developers write comprehensive test suites
- Suggest edge cases and test scenarios
- Recommend appropriate testing patterns
- Explain testing best practices

## Your Style
- Provide code examples for every recommendation
- Explain *why* a testing approach is beneficial
- Suggest specific pytest plugins when relevant
"""

# TASK 4: Use your TestingExpert agent
# Ask: "@TestingExpert Review the analytics.py service and suggest test cases"
# Observe how it provides focused testing guidance!


# ═══════════════════════════════════════════════════════════════════════════════
# PART 3: Advanced Agent Configuration
# ═══════════════════════════════════════════════════════════════════════════════

# TASK 5: Create a domain-specific agent
# Let's create an "EnergyAnalyticsAgent" for our smart home domain:
# Ask Copilot: "Create a custom agent that specializes in energy analytics,
# IoT device monitoring, and efficiency calculations"

"""
Example agent structure:

---
title: EnergyAnalyticsAgent
description: IoT energy monitoring and efficiency expert
---

You are EnergyAnalyticsAgent, specialized in smart home energy systems.

## Domain Knowledge
- Energy consumption patterns
- Device efficiency metrics
- Cost optimization strategies
- IoT sensor data analysis

## Available Context
- Device models in models/device.py
- Reading models in models/reading.py
- Analytics logic in services/analytics.py

## Your Approach
1. Always consider time-of-use energy rates
2. Suggest practical energy-saving recommendations
3. Use real-world efficiency benchmarks
4. Reference industry standards (Energy Star, etc.)
"""

# TASK 6: Test domain-specific knowledge
# Ask: "@EnergyAnalyticsAgent What's the ideal efficiency score for a smart thermostat?"
# The agent should provide domain-specific insights!


# ═══════════════════════════════════════════════════════════════════════════════
# PART 4: Agents with Custom Tools
# ═══════════════════════════════════════════════════════════════════════════════

# TASK 7: Create an agent that uses MCP tools
# Combine Exercise 8 (MCP) with custom agents!

"""
---
title: DataAnalystAgent
description: Data analyst with access to database and APIs via MCP
---

You are DataAnalystAgent, a data analysis expert.

## Your Tools
- @mcp:sqlite - Query the energy database
- @mcp:weather - Fetch weather correlation data
- @mcp:utility-rates - Get current electricity rates

## Your Workflow
1. Query data using appropriate MCP tools
2. Perform statistical analysis
3. Generate visualization code (matplotlib/plotly)
4. Provide actionable insights

## Your Output
- Always show the data query used
- Explain statistical significance
- Suggest business actions
"""

# TASK 8: Use the data analyst agent
# Ask: "@DataAnalystAgent Analyze the correlation between temperature and
# device efficiency for the past week"
# The agent will orchestrate MCP tools and provide analysis!


# ═══════════════════════════════════════════════════════════════════════════════
# PART 5: Multi-Agent Workflows
# ═══════════════════════════════════════════════════════════════════════════════

# TASK 9: Create a workflow using multiple agents
# Scenario: Adding a new feature with proper testing

# Step 1: Ask @EnergyAnalyticsAgent for feature design
# "@EnergyAnalyticsAgent Design a peak demand prediction feature"

# Step 2: Implement using standard Copilot
# Use the Chat to generate the implementation

# Step 3: Ask @TestingExpert for test coverage
# "@TestingExpert Create tests for the peak demand prediction"

# Step 4: Ask @GitExpert for commit guidance
# "@GitExpert How should I commit this new feature?"


# TASK 10: Create an "ArchitectureReviewer" agent
# Ask Copilot: "Create an agent that reviews code for architectural compliance
# with our services/ and models/ structure"

"""
---
title: ArchitectureReviewer
description: Enforces project architectural patterns
---

You are ArchitectureReviewer, guardian of clean architecture.

## Project Rules (from .github/copilot-instructions.md)
- Logic belongs in services/
- Data models belong in models/
- Use type hints everywhere
- Prefer f-strings for formatting

## Your Review Process
1. Check if new logic is in services/
2. Verify type hints are present
3. Ensure imports are organized
4. Check for proper error handling

## Your Feedback
- Specific file and line references
- Explanation of why a pattern is preferred
- Refactoring suggestions with code examples
"""


# ═══════════════════════════════════════════════════════════════════════════════
# PART 6: Agent Best Practices
# ═══════════════════════════════════════════════════════════════════════════════

# TASK 11: Learn agent design best practices
# Ask Chat: "What are the best practices for creating effective custom agents?"

# Expected principles:
# - Clear, focused scope (don't make agents too general)
# - Specific expertise areas
# - Defined communication style
# - Access to relevant context/tools
# - Examples of good vs bad responses


# TASK 12: Create an agent collaboration guide
# Ask: "Create a document explaining which agent to use for different tasks"

# Example output:
"""
# Agent Selection Guide

## For Code Implementation
- Use default @workspace for general development
- Use @EnergyAnalyticsAgent for domain-specific features

## For Testing
- Use @TestingExpert for all testing-related questions

## For Data Analysis
- Use @DataAnalystAgent when working with databases or APIs

## For Architecture
- Use @ArchitectureReviewer before committing code

## For Git Workflow
- Use @GitExpert for commit messages and branch strategy
"""


# ═══════════════════════════════════════════════════════════════════════════════
# BONUS: Advanced Agent Techniques
# ═══════════════════════════════════════════════════════════════════════════════

# TASK 13: Create an agent with persona
# Build a "SecurityAuditor" agent with a security-focused personality:

"""
---
title: SecurityAuditor
description: Security-first code reviewer
---

You are SecurityAuditor, a cybersecurity expert with 15 years of experience.

## Your Mindset
- Assume threat actors are sophisticated
- Prioritize defense in depth
- Never trust user input

## Security Checks
- [ ] Input validation and sanitization
- [ ] Authentication and authorization
- [ ] Secrets management (no hardcoded keys)
- [ ] SQL injection prevention
- [ ] XSS protection
- [ ] CSRF tokens

## Your Communication
- Direct and firm on security issues
- Explain the attack vector, not just the fix
- Reference OWASP Top 10 when relevant
"""

# TASK 14: Use the security agent
# Ask: "@SecurityAuditor Review the data_ingestion.py for security vulnerabilities"


# ═══════════════════════════════════════════════════════════════════════════════
# KEY TAKEAWAYS
# ═══════════════════════════════════════════════════════════════════════════════

"""
✅ Custom agents are defined in .github/agents/*.agent.md files
✅ Agents have focused expertise, custom instructions, and specific tools
✅ Use @ to invoke agents in Copilot Chat
✅ Combine multiple agents for complex workflows
✅ Agents can use MCP tools for external data access
✅ Design agents with clear scope and communication style
✅ Use agents to enforce team standards and best practices

🎉 Congratulations! You've completed all GitHub Copilot exercises!
Next: Test your skills in the hackathon/ challenges!
"""


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICAL EXERCISE: Build Your Own Agent
# ═══════════════════════════════════════════════════════════════════════════════

# CHALLENGE: Create a custom agent for YOUR domain
# 1. Identify a specific task you do repeatedly
# 2. Create a custom agent to help with that task
# 3. Test it with real questions
# 4. Iterate on the instructions based on quality of responses

# Examples:
# - APIDocAgent - Generates API documentation
# - DatabaseMigrationAgent - Helps with schema changes
# - DeploymentAgent - Assists with CI/CD pipelines
# - OnboardingAgent - Helps new team members understand the codebase
