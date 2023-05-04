from databases import Database
import os
database = Database('sqlite+aiosqlite:///new.db')
TOKEN = os.environ.get('TOKEN', '')
print('TOKEN:', TOKEN)