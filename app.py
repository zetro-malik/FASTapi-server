import pandas as pd
from fastapi import FastAPI
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

@app.get("/classNotHeld/{ID}")
async def class_not_held(ID: int):
     print(ID)