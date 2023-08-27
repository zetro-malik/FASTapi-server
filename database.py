import pyodbc
import datetime

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=ZETRO\MSSQLSERVER01;"
    "Database=cra;"
    "Trusted_Connection=yes;"
)

