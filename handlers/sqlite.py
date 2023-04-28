import  sqlite3 as sq
from config import database

async def db_start():
    print("база данных создана")
    await database.connect()
    await database.execute("CREATE TABLE IF NOT EXISTS meeting(meeting_id TEXT PRIMARY KEY, date, time, service, connection ,other)")
    # await database.commit()
    

async def create_meeting(meeting_id):
    await database.connect()
    meeting = await database.fetch_one("SELECT 1 FROM meeting WHERE meeting_id == '{key}'".format(key =meeting_id))
    if not meeting:
        await database.fetch_one("INSERT INTO meeting VALUES(?,?,?,?,?,?)", (meeting_id, '', '', '', '',''))
        #await db.commit()
         
async def edit_meeting(meeting_id, name, value):
    
    await database.connect()

    if name == 'date':
        query = f"UPDATE meeting SET date = :date WHERE meeting_id = :meeting_id"
       
        await database.execute(query,values={'date':value,'meeting_id':meeting_id})
    else:
        query = f"UPDATE meeting SET {name} = ? WHERE meeting_id = ?"
        
        await database.execute(query, (value, meeting_id))
    #db.commit()  


async def get_meet_by_id(meeting_id):
    await database.connect()
    
    meeting = await database.execute(f"SELECT date, time FROM meeting WHERE meeting_id == {meeting_id}")
    return await meeting.fetchone()


async def get_meetings():
    await database.connect()
    
    return await  database.execute(f"SELECT date, time FROM meeting").fetchall()


async def get_busy_times_by_day(day):
    await database.connect()

    return await database.fetch_all("SELECT time FROM meeting WHERE date == '{key}'".format(key = day))
    
   