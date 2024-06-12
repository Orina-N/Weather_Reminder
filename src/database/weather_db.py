import os
import sys
import schedule
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scraping.scraper import scrape_weather_data
from conn import conn, cursor

def create_table():
    #print("Creating table...")
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS weather_data (
        date TEXT,
        temperature TEXT,
        low_temperature TEXT,
        rain_chance TEXT,
        wind_speed TEXT
    )
    '''
    cursor.execute(create_table_query)
    conn.commit()
    #print("Table created successfully.")

def insert_data():
    #print("Inserting data...")
    truncate_query = "DELETE FROM weather_data"
    cursor.execute(truncate_query)
    conn.commit()

    insert_query = '''
    INSERT INTO weather_data (date, temperature, low_temperature, rain_chance, wind_speed)
    VALUES (?, ?, ?, ?, ?)
    '''
    weather_data = scrape_weather_data()

    for data in weather_data:
        cursor.execute(insert_query, (data['date'], data['temperature'], data['low_temperature'], data['rain_chance'], data['wind_speed']))
    conn.commit()
    #print("Data inserted successfully.")


def new_day():
    create_table()
    insert_data()

schedule.every().day.at("00:00").do(new_day)


while True:
    schedule.run_pending()
    time.sleep(1)

