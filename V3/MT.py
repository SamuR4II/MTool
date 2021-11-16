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
    
    space = " " * 3
    
    print(space, " ___________________")
    print(space, "|_Tony's_Music_Tool_|")
    print(space, "|]=================[|")
    print(space, "::      -d URL      - To Download AUDIO only")
    print(space, "::      -dv URL     - To Download VIDEO")
    print(space, "::      -c PATH     - To convert a .webm file")
    print(space, "::      -l TYPE     - To list files. Example: 'MT.exe -l .mp3'")
    print(space, "::      -u          - To Update")
    print(space, "|]_________________[|\n")



def Download(url):

    clear()

    # Download Audio
    if name == 'nt':
        os.system("Programs\youtube-dl.exe -f bestaudio " + url)
    else:
        os.system("youtube-dl -f bestaudio " + url)

    # get File name and print it out

    clear()
    space = "  " * 2

    allWebm_files = glob.glob("*webm")
    AudioFile = allWebm_files[0]

    print(space, "File -: " + str(AudioFile) + " :: Downloaded!")

    sleep(2)
    clear()

    # convert .Webm file to .mp3 with ffmpeg

    if name == 'nt':
        os.system('Programs\\ffmpeg.exe -i "' + str(AudioFile) + '" -vn -ab 128k -ar 44100 -y "' + str(AudioFile.replace("webm", "mp3")) + '"')
    else:
        os.system('ffmpeg -i "' + str(AudioFile) + '" -vn -ab 128k -ar 44100 -y "' + str(AudioFile.replace("webm", "mp3")) + '"')

    sleep(0.5)

    print(space, "Succesfully converted .webm file to .mp3")
    sleep(1)

    # --

    print(space, "\nWould you like to keep the .webm file?")

    keep = input(space + "y/n :")

    if keep == "y":
        print("\n" + space, " OK !")
        sleep(1)
        clear()

    else:
        print("\n" + space + "Destroying .webm FILE !!! ha ha ha ...")

        if name == 'nt':
            os.system('DEL "' + str(AudioFile) + '"')
        else:
            os.system('rm "' + str(AudioFile) + '"')

        sleep(1)
        clear()

        print(space, str(AudioFile) + "\n     Downloaded!")



def Convert(File_PATH):

    if name == 'nt':
        os.system('Programs\\ffmpeg.exe -i "' + File_PATH + '" -vn -ab 128k -ar 44100 -y "' + File_PATH.replace(".webm",".mp3") + '"')
    else:
        os.system('ffmpeg -i "' + File_PATH + '" -vn -ab 128k -ar 44100 -y "' + File_PATH.replace(".webm",".mp3") + '"')

    sleep(0.5)
    clear()

    space = "  " * 2
    print(space, "Succesfully Converted!")

def List_Files(file_type):

    files = glob.glob("*" + str(file_type))

    print("\n   :: here is a list of " + str(file_type) + " files\n")
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

            clear()

            space = ' ' * 2

            print(space, "Video Downloaded!\n")

        except Exception as E:
            print("you did sometin wong...\n")
            sleep(1)
            print(str(E))


def Update():

    space = ' ' * 2

    print("\n")
    print(space, "[ MT Version :: 3.5 ]\n")
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

