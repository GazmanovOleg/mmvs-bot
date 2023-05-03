import  sqlite3 as sq
from config import database

async def db_start():
    print("база данных создана")
    await database.connect()
    await database.execute("CREATE TABLE IF NOT EXISTS meeting(meeting_id TEXT PRIMARY KEY, date, time, service, connection ,other)")
    # await database.commit()
    

async def create_meeting(meeting_id, other):
    await database.connect()
    meeting = await database.fetch_one("SELECT 1 FROM meeting WHERE meeting_id == :meeting_id", values = {'meeting_id':meeting_id})
    print("dfgdfgdfg")
    print(meeting)
    if not meeting:
        print("Приход")
        values = {'meeting_id':meeting_id, 'date':"", 'time':"", 'service':" ", 'connection':" ", 'other':other}
        query = f"INSERT INTO meeting (meeting_id, date, time, service, connection ,other) VALUES(:meeting_id, :date, :time, :service, :connection ,:other)"
        await database.fetch_one(query, values)
        #await db.commit()



        
         
async def edit_meeting(meeting_id, name, value):
    await database.connect()
    values = {'value':value, 'meeting_id':meeting_id}
    query = f"UPDATE meeting SET {name} = :value WHERE meeting_id = :meeting_id"
    return await database.fetch_one(query, values)

  




async def get_meet_by_id(meeting_id):
    print("Приход2222")
    await database.connect()
    query = f"SELECT date, time, connection FROM meeting WHERE meeting_id == {meeting_id}"
    
    return await database.fetch_one(query)


async def get_meetings():
    await database.connect()
    
    return await  database.execute(f"SELECT date, time FROM meeting").fetchall()


async def get_busy_times_by_day(day):
   
    await database.connect()

    return await database.fetch_all("SELECT time FROM meeting WHERE date == :day", values={'day':day})
    
   