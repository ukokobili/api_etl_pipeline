# import request library: for making request to the API
import requests as rq
import pprint as pp
import pandas as pd
import hashlib # working of MD5 (byte - byte)

# import keys and ts variables saved in the .env file
api_key = 'xxxxxxxxx'
private_key = 'xxxxxxx'
ts = '1000'

# assign the based url
baseurl = 'http://gateway.marvel.com'

# endpoints 
character_endpoint = '/v1/public/characters'
comics_endpoint = '/v1/public/comics'
creators_endpoint = '/v1/public/creators'
events_endpoint = '/v1/public/events'
series_endpoint = '/v1/public/series'
stories_endpoint = '/v1/public/stories'


# https://www.pythonpool.com/python-md5/
result = hashlib.md5((ts+private_key+api_key).encode()) 
hash_key = result.hexdigest() 


# defining function to call the api
def main_request(baseurl, endpoint, ts, api_key, hash_key):
    # make request to the API with the GET
    r = rq.get(f'{baseurl}{endpoint}?ts={ts}&apikey={api_key}&hash={hash_key}')
    # assign the output into a new variable
    data = r.json()
    # return the a list and dictionary of the schema
    return data['data']

# defining the character function
def xter_data():
  # # pulling the character data from API and assigning to a variable 
  response = main_request(baseurl, character_endpoint, ts, api_key, hash_key)
  # create a list to store output
  xter_list = []
  # loop through the dictionary and append the required values
  for x in response['results']:
    # assigning the key-pair values 
    xter = {
        'id': x['id'],
        'name': x['name'],
        'description': x['description'],
        'modified_date': x['modified'],
        'featured_comics': x['comics']['available'],
        'featured_series': x['series']['available'],
        'featured_stories': x['stories']['available'],
        'featured_events': x['events']['available']
    }
    # append the result to the list above
    xter_list.append(xter)
  # return a dataframe of the appended list
  return pd.DataFrame(xter_list)

# defining the comics function
def comic_data():
  # pulling the comics data from API and assigning to a variable 
  response = main_request(baseurl, comics_endpoint, ts, api_key, hash_key)
  # create a list to store output
  comic_list = []
  # loop through the dictionary and append the required values
  for x in response['results']:
    # assigning the key-pair values
    comics = {
          'id': x['id'],
          'title': x['title'],
          'description': x['description'],
          'modified_date': x['modified'],
          'isbn' : x['isbn'],
          'number_of_pages': x['pageCount'],
          'price': x['prices'][0]['price']
    }
    # append the result to the list above
    comic_list.append(comics)
  # return a dataframe of the appended list
  return pd.DataFrame(comic_list)

#  defining the creators function
def creators_data():
  # pulling the creators data from API and assigning to a variable
  response = main_request(baseurl, creators_endpoint, ts, api_key, hash_key)
  # create a list to store output
  creators_list = []
  # loop through the dictionary and append the required values
  for x in response['results']:
    # assigning the key-pair values
    creators = {
          'id': x['id'],
          'full_name': x['fullName'],
          'modified_date': x['modified']
    }
    # append the result to the list above
    creators_list.append(creators)
  # return a dataframe of the appended list
  return pd.DataFrame(creators_list)

# defining the events function
def events_data():
  # pulling the events data from API and assigning to a variable
  response = main_request(baseurl, events_endpoint, ts, api_key, hash_key)
  # create a list to store output
  events_list = []
  # loop through the dictionary and append the required values
  for x in response['results']:
    # assigning the key-pair values
    events = {
          'id': x['id'],
          'title': x['title'],
          'description': x['description'],
          'modified_date': x['modified'],
          'start_date' : x['start'],
          'end_date': x['end']
    }
    # append the result to the list above
    events_list.append(events)
  # return a dataframe of the appended list
  return pd.DataFrame(events_list)

# defining the series function
def series_data():
  # pulling the series data from API and assigning to a variable
  response = main_request(baseurl, series_endpoint, ts, api_key, hash_key)
  # create a list to store output
  series_list = []
  # loop through the dictionary and append the required values
  for x in response['results']:
    # assigning the key-pair values
    series = {
          'id': x['id'],
          'title': x['title'],
          'description': x['description'],
          'modified_date': x['modified'],
          'end_year': x['endYear'],
          'rating' : x['rating']
    }
    # append the result to the list above
    series_list.append(series)
  # return a dataframe of the appended list
  return pd.DataFrame(series_list)

# defining the stories function
def stories_data():
  # pulling the stories data from API and assigning to a variable
  response = main_request(baseurl, stories_endpoint, ts, api_key, hash_key)
  # create a list to store output  
  stories_list = []
  # loop through the dictionary and append the required values
  for x in response['results']:
    # assigning the key-pair values
    stories = {
          'id': x['id'],
          'title': x['title'],
          'description': x['description'],
          'modified_date': x['modified'],
          'original_issue' : x['originalIssue']['name']
    }
    # append the result to the list above
    stories_list.append(stories)
  # return a dataframe of the appended list
  return pd.DataFrame(stories_list)

