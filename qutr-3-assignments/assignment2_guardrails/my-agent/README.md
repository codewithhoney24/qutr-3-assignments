# Assignment 2: Implement Output Guardrail Functionality

This project extends the **guardrails.py** example by adding **output guardrails** and demonstrating advanced usage of OpenAI’s Agent SDK.

---

## ✨ Features
1. **Two Agents**
   - **BotAgent**: Handles math queries, FAQs, and order lookups.
   - **HumanAgent**: Escalation target for complex/negative queries.

2. **Function Tools**
   - `get_order_status(order_id)` → Simulates order lookup.
   - Uses `is_enabled` logic through query routing (order-related only).
   - Returns friendly error if order not found.

3. **Guardrails**
   - **Input Guardrail**: Blocks non-math, non-order queries.
   - **Output Guardrail**: Sanitizes responses to avoid politics/political figures.
   - **Negative Guardrail**: Detects offensive language → escalates to HumanAgent.

4. **Agent Handoff**
   - If offensive/complex → handoff to HumanAgent.

5. **ModelSettings**
   - `tool_choice="auto"` (let bot decide tool usage).
   - Metadata added (`team: support-bot`, `version: 2.0`).

6. **Logging**
   - Logs all queries, responses, tool invocations, and handoffs to `agent_log.txt`.

---

## 📂 Folder Structure
