import  sqlite3 as sq


async def db_start():
    global db, cur
    print("база данных создана")
    db = sq.connect('new.db')
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS meeting(meeting_id TEXT PRIMARY KEY, date, time, other)")
    db.commit()
    

async def create_meeting(meeting_id):
    meeting = cur.execute("SELECT 1 FROM meeting WHERE meeting_id == '{key}'".format(key =meeting_id)).fetchone()
    if not meeting:
        cur.execute("INSERT INTO meeting VALUES(?,?,?,?)", (meeting_id, '', '', ''))
        db.commit()
        
    
async def edit_meeting(meeting_id, name, value):

    query = f"UPDATE meeting SET {name} = ? WHERE meeting_id = ?"
    cur.execute(query, (value, meeting_id))
    db.commit()  


def get_meet_by_id(meeting_id):
    meeting = cur.execute(f"SELECT date, time FROM meeting WHERE meeting_id == {meeting_id}")
    
    return meeting.fetchone()

def get_meetings():
    return  cur.execute(f"SELECT date, time FROM meeting").fetchall()

def get_busy_times_by_day(day):
    return cur.execute("SELECT time FROM meeting WHERE date == '{key}'".format(key = day)).fetchall()
    
   