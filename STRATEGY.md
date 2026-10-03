# Enterprise AI Enablement Strategy & 90-Day Execution Roadmap

## Executive Overview
Scaling AI across energy trading, commercial sales, and controlling requires balancing model performance, data privacy, and cost economics. This document outlines the architectural framework and 90-day deployment playbook for enterprise AI enablement.

---

## 1. Model Economics & Routing Matrix

| Workload Tier | Sensitivity | Preferred Architecture | Key Justification |
| :--- | :--- | :--- | :--- |
| **Tier 1: Strategic & Unstructured Contract Parsing** | High | Proprietary API (Claude 3.5 Sonnet) | Complex reasoning over multi-page PDF term sheets, indexation logic, and liability clauses. |
| **Tier 2: Trade Ledger & Sensitive Financials** | Critical | Fine-tuned Open-Weight (Llama 3 70B On-Prem) | Complete data isolation for proprietary deal logs and confidential margin data. |
| **Tier 3: Daily Summarization & Search** | Low/Medium | Lightweight Open-Weight (Llama 3 8B / Mixtral) | High-throughput, low-latency processing for daily market news and internal policy RAG. |

---

## 2. Enterprise 90-Day Enablement Roadmap
### Days 1–30: Foundation & Governance
* **Audit & Evaluation Baseline:** Establish automated evaluation suites (Pydantic validation, hallucination tracking) for all active LLM prompts.
* **Architecture & Model Gateway:** Deploy unified LLM routing gateway to track token usage, cost-per-department, and latency across BUs.
* **Compliance Alignment:** Partner with Legal/Risk to map AI tools against EU AI Act requirements and data protection rules.

### Days 31–60: High-Impact Business Pilots
* **Trading & Sales Agent:** Deploy the *Energy Deal Review Agent* MVP to pilot with 5 senior account managers and trading leads.
* **Controlling Commentary Automation:** Roll out automated variance analysis and preliminary P&L commentary generators for monthly reporting cycles.
* **Champion Network:** Launch a hands-on "AI Champions" program across Sales, Trading, and Finance (2 users per department).

### Days 61–90: Enterprise Scaling & Self-Serve
* **Prompt & Agent Library:** Publish internal, tested prompt templates and tool-calling code samples for developer squads.
* **Continuous Feedback Loops:** Implement telemetry logging (WAU, token cost per deal reviewed, manual correction rate).
* **Cross-Functional Hackathon:** Host a business-led AI hackathon focusing on automated risk flagging and logistics optimization.
