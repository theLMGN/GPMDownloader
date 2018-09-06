from gmusicapi import Mobileclient
from authentication import *

api = Mobileclient()
logged_in = api.login(GPMEMAIL,GPMPASSWORD,Mobileclient.FROM_MAC_ADDRESS)

devices = api.get_registered_devices()

for device in devices:
    print("---")
    try:
        print("Device Name: " + device["friendlyName"])
    except:
        print("Device Name: ???")
    print("Device OS: " + device["type"])
    print("Device ID: " + device["id"])