import os
from subprocess import Popen

def darwinN(title,text):
    Popen(['/usr/local/bin/terminal-notifier', '-group','gpm-dl','-title','GPM Downloader', '-subtitle',title, '-message', text,">/dev/null"])

def notify(title,text):
    if os.path.isfile("/usr/local/bin/terminal-notifier"):
        darwinN(title,text)