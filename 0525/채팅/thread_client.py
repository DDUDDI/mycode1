import socket
from _thread import *

HOST = '127.0.0.1'
PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def client_thread(client_socket, ):
    while True:
        data = client_socket.recv(1024)
        print('Received from the server: ', repr(data.decode()))

start_new_thread(client_thread, (client_socket, ))

while True:
    message = input('Enter Message: ')
    if message == 'quit':
        break
    client_socket.send(message.encode())

client_socket.close()