import sys
import os 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.conn import conn,cursor

def query_rain_percentage():
    sql = """
       SELECT rain_chance FROM weather_data WHERE date =  'Today' OR date = 'Tonight'
    """
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

print(query_rain_percentage())
