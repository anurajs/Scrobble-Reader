import requests
import time


url = 'http://ws.audioscrobbler.com/2.0/'

payload= {
    'method':'user.getrecenttracks',
    'api_key':api_key,
    'format':'json',
    'user':user,
    'limit':1
}

while(True):
    time.sleep(4)
    r = requests.get(url,payload)
    details = r.json()
    details = details['recenttracks']['track'][0]
    artist = details['artist']['#text']
    name = details['name']
    file = open("nowplaying.txt",'w',encoding='utf-8')
    file.write('<<'+ name + ' | ' + artist + ">> ")
    print('<<'+ name + ' | ' + artist + ">> ")
    r.close()
    file.close()