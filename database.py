import pyodbc
import datetime

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=ZETRO\MSSQLSERVER01;"
    "Database=cra;"
    "Trusted_Connection=yes;"
)



def getTimeTable():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TimeTable")
    data = []
    for row in cursor:
        json = {
            "ID": row[0],
            "Day": row[1],
            "StartTime": row[2],
            "EndTime": row[3],
            "Section": row[4],
            "CourseName": row[5],
            "CourseCode": row[6],
            "TeacherName": row[7],
            "Venue": row[8],
            "Semester": row[9],
            "Floor": row[10]
        }
        data.append(json)
    return data

def insert_class_not_held(tid):
    current_day = datetime.datetime.now().strftime('%a')
    cursor = conn.cursor()

    insert_query = "INSERT INTO Attendance (TID, Day, Date, TimeIn, TimeOut,remarks) VALUES (?, ?, ?, NULL, NULL,?)"
    values = (tid, current_day, datetime.date.today(),"Class Not Held")
    cursor.execute(insert_query, values)

    conn.commit()

def insert_class_in(tid,startime, remarks):
    current_day = datetime.datetime.now().strftime('%a')
    cursor = conn.cursor()

    insert_query = "INSERT INTO Attendance (TID, Day, Date, TimeIn, TimeOut,remarks) VALUES (?, ?, ?, ?, NULL,?)"
    values = (tid, current_day, datetime.date.today(),startime,remarks)
    cursor.execute(insert_query, values)

    conn.commit()

    
def insert_class_out(tid,startime, remarks):
    current_day = datetime.datetime.now().strftime('%a')
    cursor = conn.cursor()

    insert_query = "INSERT INTO Attendance (TID, Day, Date, TimeIn, TimeOut,remarks) VALUES (?, ?, ?, ?, NULL,?)"
    values = (tid, current_day, datetime.date.today(),startime,remarks)
    cursor.execute(insert_query, values)

    conn.commit()

def insert_class_out(tid, endtime):
        cursor = conn.cursor()
        update_query = """
            UPDATE Attendance
            SET TimeOut = ?
            WHERE TID = ?
        """
        cursor.execute(update_query, (endtime, tid))
        conn.commit()
        print(f"Time out recorded for TID {tid}")


def getAttendanceData():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Attendance")
    data = []
    for row in cursor:
        json = {
            "ID": row[0],
            "TID": row[1],
            "Day": row[2],
            "Date": row[3],
            "TimeIn": row[4],
            "TimeOut": row[5]
        }
        data.append(json)
    return data




if __name__ == "__main__":
    insert_class_not_held(1)