import requests
import json
import nlp
import os

URL = "https://api.twitter.com/2/tweets/search/recent"

def listToString(keywords): 
    string = "" 

    for word in keywords: 
        string = string + " " + word
 
    return string

def searchTweets(keywords):
    params = {
        'query': listToString(keywords),
        'expansions': 'author_id'
    }

    file = open('auth.json',)
    auth = json.load(file)

    headers = auth

    classifiedData = {
        'donor': []
    }

    while (len(classifiedData['donor']) < 4):
        r = requests.get(url = URL, params = params, headers = headers)
        data = r.json()
        authors = data['includes']['users']
        for tweet in data['data']:
            if len(tweet['text'])<256:
                intent = nlp.natlangpro(tweet['text'])
                intent=intent[0].lower()
                if (intent == 'donate'):
                    for author in authors:
                        if (author['id'] == tweet['author_id']):
                            classifiedData['donor'].append('https://twitter.com/{}/status/{}'.format(author['username'],tweet['id']))
                    
        
        params['next_token'] = data['meta']['next_token']

    return classifiedData['donor']

