import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
CLIENT = None
IP_ADDRESS = "127.0.0.1"
PORT = 8000
BUFFER_SIZE = 4096

def setup():
    global CLIENT
    CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    CLIENT.connect((IP_ADDRESS, PORT))
    musicWindow()
def musicWindow():
    window = Tk()
    window.title("Music Window")
    window.geometry("300x300")
    window.configure(bg='lightskyblue')

    selectsong = Label(window, text="Select Song", bg="LightSkyBlue", font=("Calibri", 8))
    selectsong.place(x=2, y=1)

    listbox = Listbox(window, activestyle="dotbox", bg="LightSkyBlue", height=10, width=39, borderwidth=2, font=("Calibri", 10))
    listbox.place(x=10, y=18)

    scrollbar1= Scrollbar(listbox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(command = listbox.yview)

    playButton = Button(window, bd=1, width=10, text="Play", bg="SkyBlue", font=("Calibri", 10))
    playButton.place(x=30, y=200)

    stopButton = Button(window, bd=1, text="Stop", width=10, bg="SkyBlue", font=("Calibri", 10))
    stopButton.place(x=200, y=200)

    uploadButton = Button(window, text="Upload", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    uploadButton.place(x=30, y=250)

    downloadButton = Button(window, text="Download", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    downloadButton.place(x=200, y=250)

    infoLabel = Label(window, text=" ", fg="blue", font=("Calibri", 8))
    infoLabel.place(x=4, y=250)
    window.mainloop()

setup()