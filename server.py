import socket
from threading import Thread
SERVER = None
IP_ADDRESS = "127.0.0.1"
PORT = 8000
BUFFER_SIZE = 4096
clients = {}

def setup():
    global SERVER
    global IP_ADDRESS
    global PORT
    global BUFFER_SIZE
    global clients

    print("MUSIC SHARING PLATFORM")
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)
    
    print("SERVER IS READY")
    print("WAITING FOR CONNECTIONS")
    print("\n\n\n")

    acceptConnections()

setup_thread = Thread(target=setup)
setup_thread.start()

def acceptConnections():
    global SERVER
    global clients

    while(True):
        client, addr = SERVER.accept()
        print(client,addr)


