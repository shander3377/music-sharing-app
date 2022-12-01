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
CLIENT = None
IP_ADDRESS = "127.0.0.1"
PORT = 8000
BUFFER_SIZE = 4096
song_selected = None
song_counter = 0
listbox = None
infoLabel = None
mixer.init()

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

    uploadButton = Button(window, text="Upload", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    uploadButton.place(x=30, y=225)

    downloadButton = Button(window, text="Download", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    downloadButton.place(x=200, y=225)

    resumeButton = Button(window, text="Resume", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10), command=resume)
    resumeButton.place(x=30, y=250)

    pauseButton = Button(window, text="Pause", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10), command=pause)
    pauseButton.place(x=200, y=250)
    
    infoLabel = Label(window, text=" ", fg="blue", font=("Calibri", 8))
    infoLabel.place(x=4, y=275)
    window.mainloop()

setup()