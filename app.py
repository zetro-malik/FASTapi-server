import pandas as pd
from fastapi import FastAPI
from fastapi import FastAPI
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends
from datetime import time
import database as db

app = FastAPI()

data_list = []

def load_data():
    global data_list
    
    data = pd.read_excel("FYP_CHR_Data.xlsx")

    data["Start Time"] = data["Start Time"].apply(lambda x: x.strftime('%H:%M') if isinstance(x, time) else x)
    data["End Time"] = data["End Time"].apply(lambda x: x.strftime('%H:%M') if isinstance(x, time) else x)

    data = data.loc[:, ~data.columns.str.startswith('Unnamed')]
    data = data[~data.apply(lambda row: "nan" in row.values, axis=1)]   

    
    data_list = data.to_dict(orient="records")

@app.on_event("startup")
async def startup_event():
    load_data()
    print(data_list)
    print("Data loaded successfully on startup")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app"}

@app.get("/sessions")
def read_sessions():
    return JSONResponse(content=db.getTimeTable())