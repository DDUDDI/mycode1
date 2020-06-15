import socket
import sys
from _thread import *

HOST = '127.0.0.1'
PORT = 1234

def showMenu():
    menu = input('서버접속(s), 종료(x): ')
    return menu

def client_thread(client_socket, ):
        # 로그인 정보를 서버에 보냄
        login = input('id pwd: ')
        client_socket.send(login.encode())

        data = client_socket.recv(1024)
        print('로그인 결과: ', data.decode())


menu = showMenu()
# 서버에 접속하고 접속/실패 메시지 표시
while True:
    if menu == 's':
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((HOST, PORT))
            print('서버 접속 성공')
            start_new_thread(client_thread, (client_socket,))
        except socket.error as e:
            print('서버 접속 실패')
    # 프로그램 종료
    elif menu == 'x':
        sys.exit()
        print('프로그램 종료...')


client_socket.close()