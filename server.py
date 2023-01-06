import socket
from threading import Thread
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
SERVER = None
IP_ADDRESS = "127.0.0.1"
PORT = 8000
BUFFER_SIZE = 4096
clients = {}
if(not os.path.isdir('shared_files')):
    os.makedirs('shared_files')
def ftp():
    global IP_ADDRESS
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345',".", perm='elradfmw')
    handler = FTPHandler
    handler.authorizer = authorizer
    ftp_server = FTPServer((IP_ADDRESS, 21), handler)
    ftp_server.serve_forever()
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

ftp_thread = Thread(target=ftp)
ftp_thread.start()
# def handleClient(client, client_name):

def acceptConnections():
    global SERVER
    global clients

    while(True):
        client, addr = SERVER.accept()
        client_name = client.recv(2048).decode().lower()
        clients[client_name] = {
            "client": client,
            "address": addr,
            "connected_with": "",
            "file_name": "",
            "file_size": 4096
        }
        print(f"Connection established with {client} ,{addr}")
        # thread = Thread(target=handleClient, args=(client, client_name))
        # thread.start()


