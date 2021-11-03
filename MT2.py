#! /usr/bin/python
#  _____                 _       __  __ _              _
# |_   _|__  _ __  _   _( )___  |  \/  | |_ ___   ___ | |
#   | |/ _ \| '_ \| | | |// __| | |\/| | __/ _ \ / _ \| |
#   | | (_) | | | | |_| | \__ \ | |  | | || (_) | (_) | |
#   |_|\___/|_| |_|\__, | |___/ |_|  |_|\__\___/ \___/|_|
#                  |___/
#
# Created by SamuR4II
#

from time import sleep
from colored import fg, bg, attr
from os import system,name
import os, glob, sys
import random

# --

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def Main():
    allcolors = [4,5,6]
    count = 5

    for i in range(1):

        R_color = random.choice(allcolors)
        R_color2 = random.choice(allcolors)

        if R_color2 == R_color:
            if R_color2 < 5:
                R_color2 = R_color2 + 1
            elif R_color2 > 5:
                R_color2 = R_color2 - 1
            else:
                R_color2 = R_color2 - 1

        sleep(0.15)

        count += 1

        space = " " * 3
        
        print(space, " ___________________")
        print(space, "|_%sT%sony's_%sM%susic_Tool_|" % (fg(R_color), attr(0), fg(R_color2), attr(0)))
        print(space, "|]=================[|")
        if count > 1:
            print(space, "::      -d URL      %s-%s To Download AUDIO only" % (fg(R_color), attr(0)))
        if count > 2:
            print(space, "::      -dv URL     %s-%s To Download VIDEO" % (fg(R_color), attr(0)))
        if count > 3:
            print(space, "::      -c PATH     %s-%s To convert a .webm file" % (fg(R_color), attr(0)))
        if count > 4:
            print(space, "::      -l TYPE     %s-%s To list files. Example: 'MT.exe -l .mp3'" % (fg(R_color), attr(0)))
        if count > 5:
            print(space, "::      -u          %s-%s To Update" % (fg(R_color), attr(0)))
        print(space, "|]_________________[|")
        print("\n")



def Download(url):

    # Download Audio
    if name == 'nt':
        os.system("Programs\youtube-dl.exe -f bestaudio " + url)
    else:
        os.system("youtube-dl -f bestaudio " + url)

    # get File name and print it out
    space = "  " * 2

    allWebm_files = glob.glob("*webm")
    AudioFile = allWebm_files[0]

    print(space, "File -: " + str(AudioFile) + " :: Downloaded!")

    sleep(2)

    # convert .Webm file to .mp3 with ffmpeg

    if name == 'nt':
        os.system('Programs\\ffmpeg.exe -i "' + str(AudioFile) + '" -vn -ab 128k -ar 44100 -y "' + str(AudioFile.replace("webm", "mp3")) + '"')
    else:
        os.system('ffmpeg -i "' + str(AudioFile) + '" -vn -ab 128k -ar 44100 -y "' + str(AudioFile.replace("webm", "mp3")) + '"')

    sleep(0.5)

    print(space, "Succesfully converted .%swebm%s file to .%smp3%s" % (fg(5), attr(0), fg(6), attr(0)))
    sleep(1)

    # --

    print(space, "\nWould you like to keep the .webm file?")

    keep = input(space + "y/n :")

    if keep == "y":
        print("\n" + space, " OK !")
        sleep(1)

    else:
        print("\n" + space + "Destroying .webm FILE !!! ha ha ha ...")

        if name == 'nt':
            os.system('DEL "' + str(AudioFile) + '"')
        else:
            os.system('rm "' + str(AudioFile) + '"')

        sleep(1)

        print(space, str(AudioFile) + "\n     Downloaded!")



def Convert(File_PATH):

    if name == 'nt':
        os.system('Programs\\ffmpeg.exe -i "' + File_PATH + '" -vn -ab 128k -ar 44100 -y "' + File_PATH.replace(".webm",".mp3") + '"')
    else:
        os.system('ffmpeg -i "' + File_PATH + '" -vn -ab 128k -ar 44100 -y "' + File_PATH.replace(".webm",".mp3") + '"')

    sleep(0.5)

    space = "  " * 2
    print(space, "Succesfully Converted!")

def List_Files(file_type):

    files = glob.glob("*" + str(file_type))

    print("\n   :: here is a %slist%s of " % (fg(5), attr(0)) + str(file_type) + " %sfiles%s\n" % (fg(3), attr(0)))
    count = 0

    for file in files:

        count += 1
        print( "  [" + str(count) + "]  " + file)

def Download_Vid(LINK):

    if True:
        try:
            if name == 'nt':
                os.system('Programs\youtube-dl.exe -f best ' + LINK)
            else:
                os.system('youtube-dl -f best ' + LINK)
            sleep(1)

            space = ' ' * 2

            print(space, "Video %sDownloaded%s!\n" % (fg(3), attr(0)))

        except Exception as E:
            print("you did sometin wong...\n")
            sleep(1)
            print(str(E))


def Update():

    space = ' ' * 2

    print("\n")
    print(space, "[ MT %sV%sersion :: 3.5 ]\n" % (fg(4), attr(0)))
    sleep(0.2)
    print("Updating youtube-dl")

    if name == 'nt':
        os.system("Programs\youtube-dl.exe -U")
    else:
        os.system("youtube-dl -U")
        os.system('pip install youtube-dl')


# --

try:

    if sys.argv[1] == "-d":
        Download(sys.argv[2])

    elif sys.argv[1] == "-c":
        Convert(sys.argv[2])

    elif sys.argv[1] == "-l":
        List_Files(sys.argv[2])

    elif sys.argv[1] == "-dv":
        Download_Vid(sys.argv[2])

    elif sys.argv[1] == "-u":
        Update()

    else:
        Main()

except Exception as i:
    Main()

