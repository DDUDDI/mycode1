import pymysql
import sys
import socket
from _thread import *

def conn_mysql():
    try:
        conn = pymysql.connect(host='localhost', user='root',
                               password='tjoeun', db='test', charset='utf8')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        print('MySQL DB에 접속 성공 !!')
        return conn, curs
    except pymysql.MySQLError as e:
        print(e)
        sys.exit()
        return None

def user_login(id, pwd):
    (conn, curs) = conn_mysql()
    sql = 'select pwd from login where id == %s'
    curs.execute(sql, (id))
    row = curs.fetchall()
    if row['pwd'] == pwd:
        conn.commit()
        msg = '로그인 성공'
        return msg
    else:
        msg = '로그인 실패'
        return msg
    conn.close()

def threaded(client_socket, addr):
    print('Connected by: ', addr[0], ':', addr[1])
    while True:
        try:
            # client로부터 login 정보를 받음
            data = client_socket.recf(1024)
            if not data:
                print('Disconnected by ' + addr[0], ':', addr[1])
                break
            # db에서 로그인 정보 확인
            data = data.decode()
            logininfo = data.splint
            loginres = user_login(logininfo[0])
            for c in client_list:
                if c[0] != client_socket:
                    c[0].send(loginres) # login 성공 여부 return

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
    client_list = []
    client_list.append(client)
    start_new_thread(threaded, client)
server_socket.close()