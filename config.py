from databases import Database
import os
database = Database('sqlite+aiosqlite:///new.db')
TOKEN = '6187663762:AAE_A4w9caLn5JLuelzZPUfTQKi3y50x544'
#os.environ.get('TOKEN', '')
print('TOKEN:', TOKEN)