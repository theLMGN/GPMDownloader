
from gmusicapi import Mobileclient
import json
from downloader import download
from tagger import gpm
from authentication import *
from notification import *
import os
import time

try:
    os.rmdir("cache")
os.makedirs("cache")

api = Mobileclient()
playlistName = PLAYLISTNAME
logged_in = api.login(GPMEMAIL,GPMPASSWORD,ANDROIDID)

notify("Starting","Downloading " + playlistName)
def plist(plist):
    startTime = time.time()
    print("Starting on " + plist["name"])
    i = 0
    for sog in plist["tracks"]:
        i = i + 1
        try:
            song = sog["track"]
            print("[" + str(i) + "/" + str(len(plist["tracks"])) + " " + str(int((i / len(plist["tracks"])) * 100)) + "%] Downloading " +  song["title"] + " by " + song["artist"])
            if os.path.isfile("output/" + song["albumArtist"] + "/" + song["album"] + "/" + song["title"] + ".mp3"):
                print("Already exists.")
            else:
                notify(str(int((i / len(plist["tracks"])) * 100)) + " Downloaded","Downloading " +  song["title"] + " by " + song["artist"])
                download(api.get_stream_url(song["storeId"]),"cache/" + song["storeId"] + ".mp3")
                print("  Downloading album art")
                download(song["albumArtRef"][0]["url"], "cache/" + song["storeId"] + ".png")
                print("  Tagging")
                gpm(song, "cache/" + song["storeId"] + ".png", "cache/" + song["storeId"] + ".mp3")
        except Exception as e:
            print(e)
            print("Waiting a second before continuing")
            sleep(2)
    notify("Done downloading","Downloaded " + str(i) + " tracks in " + str(time.time() - startTime) + "s")
        
        

playlist = api.get_all_user_playlist_contents()
for val in playlist:
    if val["name"] == playlistName:
        plist(val)
