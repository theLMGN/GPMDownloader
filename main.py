
from gmusicapi import Mobileclient
import json
from downloader import download
from tagger import gpm,makeClean
from authentication import *
import os
import shutil
import time

try:
    shutil.rmtree("cache")
except Exception as e:
    print("failed to delete cache, probably nothing to worry about")
    print(e)
os.makedirs("cache")

api = Mobileclient()
logged_in = api.login(GPMEMAIL,GPMPASSWORD,ANDROIDID)

if api.is_subscribed:
    print("you have GPM all access, the app will work fine!")
else:
    print("!! WARN !!: a paid GPM subscription is recommended.")




def plist(plist):
    startTime = time.time()
    print("Starting on " + plist["name"])
    i = 0
    for sog in plist["tracks"]:
        i = i + 1
        try:
            song = sog["track"]
            track = sog["track"]
            if os.path.isfile( "output/" + makeClean(track["albumArtist"]) + "/" + makeClean(track["album"]) + "/" + makeClean(track["title"]) + ".mp3"):
                a = 0
            else:
                print("[" + str(i) + "/" + str(len(plist["tracks"])) + " " + str(int((i / len(plist["tracks"])) * 100)) + "%] Downloading " +  song["title"] + " by " + song["artist"])
                download(api.get_stream_url(song["storeId"]),"cache/" + song["storeId"] + ".mp3")
                print("  Downloading album art")
                download(song["albumArtRef"][0]["url"], "cache/" + song["storeId"] + ".png")
                print("  Tagging")
                gpm(song, "cache/" + song["storeId"] + ".png", "cache/" + song["storeId"] + ".mp3")
        except Exception as e:
            print(sog)
            print(e)
            print("Waiting a second before continuing")
            time.sleep(2)
        
        

playlist = api.get_all_user_playlist_contents()
for val in playlist:
    if val["name"] == PLAYLISTNAME:
        plist(val)
