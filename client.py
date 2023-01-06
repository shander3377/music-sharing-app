import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound
import pygame
from pygame import mixer
import os
import time
import ftplib
from ftplib import FTP
import ntpath
from pathlib import Path
CLIENT = None
IP_ADDRESS = "127.0.0.1"
PORT = 8000
BUFFER_SIZE = 4096
song_selected = None
song_counter = 0
listbox = None
infoLabel = None
mixer.init()


def browse_files():
    global infoLabel
    global listbox
    global song_counter

    try:
        filename = filedialog.askopenfilename()
        HOSTNAME = "127.0.0.1"
        USERNAME = "user"
        PASSWORD = "12345"

        ftp_server = FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = "utf-8"
        ftp_server.cwd('shared_files')
        fname = ntpath.basename(filename)
        with open(filename, 'rb') as file:
            ftp_server.storbinary(f"STOR {fname}", file)
        ftp_server.dir()
        ftp_server.quit()

        listbox.insert(song_counter, fname)
        song_counter = song_counter+1
    except FileNotFoundError:
        print("Cancel Button Pressed")

def download():
    global song_selected
    song_selected = listbox.get(ANCHOR)
    song_to_download = listbox.get(ANCHOR)
    infoLabel.configure(text="Downloading" + song_to_download + "...")
    HOSTNAME = "127.0.0.1"
    USERNAME = "user"
    PASSWORD = "12345"
    home = str(Path.home())
    download_path = home+"\\Downloads"
    download_path="E:\Downloads"
    ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
    ftp_server.encoding = "utf-8"
    ftp_server.cwd("shared_files")
    local_file_name =  os.path.join(download_path, song_to_download)
    file = open(local_file_name, 'wb')
    ftp_server.retrbinary('RETR '+ song_to_download, file.write)
    ftp_server.dir()
    file.close()
    ftp_server.quit()
    infoLabel.configure(text="Succesfully downloaded " + song_to_download)
    time.sleep(1)
    print(song_selected)
    if song_selected != "":
        infoLabel.configure(text="Now playing " + song_selected)
    else:
        infoLabel.configure(text="")

def resume():
    global song_selected
    global listbox
    global infoLabel
    mixer.music.unpause()
def pause():
    global song_selected
    global listbox
    global infoLabel
    mixer.music.pause()

def play():
    global song_selected
    global listbox
    global infoLabel
    song_selected = listbox.get(ANCHOR)
    mixer.music.load("shared_files/"+song_selected)
    mixer.music.play()

    if(song_selected != ""):
        infoLabel.configure(text="Now Playing: "+ song_selected)
    else:
        infoLabel.configure(text="")

def stop():
    global song_selected
    global infoLabel
    mixer.music.stop()
    infoLabel.configure(text="")
def setup():
    global CLIENT
    CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    CLIENT.connect((IP_ADDRESS, PORT))
    musicWindow()
def musicWindow():
    global song_counter
    global listbox
    global infoLabel

    window = Tk()
    window.title("Music Window")
    window.geometry("300x300")
    window.configure(bg='lightskyblue')

    selectsong = Label(window, text="Select Song", bg="LightSkyBlue", font=("Calibri", 8))
    selectsong.place(x=2, y=1)

    listbox = Listbox(window, activestyle="dotbox", bg="LightSkyBlue", height=10, width=39, borderwidth=2, font=("Calibri", 10))
    listbox.place(x=10, y=18)

    for file in os.listdir("shared_files"):
        filename = os.fsdecode(file)
        listbox.insert(song_counter, filename)
        song_counter = song_counter +1

    scrollbar1= Scrollbar(listbox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(command = listbox.yview)

    playButton = Button(window, bd=1, width=10, text="Play", bg="SkyBlue", command=play, font=("Calibri", 10))
    playButton.place(x=30, y=200)

    stopButton = Button(window, bd=1, command=stop, text="Stop", width=10, bg="SkyBlue", font=("Calibri", 10))
    stopButton.place(x=200, y=200)

    uploadButton = Button(window, text="Upload", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10), command=browse_files)
    uploadButton.place(x=30, y=225)

    downloadButton = Button(window, text="Download", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10), command=download)
    downloadButton.place(x=200, y=225)

    resumeButton = Button(window, text="Resume", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10), command=resume)
    resumeButton.place(x=30, y=250)

    pauseButton = Button(window, text="Pause", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10), command=pause)
    pauseButton.place(x=200, y=250)
    
    infoLabel = Label(window, text=" ", fg="blue", font=("Calibri", 8))
    infoLabel.place(x=4, y=275)
    window.mainloop()

setup()