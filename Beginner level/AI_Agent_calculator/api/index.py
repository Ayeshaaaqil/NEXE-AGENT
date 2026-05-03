from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import os
from tools.math_engine import calculate
from tools.memory_store import calc_memory  # Nayi file import karein

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    # Dashboard load karein
    with open(os.path.join("static", "index.html"), "r") as f:
        return f.read()

@app.post("/api/calculate")
async def process_calc(request: Request):
    body = await request.json()
    user_query = body.get("query", "")
    
    # Memory se pichla result nikaal kar calculation engine ko dena
    last_res = calc_memory.get_last_result()
    result = calculate(user_query, last_res)
    
    # Agar calculation sahi rahi, toh memory update kar dena
    if result.get("status") == "success":
        calc_memory.save_result(result["data"]["result"])
        
    return result

@app.post("/api/clear")
async def clear_memory():
    calc_memory.clear()
    return {"status": "success", "message": "Memory cleared"}