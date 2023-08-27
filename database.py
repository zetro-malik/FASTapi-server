import pyodbc
import datetime

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=ZETRO\MSSQLSERVER01;"
    "Database=cra;"
    "Trusted_Connection=yes;"
)


########################## lectures into slide ###############################


def SaveIntervalBoardImage(lectureID, path):
    x = datetime.datetime.now().strftime("%X")
    cursor = conn.cursor()
    cursor.execute("insert into IntervalBoardImage values(?,?,?)", (lectureID, path, x))
    conn.commit()


def SaveSlide(lectureID, path):
    cursor = conn.cursor()
    cursor.execute("insert into slide values(?,?)", (lectureID, path))
    conn.commit()


def SaveConflictedBoardSegment(lectureID, imageNO, imageSide, path):
    cursor = conn.cursor()
    cursor.execute(
        "insert into ConflictedBoardSegment values(?,?,?,?)",
        (lectureID, imageNO, imageSide, path),
    )
    conn.commit()


def getSlide(ID):
    cursor = conn.cursor()
    cursor.execute("select * from slide where lectureID=?", (ID))

    for row in cursor:
        return row[1]


def getConflictedImage(id):
    cursor = conn.cursor()
    cursor.execute("select * from ConflictedBoardSegment where lectureID=?", (id))
    data = []
    for row in cursor:
        json = {
            "ID": row[0],
            "lectureID": row[1],
            "ImageNO": row[2],
            "ImageSide": row[3],
            "Image": row[4],
        }
        data.append(json)
    return data


def saveExamHallData(subject, x, teacher):
    print(x)
    cursor = conn.cursor()
    cursor.execute("insert into exam values(?,?,?)", (subject, x, teacher))
    conn.commit()
    cursor.execute(
        "select * from exam where subject=? and date=? and teacher=?",
        (subject, x, teacher),
    )
    rowID = -1
    for row in cursor:
        rowID = row[0]
    return rowID


def saveExamActivity(ID, std, name):
    start_time = datetime.datetime.now().strftime("%X")
    cursor = conn.cursor()
    cursor.execute(
        "insert into cheatingActivity (examID,studentID,name,startTime) values (?,?,?,?)",
        (ID, std, name, str(start_time)),
    )
    conn.commit()
    cursor.execute(
        "select * from cheatingActivity where examID=? and studentID=? and name=? and startTime=?",
        (ID, std, name, str(start_time)),
    )
    rowID = -1
    for row in cursor:
        rowID = row[0]
    return rowID


def updateExamEndActivityTime(ID):
    cursor = conn.cursor()
    cursor.execute(
        "update cheatingActivity set endTime=? where activityID=?",
        (str(datetime.datetime.now().strftime("%X")), ID),
    )
    conn.commit()


def getExamActivity():
    cursor = conn.cursor()
    cursor.execute("select * from cheatingActivity")
    data = []
    for row in cursor:
        json = {
            "ID": row[0],
            "examID": row[1],
            "studentID": row[2],
            "name": row[3],
            "startTime": row[4],
            "endTime": row[5],
        }
        data.append(json)
    return data


def readRoomID(id):
    cursor = conn.cursor()
    cursor.execute("select * from lecture where lectureID=?", (id))
    data = ""
    for row in cursor:
        data = row
    return data


def readAllLectureInfo():
    cursor = conn.cursor()
    cursor.execute("select * from lecture")
    data = []
    for row in cursor:
        json = {
            "lectureID": row[0],
            "class": row[1],
            "section": row[2],
            "course": row[3],
            "teacher": row[4],
            "date": row[5]
        }
        data.append(json)
    return data


def SaveRoomData(cls, section, course, teacher):
    x1 = datetime.datetime.now().strftime("%x")
    x2 = datetime.datetime.now().strftime("%X")
    x = x1 + "_" + x2
    print(x)
    cursor = conn.cursor()
    cursor.execute(
        "insert into lecture values(?,?,?,?,?)", (cls, section, course, teacher, x)
    )
    conn.commit()
    cursor.execute(
        "select * from lecture where class=? and section=? and course=? and teacher=? and date=?",
        (cls, section, course, teacher, x),
    )
    rowID = -1
    for row in cursor:
        rowID = row[0]
    return rowID


def SaveActivityData(ID, std, name):
    start_time = datetime.datetime.now().strftime("%X")
    cursor = conn.cursor()
    cursor.execute(
        "insert into activity (lectureID,studentID,name,startTime) values (?,?,?,?)",
        (ID, std, name, str(start_time)),
    )
    conn.commit()
    cursor.execute(
        "select * from activity where lectureID=? and studentID=? and name=? and startTime=?",
        (ID, std, name, str(start_time)),
    )
    rowID = -1
    for row in cursor:
        rowID = row[0]
    return rowID


def updateEndActivityTime(ID):
    cursor = conn.cursor()
    cursor.execute(
        "update activity set endTime=? where activityID=?",
        (str(datetime.datetime.now().strftime("%X")), ID),
    )
    conn.commit()



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
            "Semester": row[9]
        }
        data.append(json)
    return data