from dataclasses import replace
import psycopg2
import pandas as pd
import api_final_call as ap
from sqlalchemy import create_engine

# assign marvel_db database details
user, password, host, port, db  = 'root', 'root', 'localhost', 5432, 'marvel_db'

# assign api request to new sets of variables from the api_request.py script
characters, comics, events, stories = ap.get_character(), ap.get_comics(), ap.get_events(), ap.get_stories()

def connect_db():
    print('Connecting to Marvel Database...')

    # login to marvel_db database
    conn = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    # check connection if successful
    conn.connect()
    return conn


print('database successfully connected, now saving tables to Marvel database')

def save_to_db():
    conn = connect_db()
    # save characters table to marvel_db
    characters.to_sql(name='characters', con=conn, index=False, if_exists='replace')
    # save comics table to marvel_db
    comics.to_sql(name='comics', con=conn, index=False, if_exists='replace')
    # save events table to marvel_db
    events.to_sql(name='events', con=conn, index=False, if_exists='replace')
    # save series table to marvel_db
    #series.to_sql(name='series', con=conn, index=False, if_exists='replace')
    # save stories table to marvel_db
    stories.to_sql(name='stories', con=conn, index=False, if_exists='replace')

save_to_db()
print('Done...')


# print('All tables have been successfully created... you can now check pgadmin')

# def main():
#     print('connecting to Marvel database...')
#     connect_db()

#     print('################################')

#     print('create table and load data...')
#     save_to_db()

#     print('All tables have been successfully created...')
#     if __name__ == "__main__":
#         main()