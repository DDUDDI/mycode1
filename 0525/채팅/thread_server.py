import socket
from _thread import *


def threaded(client_socket, addr):
    print('Connected by: ', addr[0], ':', addr[1])
    while True:
        try:
            data = client_socket.recv(1024) # TCP socket 사용
            if not data:
                print('Disconnected by ' + addr[0], ':', addr[1])
                break
            print('Recceived from' + addr[0], ':', addr[1], data.decode()) # 여기를 바꿔야함
            for c in client_list:
                if c[0] != client_socket:
                    c[0].send(data) # 앞에 IP 주소 붙이면 누가 보낸 메세지인지 알 수 있음
            # client_socket.send(data) # TCP이므로 받는 곳의 주소 X
        except ConnectionResetError as e:
            print('Disconnected by ' + addr[0], ':', addr[1])
            break
    client_socket.close()


HOST = '127.0.0.1'
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()
print('server start')

while True:
    print('Server waiting...')
    client = server_socket.accept()
    client_list = []
    client_list.append(client)
    # (client_socket, addr) = server_socket.accept()
    start_new_thread(threaded, client) # start_new_thread: 가상의 CPU(thread)로 threaded func를 실행하겠다

server_socket.close()
