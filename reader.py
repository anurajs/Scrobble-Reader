import requests
import time
import json 

conf = open("config.json",'r')
conf = json.loads(conf.read())

api_key = conf['api_key']
user = conf['user']
url = 'http://ws.audioscrobbler.com/2.0/'

payload= {
    'method':'user.getrecenttracks',
    'api_key':api_key,
    'format':'json',
    'user':user,
    'limit':1
}

while(True):
    r = requests.get(url,payload)
    details = r.json()
    details = details['recenttracks']['track'][0]
    artist = details['artist']['#text']
    name = details['name']
    file = open("nowplaying.txt",'w',encoding='utf-8')
    file.write('<<'+ name + ' | ' + artist + ">>  ")
    print('<<'+ name + ' | ' + artist + ">> ")
    r.close()
    file.close()
    time.sleep(4)