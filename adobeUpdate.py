#!/usr/bin/python3
#This script will keep your Adobe Flash up to date
#By Martino Jones
#20151014
import os

def getFlashUpdate():
        url = "wget -nc https://fpdownload.macromedia.com/get/flashplayer/pdc/" + flashVersion + "/install_flash_player_osx.dmg -O flashplayer" + flashVersion + ".dmg"
        print(url)
        os.system(url)


print("Getting latest version")
flashVersion = os.popen("/usr/bin/curl -s http://www.adobe.com/software/flash/about/ | sed -n '/Safari/,/<\/tr/s/[^>]*>\([0-9].*\)<.*/\\1/p'").read()
flashVersion = flashVersion.split("\n")[0]
print("Latest version is: " + flashVersion)

#Get local flash version
currentDownload = ""
for file in os.listdir(os.curdir):
    if file.startswith("flashplayer"):
        currentDownload = file
if not currentDownload == "":
    print("Your version is: " + currentDownload.split("flashplayer")[1].split(".dmg")[0] + " and the current version is: " + flashVersion)

    if currentDownload.split("flashplayer")[1].split(".dmg")[0] < flashVersion:
        print("Downloading new version...")
        getFlashUpdate()

else:
    print("You don't have a version of Flash downloaded, I will do that for you!")
    getFlashUpdate()
