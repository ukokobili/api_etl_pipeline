# import request library: for making request to the API
from numpy import character
import requests as rq
import pprint as pp
import pandas as pd
import hashlib # working of MD5 (byte - byte)
import psycopg2
from sqlalchemy import create_engine

# declare API credentials
api_key = '588b45a229442c116e0361f021e60cc8'
private_key = 'c42a86afb87c38979b3fe3b03827394b5887a479'
ts = '1000'



# encode the api keys 
# https://www.pythonpool.com/python-md5/
result = hashlib.md5((ts+private_key+api_key).encode()) 
hash_key = result.hexdigest() 

 # list of marvel characters for API call
ids = 1011334, 1017100, 1009144, 1010699, 1009146, 1016823, 1009148, 1009149, 1010903, 1011266, 1010354, 1010846, 1017851, 1012717, 1011297, 1011031, 1009150, 1011198, 1011175, 1011136

# base url for get request
baseurl = 'http://gateway.marvel.com'

# endpoints for the different schemas
endpoint ='/v1/public/characters'
# filters
stories_ = '/stories'
series_e = '/series'
comics_ = '/comics'
events_ = '/events'

# define get stories function
def get_stories():
    # list for all character IDs details
    main = []
    # loop through the IDs
    for a in ids:
        # get request from the API
        r = rq.get(f'{baseurl}{endpoint}/{a}{stories_}?ts={ts}&apikey={api_key}&hash={hash_key}')
        # return json string
        data = r.json()
        # append to main list
        main.append(data)
    # stories list
    stories = []
    # loop through get 
    for response in main:
        results = response['data']['results']
       
        for details in results:
            story = {
                'id': details['id'],
                'title': details['title'],
                'description': details['description'],
                'modified_date': details['modified'],
                'type': details['type'],
                'character_id': details['characters']['items'][0]['resourceURI'].replace('/',' ').split()[-1],
                'comics_id': details['comics']['items'][0]['resourceURI'].replace('/',' ').split()[-1]
            }
            stories.append(story)              
    return pd.DataFrame(stories)

####################################################################################################################

def get_comics():
    main = []
    # loop through the IDs
    for a in ids:
        # get request from the API
        r = rq.get(f'{baseurl}{endpoint}/{a}{comics_}?ts={ts}&apikey={api_key}&hash={hash_key}')
        # return json string
        data = r.json()
        # append to main list
        main.append(data)
    comics = []
    for response in main:
        results = response['data']['results']
        for details in results:
            comic = {
                'id': details['id'],
                'title': details['title'],
                'description': details['description'],
                'modified_date': details['modified'],
                'number_of_pages': details['pageCount'],
                'print_price': details['prices'][0]['price'],
                'digital_purchase_price': details['prices'][-1]['price'],
                'character_id': details['characters']['items'][0]['resourceURI'].replace('/',' ').split()[-1]
            }
            comics.append(comic)              
    return pd.DataFrame(comics)

##############################################################################################################

def get_events():
    main = []
    # loop through the IDs
    for a in ids:
        # get request from the API
        r = rq.get(f'{baseurl}{endpoint}/{a}{events_}?ts={ts}&apikey={api_key}&hash={hash_key}')
        # return json string
        data = r.json()
        # append to main list
        main.append(data)
    events = []
    for response in main:
        results = response['data']['results']
       
        for details in results:
            event = {
                'id': details['id'],
                'title': details['title'],
                'description': details['description'],
                'modified_date': details['modified'],
                'started': details['start'],
                'ended': details['end'],
                'character_id': details['characters']['items'][0]['resourceURI'].replace('/',' ').split()[-1],
                'creators_id': details['creators']['items'][0]['resourceURI'].replace('/',' ').split()[-1],
                'creators': details['creators']['items'][0]['name'],
                'creators_role': details['creators']['items'][0]['role'],
                'comics_id': details['comics']['items'][0]['resourceURI'].replace('/',' ').split()[-1],
            }
            events.append(event)              
    return pd.DataFrame(events)

#############################################################################################################

def get_character():
    main = []
    # loop through the IDs
    for a in ids:
        # get request from the API
        r = rq.get(f'{baseurl}{endpoint}/{a}?ts={ts}&apikey={api_key}&hash={hash_key}')
        # return json string
        data = r.json()
        # append to main list
        main.append(data)

    characters = []
    for response in main:
        results = response['data']['results']
        
        for details in results:
            xter = {
                'id': details['id'],
                'name': details['name'],
                'description': details['description'],
                'modified_date': details['modified']
            }
            characters.append(xter)
    return pd.DataFrame(characters)

#################################################################################################################

def get_series():
    # list for all character IDs details
    main = []
    # loop through the IDs
    for a in ids:
        # get request from the API
        r = rq.get(f'{baseurl}{endpoint}/{a}{series_e}?ts={ts}&apikey={api_key}&hash={hash_key}')
        # return json string
        data = r.json()
        # append to main list
        main.append(data)
    series_list = []
    for response in main:
        results = response['data']['results']
        
        for details in results:
            series_ = {
                'id': details['id'],
                'title': details['title'],
                'description': details['description'],
                'modified_date': details['modified'],
                'start_year': details['startYear'],
                'end_year': details['endYear'],
                'rating': details['rating'],
                'type': details['type'],
                'character_id': details['characters']['items'][0]['resourceURI'].replace('/',' ').split()[-1],
                'comics_id': details['comics']['items'][0]['resourceURI'].replace('/',' ').split()[-1]
            }
            series_list.append(series_)              
    return pd.DataFrame(series_list)

################################################################################################################

# define database connect function
def connect_db():
    print('Connecting to Marvel Database...')

    # login to marvel_db database
    conn = create_engine(f'postgresql://root:root@localhost:5432/marvel_db')
    # check connection if successful
    conn.connect()
    return conn

################################################################################################################## 

def run_etl():
    conn = connect_db()
    # save characters table to marvel_db
    get_character().to_sql(name='characters', con=conn, index=False, if_exists='replace')
    # save comics table to marvel_db
    get_comics().to_sql(name='comics', con=conn, index=False, if_exists='replace')
    # save events table to marvel_db
    get_events().to_sql(name='events', con=conn, index=False, if_exists='replace')
    # save series table to marvel_db
    get_series().to_sql(name='series', con=conn, index=False, if_exists='replace')
    # save stories table to marvel_db
    get_stories().to_sql(name='stories', con=conn, index=False, if_exists='replace')

run_etl()