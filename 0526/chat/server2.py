import socket
from _thread import *
from chat_login import *

client_list = []

def login_thread(client_socket, addr):
    data = client_socket.recv(1024)
    data = data.decode()
    # print('서버에서 수신', data) # debuging 용
    userinfo = data.split()
    uid = userinfo[0]
    pwd = userinfo[1]
    ok = authenticate(uid, pwd)
    if ok:
        client_socket.send('1'.encode())
    else:
        client_socket.send('0'.encode())
    print('로그인 쓰레드 종료...')
    client_list.append((client_socket, addr))
    start_new(chat_thread, (client_socket, addr))

def chat_thread(client_socket, addr):
    print('Connected by: ', addr[0], ':', addr[1])
    while True:
        try:
            data = client_socket.recv(1024) # TCP socket 사용
            if not data:
                print('Disconnected by ' + addr[0], ':', addr[1])
                break
            print('Received from' + addr[0], ':', addr[1], data.decode())
            client_socket.send(data) # TCP이므로 받는 곳의 주소 X
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
    print('server waiting...')
    client = server_socket.accept()
    start_new_thread(login_thread, client)


server_socket.close()


