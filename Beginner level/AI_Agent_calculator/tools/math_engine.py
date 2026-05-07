import math
import re

def calculate(query, last_result=None):
    # 1. Pre-processing
    query = query.lower().strip()

    # 2. Security Firewall
    forbidden = ["import", "os", "sys", "eval", "exec", "getattr", "write", "__", "open", "builtins"]
    if any(f in query for f in forbidden):
        return {"status": "error", "message": "Security Alert: Restricted keywords detected."}

    # 3. Natural Language & Mobile Symbols Mapping
    mappings = {
        "ten": "10", "twenty": "20", "thirty": "30", "forty": "40", "fifty": "50",
        "hundred": "100", "thousand": "1000", "add by": "+", "plus": "+", 
        "minus": "-", "multiply": "*", "divide": "/", "times": "*", 
        "into": "*", "percent": "/100", "square root of": "math.sqrt(", "root of": "math.sqrt(",
        "of": "*",
        "×": "*",  # Mobile multiplication symbol fix
        "÷": "/",  # Mobile division symbol fix
        "−": "-"   # Mobile long dash (hyphen) fix
    }
    
    # Sort to replace longer words first
    for word in sorted(mappings.keys(), key=len, reverse=True):
        query = query.replace(word, mappings[word])

    # 4. Handle Memory
    if any(word in query for word in ["result", "it", "ans", "previous"]):
        if last_result is None:
            return {"status": "error", "message": "Memory is empty."}
        for word in ["result", "it", "ans", "previous"]:
            query = query.replace(word, str(last_result))

    # 5. Percentage Logic Fix (Handles both 10% and 10 % with space)
    query = re.sub(r'(\d+(\.\d+)?)\s*%', r'(\1/100)', query)

    # 6. Math logic fix (Brackets for sqrt)
    if "math.sqrt(" in query and not query.endswith(")"):
        query += ")"

    # 7. Sanitize: Ab humne extra symbols ko allow karna hai jo mapping se aaye hain
    # Humne '×' aur '÷' ko pehle hi replace kar diya hai, isliye sirf math operators bachenge
    expression = re.sub(r'[^0-9+\-*/().math.sqrt]', '', query).strip()
    
    try:
        if not expression: raise ValueError("Empty")
        
        result = eval(expression, {"__builtins__": None}, {"math": math})
        
        return {
            "status": "success",
            "data": {
                "result": round(float(result), 4),
                "expression": expression
            }
        }
    except ZeroDivisionError:
        return {"status": "error", "message": "Division by zero is not allowed."}
    except Exception:
        return {"status": "error", "message": "Invalid expression. Try '10% of 500' or '5 × 5'."}
