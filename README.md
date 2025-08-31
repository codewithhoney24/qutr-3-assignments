# QUTR 3 Assignments

This repository contains multiple assignments demonstrating AI agent workflows, guardrails, dynamic instructions, and smart customer support bots using Python and OpenAI’s Agent SDK.

---

## 📁 Repository Structure

---

## **Assignment 1: Custom Web Search Tool**
**Objective:**  
Build a custom web search tool using the Tavily API integrated with an AI Agent to retrieve and process web information.

**Tasks:**
- Explore [Tavily API documentation](https://docs.tavily.com)  
- Implement a search tool that fetches results via the API.  
- Ensure the tool can be called by an AI agent to answer user queries.

**Code Location:**  
[Custom-Web-Search-Tool/](Custom-Web-Search-Tool/)


---

## **Assignment 2: Implement Output Guardrail Functionality**
**Objective:**  
Extend the existing `guardrails.py` example to add output guardrails using OpenAI’s Agent SDK.

**Tasks:**
- Current code blocks non-math queries (input guardrails).  
- Add rules so agent responses avoid political topics and references to political figures.

**Code Location:**  
[`assignment2_guardrails/guardrails.py`](assignment2_guardrails/guardrails.py)

---

## **Assignment 3: Convert Static Instructions into Dynamic Instructions**
**Objective:**  
Convert static instructions into dynamic ones using OpenAI’s Agent SDK based on the `bilal_fareed_code` example.

**Tasks:**
- Enable a single agent to store and retrieve details for multiple hotels.  
- Use context to return the correct hotel information based on the user’s query.

**Code Location:**  
[`bilal_fareed_code/my_agent/hotel_assistant.py`](bilal_fareed_code/my_agent/hotel_assistant.py)

---

## **Assignment 4: Build a Smart Customer Support Bot**
**Objective:**  
Create a customer support bot using OpenAI’s Agent SDK that handles FAQs, fetches order statuses, and escalates to a human agent when necessary. Include guardrails to ensure positive interactions.

**Requirements:**
- Answer basic product FAQs.  
- Fetch order status using a simulated API (`function_tool`).  
- Escalate to a human agent if the query is complex or sentiment is negative.  
- Enforce guardrails to block or rephrase negative/offensive input.  
- Showcase usage of `model_settings` (tool_choice, metadata, etc.).  
- Demonstrate advanced use of `@function_tool` decorator (`is_enabled`, `error_function`).

**Breakdown of Required Elements:**
1. **Agents**: BotAgent (handles FAQs & orders) & HumanAgent (handoff)  
2. **Function Tools**: `@function_tool` for `get_order_status(order_id)`  
3. **Guardrails**: `@guardrail` to check offensive/negative language  
4. **Agent Handoff**: Escalate to HumanAgent if bot cannot handle query  
5. **ModelSettings**: Use `tool_choice="auto"` or `"required"` and metadata  
6. **Logging**: Log all tool invocations and handoffs

**Code Location:**  
[`smart-customer-support-bot/`](smart-customer-support-bot/)

---

**Notes:**  
- Each assignment includes full source code with comments highlighting tool calls, guardrails, handoffs, and `model_settings`.  
- Screenshots or logs can be added to demonstrate all scenarios working.  

---

🚀 Happy Coding!
