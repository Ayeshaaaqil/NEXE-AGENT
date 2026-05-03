# 🧮 Task 2: AI Calculator Agent

A sophisticated, autonomous AI Calculator built with **Python (FastAPI)**. This agent is designed to process natural language math requests, maintain calculation memory, and output results in a clean, structured JSON format.

---

## 🚀 Key Features

*   **Natural Language Processing:** Understands requests like "Add 5 to my previous result" or "Calculate the square root of 144".
*   **Memory Management:** Stores the last calculated value in a session-based memory for sequential operations.
*   **Advanced Math Ops:** Supports Basic (Add, Sub, Mul, Div) and Advanced (Power, Root, Percentage) calculations.
*   **Structured Output:** Every response follows a strict JSON schema for professional integration.
*   **Clean UI/UX:** A modern, dark-themed dashboard with real-time feedback and calculation history.

---

## 📂 Project Structure

The project is organized into a modular architecture for scalability:
```text
ai-calculator-agent/
│
├── api/
│   └── index.py          # Main FastAPI entry point & Routing
│
├── tools/
│   ├── __init__.py
│   ├── math_engine.py    # Core logic for mathematical operations
│   └── memory_store.py   # Logic for handling session-based memory
│
├── static/
│   └── index.html        # Professional Frontend (Tailwind CSS)
│
├── requirements.txt      # List of dependencies (FastAPI, Uvicorn, etc.)
├── vercel.json           # Configuration for Vercel deployment
└── README.md             # Project documentation (This file)