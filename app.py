import pandas as pd
from fastapi import FastAPI, Request
from fastapi import FastAPI
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends
from datetime import time
import database as db

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app"}

@app.get("/sessions")
def read_sessions():
    return JSONResponse(content=db.getTimeTable())

@app.post("/classNotHeld/{ID}")
async def class_not_held(ID: int):
     db.insert_class_not_held(ID)
     return {"message": "success"}

@app.post("/insert_timein")
async def process_json(request: Request):
    try:
        json_data = await request.json()
        db.insert_class_in(json_data['tid'],json_data['current_time'],json_data['remarks'])
        return {"received_json": json_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid JSON data")
    

@app.post("/insert_timeout")
async def process_json(request: Request):
    try:
        json_data = await request.json()
        db.insert_class_out(json_data['tid'],json_data['current_time'])
        return {"received_json": json_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid JSON data")
    

@app.post("/director_attendance")
async def process_json(request: Request):
    try:
        return JSONResponse(content=db.getAttendanceData())
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid JSON data")