from mutagen.mp3 import MP3
from mutagen.id3 import error
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC, APIC,TRCK
import os
def dir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
def gpm(track,albumArt,song):
    tags = MP3(song)
    try:
        tags.add_tags()
    except error:
        print("has tags")

    try:
        tags["TRCK"] = TRCK(encoding=3, text=str(track["trackNumber"]))
    except:
        print("  !!! Failed to add track no")
    try:
        tags["TIT2"] = TIT2(encoding=3, text=track["title"])
    except:
        print("  !!! Failed to add title")
    try:
        tags["TALB"] = TALB(encoding=3, text=track["album"])
    except:
        print("  !!! Failed to add album")
    try:
        tags["COMM"] = COMM(encoding=3, lang=u'eng', desc='desc', text=u'Downloaded from GPM')
    except:
        print("  !!! Failed to add comment")
    try:
        tags["TPE1"] = TPE1(encoding=3, text=track["artist"])
    except:
        print("  !!! Failed to add artist")
    try:
        tags["TPE2"] = TPE2(encoding=3, text="Various Artists")
    except:
        print("  !!! Failed to add album artist")
    try:
        tags["TCOM"] = TCOM(encoding=3, text=track["composer"])
    except:
        print("  !!! Failed to add composer")
    try:
        tags["TCON"] = TCON(encoding=3, text=track["genre"])
    except:
        print("  !!! Failed to add genre")
    try:
        tags["TDRC"] = TDRC(encoding=3, text=str(track["year"]))
    except:
        print("  !!! Failed to add year")

    tags["APIC"] = APIC(
            encoding=3, # 3 is for utf-8
            mime='image/png', # image/jpeg or image/png
            type=3, # 3 is for the cover image
            desc=u'Cover',
            data=open(albumArt,"rb").read()
        )
    output = "output/" + track["albumArtist"] + "/" + track["album"].replace("/", "slash").replace("|", "pipe") + "/" + track["title"] + ".mp3"
    dir("output")
    dir("output/" + track["albumArtist"])
    dir("output/" + track["albumArtist"] + "/" + track["album"].replace("/", "slash").replace("|", "pipe"))
    tags.save(song)
    os.rename(song, output)
    os.remove(albumArt)