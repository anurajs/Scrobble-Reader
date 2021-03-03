import requests
import time
import json


class Song():
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __hash__(self):
        return hash((self.title, self.artist))

    def __eq__(self, value):
        if value is None:
            return False
        return self.title == value.title and self.artist == value.artist


conf = dict()

with open("config.json", 'r') as file:
    conf = json.loads(file.read())


api_key = conf['api_key']
user = conf['user']
url = 'http://ws.audioscrobbler.com/2.0/'

payload = {
    'method': 'user.getrecenttracks',
    'api_key': api_key,
    'format': 'json',
    'user': user,
    'limit': 1
}

lastSong = None
while(True):
    r = requests.get(url, payload)
    details = r.json()
    details = details['recenttracks']['track'][0]
    name = details['name']
    artist = details['artist']['#text']
    s = Song(name, artist)
    if s == lastSong:
        time.sleep(4)
        continue
    file = open("nowplaying.txt", 'w', encoding='utf-8')
    file.write('<<' + name + ' | ' + artist + ">>  ")
    print('<<' + name + ' | ' + artist + ">> ")
    lastSong = s
    r.close()
    file.close()
    time.sleep(4)
