const fs = require('fs');
const axios = require('axios').default
require('dotenv').config()

payload = {
    'method':'user.getrecenttracks',
    'api_key': process.env.API_KEY,
    'format':'json',
    'user': process.env.USER_NAME,
    'limit':1
}

lastSong = null

const getSong = (payload) => {
    const url = 'http://ws.audioscrobbler.com/2.0/'
    return new Promise((resolve, reject) => {
        axios.get(url,{params:payload}).then(resp =>{
            let details = resp.data;
            details = details['recenttracks']['track'][0]
            if(details['@attr'] && details['@attr'].nowplaying){
                let song = {
                    name:details['name'],
                    artist:details['artist']['#text']
                }
                resolve(song)
            }else{
                reject("Not listening to anything")
            }
        }).catch(err=>{
            if(err.response.data.error == 6){
                reject("Check your api key or username in the .env file")
            }else {
                reject(err.response.data.message)
            }
        }
    )})
}

setInterval(()=>{
    getSong(payload).then(song => {
        if(JSON.stringify(song) == JSON.stringify(lastSong)){
            return
        }
        lastSong = song
        console.log(song);
        fs.writeFileSync('nowplaying.txt',`<< ${song.name} | ${song.artist} >>  `)
    }).catch(err => {
       console.log(err) 
    })
},4000)