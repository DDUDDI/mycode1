from _thread import *
import sys
import socket


def showMenu():
    menu = input('서버접속(s), 종료(x): ')
    return menu


HOST = '127.0.0.1'
PORT = 1234
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    menu = showMenu()
    if menu == 's':
        try: # 접속 먼저 실행
            client_socket.connect((HOST, PORT))
            logininfo = input('ID PWD: ')
            client_socket.send(logininfo.encode()) # sendall: 확실히 보냄

            data = client_socket.recv(1024)
            ok = int(data.decode())
            if ok:
                print('로그인 성공')
                print('채팅 서버 접속...')
                break
            else:
                print('로그인 실패')
        except Exception as e:
            print(e)
            print('접속 실패')
            sys.exit()
    elif menu == 'x':
        print('프로그램 종료...')
        sys.exit()


def recv_thread(client_socket, ): # 수신용 쓰레드
    while True:
        data = client_socket.recv(1024)
        print('>>> ', repr(data.decode()))

start_new_thread(recv_thread, (client_socket, ))
# repr이 무엇인가

while True: # 송신용 쓰레드
    message = input('Enter Message: ')
    if message == 'quit':
        print('채팅 서버 종료...')
        break
    client_socket.send(message.encode())


client_socket.close()
