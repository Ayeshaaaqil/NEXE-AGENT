import math
import re

def calculate(query, last_result=None):
    # 1. Pre-processing
    query = query.lower().strip()

    # 2. Security Firewall (Block dangerous Python commands)
    forbidden = ["import", "os", "sys", "eval", "exec", "getattr", "write", "__", "open", "builtins"]
    if any(f in query for f in forbidden):
        return {"status": "error", "message": "Security Alert: Restricted keywords detected."}

    # 3. Natural Language Mapping
    mappings = {
        "ten": "10", "twenty": "20", "thirty": "30", "forty": "40", "fifty": "50",
        "hundred": "100", "thousand": "1000", "add by": "+", "plus": "+", 
        "minus": "-", "multiply": "*", "divide": "/", "times": "*", 
        "into": "*", "percent": "/100", "square root of": "math.sqrt(", "root of": "math.sqrt("
    }
    
    for word, symbol in mappings.items():
        query = query.replace(word, symbol)

    # 4. Handle Memory (it, ans, result)
    if any(word in query for word in ["result", "it", "ans", "previous"]):
        if last_result is None:
            return {"status": "error", "message": "Memory is empty. Start a new calculation."}
        for word in ["result", "it", "ans", "previous"]:
            query = query.replace(word, str(last_result))

    # 5. Math logic fix (Brackets for sqrt)
    if "math.sqrt(" in query and not query.endswith(")"):
        query += ")"

    # 6. Sanitize: Keep only numbers and math operators
    expression = re.sub(r'[^0-9+\-*/().%*math.sqrt]', '', query).strip()
    
    try:
        if not expression: raise ValueError("Empty")
        
        # 7. Safe Evaluation
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
        return {"status": "error", "message": "Invalid expression. Try '50 plus 10'."}