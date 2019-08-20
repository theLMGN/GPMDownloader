
from gmusicapi import Mobileclient
import json
from downloader import download
from tagger import tagGPM,makeClean
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

library = []

if DOWNLOADLIBRARY:
    print("Downloading list of songs in library, this may take a while!")
    library = api.get_all_songs()
    print(f"Downloaded list of {len(library)} songs in library")



def plist(plist):
    startTime = time.time()
    print("Starting on " + plist["name"])
    i = 0
    for sog in plist["tracks"]:
        i = i + 1
        try:
            song = {}
            if sog["trackId"].startswith('T'):
                song = sog["track"]
                song["trackId"] = song["storeId"]
            else:
                found = False
                for s in library:
                    if sog["trackId"] == s["id"]:
                        found = True
                        song = s
                        song["trackId"] = sog["trackId"]
                if not found:
                    raise Exception("Song not found in library")
            if os.path.isfile( "output/" + makeClean(song["albumArtist"]) + "/" + makeClean(song["album"]) + "/" + makeClean(song["title"]) + ".mp3"):
                a = 0
            else:
                print("[" + str(i) + "/" + str(len(plist["tracks"])) + " " + str(int((i / len(plist["tracks"])) * 100)) + "%] Downloading " +  song["title"] + " by " + song["artist"])
                download(api.get_stream_url(song["trackId"]),"cache/" + song["trackId"] + ".mp3")
                print("  Downloading album art")
                download(song["albumArtRef"][0]["url"], "cache/" + song["trackId"] + ".png")
                print("  Tagging")
                tagGPM(song, "cache/" + song["trackId"] + ".png", "cache/" + song["trackId"] + ".mp3")
        except Exception as e:
            print(sog)
            print(e)
            print("Waiting a second before continuing")
            time.sleep(2)
        
        

playlist = api.get_all_user_playlist_contents()
for val in playlist:
    if val["name"] == PLAYLISTNAME:
        plist(val)
