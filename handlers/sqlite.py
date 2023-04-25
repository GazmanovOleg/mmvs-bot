import  sqlite3 as sq

async def db_start():
    global db, cur
    print("база данных создана")
    db = sq.connect('new.db')
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS meeting(meeting_id TEXT PRIMARY KEY, date, time, other) ")
    db.commit()

async def create_meeting(meeting_id):
    meeting = cur.execute("SELECT 1 FROM meeting WHERE meeting_id == '{key}'".format(key =meeting_id)).fetchone()
    if not meeting:
        cur.execute("INSERT INTO meeting VALUES(?,?,?,?)", (meeting_id, '', '', ''))
        db.commit()
    

async def edit_meeting(meeting_id, name, value):
    cur.execute(f"UPDATE meeting SET {name} = {value} WHERE meeting_id == '{meeting_id}'")
    db.commit()   

def get_meet_by_id(meeting_id):
    meeting = cur.execute(f"SELECT date, time FROM meeting WHERE meeting_id == {meeting_id}")
    return meeting