import pandas as pd
from fastapi import FastAPI
from fastapi import FastAPI
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends

app = FastAPI()

data_list = []

def load_data():
    global data_list
    excel_file = 'FYP_CHR_Data.xlsx'  # Replace with the actual path of your Excel file
    df = pd.read_excel(excel_file)
    data_list = df.to_dict(orient='records')

@app.on_event("startup")
async def startup_event():
    load_data()
    print("Data loaded successfully on startup")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app"}

@app.get("/sessions")
def read_sessions():
    return data_list
