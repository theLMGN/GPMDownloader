# GPMDownloader

Downloads music from GPM in 320kbps MP3 format.

## Requirements

Python3 - a recent version please, tested under 3.7

A **paid** GPM account

Some understanding on how to edit config files and work around the CLI. 

## Installation

1. Install Python 3.
2. Open the CLI and point it to where you downloaded GPMDownloader
3. `pip install -r requirements.txt`
4. Rename `authentication.1.py` to `authentication.py`
5. Open in a text editor such as Notepad++ (win) or BBEdit (mac).
6. Fill in the `GPMEMAIL` field with your Gmail address, and `GPMPASSWORD` with an app password generated at https://myaccount.google.com/apppasswords.
7. Save the file
8. `python androidids.py`
9. Find an Android device, like so

```
---
Device Name: No carrier Nexus 6P
Device OS: ANDROID
Device ID: 0x0123456789abcdef
---
```

10. Remove the `0x` from the start of the device id, so it looks something like this `0123456789abcdef` and put it in the `ANDROIDID` field of the authentication file
11. Fill in the playlist name
12. Save the file.

Then, simply run the `main.py` script.

## Thanks
**gmusicapi** for the interface with Google Play and providing download URLS.

**mutagen** ID3 tagging library for Python.