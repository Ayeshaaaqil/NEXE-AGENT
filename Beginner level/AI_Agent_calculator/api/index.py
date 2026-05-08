from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import os
from tools.math_engine import calculate
from tools.memory_store import calc_memory

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    # Use absolute path if Vercel gives file not found error
    file_path = os.path.join(os.getcwd(), "static", "index.html")
    with open(file_path, "r") as f:
        return f.read()

@app.post("/api/calculate")
async def process_calc(request: Request):
    try:
        body = await request.json()
        user_query = body.get("query", "")
        
        last_res = calc_memory.get_last_result()
        result = calculate(user_query, last_res)
        
        if result.get("status") == "success":
            calc_memory.save_result(result["data"]["result"])
            
        return result
    except Exception as e:
        return JSONResponse(status_code=400, content={"status": "error", "message": str(e)})

@app.post("/api/clear")
async def clear_memory():
    calc_memory.clear()
    return {"status": "success", "message": "Memory cleared"}
