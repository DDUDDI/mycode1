import socket
from _thread import *

def client_thread(client_socket, ):
    while True:
        # 데이터 수신 (server -> client)
        data = client_socket.recv(1024)

HOST = '127.0.0.1'
PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# 4. receive[server -> client]
# 왜 receive를 먼저 실행할까..............?
start_new_thread(client_thread, (client_socket,))

# 1. send[client -> server]
while True:
    message = input('Enter message: ')
    if message == 'quit':
        break
    client_socket.send(message.encode())

client_socket.close()