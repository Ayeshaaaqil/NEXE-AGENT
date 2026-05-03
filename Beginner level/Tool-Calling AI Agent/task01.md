Tool-Calling AI Agent

Project Overview

This project is a Tool-Calling AI Agent built with Python that can understand user requests, call appropriate tools/functions, return structured JSON responses, handle errors gracefully, and be deployed online using Vercel with source code managed through GitHub.

---

Tech Stack

- Python – Core programming language
- GitHub – Version control and repository hosting
- Vercel – Deployment/Hosting platform

---

Core Requirements

1. Function Calling

The AI Agent should:

- Detect when a tool/function is required
- Select the appropriate function based on user input
- Pass correct parameters to the function
- Execute the function/tool
- Process and return the result

Example

{
  "function": "get_weather",
  "parameters": {
    "city": "Karachi"
  }
}

---

2. JSON Response

The agent must return structured JSON responses for all outputs.

Success Response Example

{
  "status": "success",
  "message": "Weather fetched successfully",
  "data": {
    "temperature": "32°C",
    "condition": "Sunny"
  }
}

Standard JSON Fields

- "status"
- "message"
- "data"
- "error"

---

3. Error Handling

The agent should properly manage runtime and user-input errors.

Error Cases to Handle

- Missing required parameters
- Invalid input format
- Tool/function not found
- External API/tool failure
- Unexpected internal exceptions

Error Response Example

{
  "status": "error",
  "message": "Missing required parameter: city",
  "error_code": 400
}

---

Additional Recommended Requirements

4. Project Structure

tool-calling-ai-agent/
│
├── main.py
├── tools/
│   ├── weather.py
│   ├── search.py
│   └── utility.py
│
├── utils/
│   └── error_handler.py
│
├── requirements.txt
├── vercel.json
└── README.md

---

5. Deployment Requirements

- Push project code to GitHub repository
- Connect GitHub repository with Vercel
- Configure "vercel.json" for Python deployment
- Deploy live project URL

---

6. Best Practices

- Use modular code structure
- Add input validation before function calls
- Write reusable utility functions
- Keep JSON response format consistent
- Use try/except blocks for robust error handling

---

Workflow

1. User sends request
2. Agent analyzes user intent
3. Appropriate function/tool selected
4. Function executed
5. Result formatted into JSON
6. Error handled if occurs
7. Response returned to user

---

Deliverables

- GitHub Repository Link
- Vercel Deployment Link
- Source Code in Python
- Documentation ("README.md")
- Working Tool-Calling AI Agent

---

Conclusion

This Tool-Calling AI Agent demonstrates practical implementation of function calling, structured JSON communication, robust error handling, and cloud deployment using modern development workflows.