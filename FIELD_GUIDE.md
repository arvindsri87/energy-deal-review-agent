# Field Guide: AI Prompting & Agent Usage for Energy Traders & Account Managers

Designed for commercial leads, traders, and controllers interacting with LLM tools and automated review agents.

---

##  3 Core Principles for Financial Prompting

1. **Explicit Data Scoping:** Always define the exact input parameters (e.g., *“Extract only TTF month-ahead gas indexation clauses”*).
2. **Require Verifiable Sources:** Instruct agents to cite specific clause numbers or policy section headers for every flagged risk.
3. **Zero Financial Math in Prompts:** Never ask an LLM to calculate margins or exposure directly. Use the agent’s built-in financial tools.

---

##  Standard Deal Review Prompt Template

```text
Role: You are an expert commercial risk reviewer for B2B energy contracts.

Task: Review the attached draft B2B supply contract and evaluate it against our Treasury Risk Policy.

Strict Constraints:
1. Extract Contract Volume (MWh), Payment Terms (Days), and Price Indexation mechanism into JSON.
2. Cross-reference Payment Terms against standard limits (Max: 30 Days).
3. Do NOT estimate margins. Invoke the 'calculate_margin' tool with extracted price and volume.
4. Output structured risk flags with exact clause citations.

---

##  Red Flags & What to Watch For

* **Vague Indexation:** If an agent categorizes a pricing formula as "Standard" without listing the index ticker (e.g., THE, TTF, PEG), ask for clarification.
* **Missing Liability Caps:** Ensure liability limit extractions specifically mention whether indirect/consequential damages are excluded.
