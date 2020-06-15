import socket
from _thread import *

# threaded 함수 정의
# parameter: client_sockeet, addr
def threaded(client_socket, addr):
    print('Connected by: ', addr[0], ':', addr[1])
    while True:
        try:
            # TCP 소켓을 사용하므로 socket.recv(buffer)
            # 데이터 수신 (client -> server)
            data = client_socket.recv(1024)
            # client로 부터 data가 전송되지 않으면 while loop 종료
            if not data:
                print('Disconnected by ' + addr[0], ':', addr[1])
                break
            # client로 부터 data가 전송되면 data decoding해서 출력
            print('Received from' + addr[0], ':', addr[1], data.decode())
            # 데이터 전송 (server -> client)
            client_socket.send(data.encode())
        except ConnectionResetError as e:
            print('Disconnected by ' + addr[0], ':', addr[1])
            break
        # client 소켓 종료
        client_socket.close()

HOST = '127.0.0.1'
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()
print('Server start')

while True:
    print('Server waiting...')
    (client_socket, addr) = server_socket.accept()
    # start_new_thread(): 가상의 CPU(thread)로 client가 요청할 때 마다 threaded func를 실행하겠다
    # 2. receive[client -> server] -> 3. send[server -> client]
    start_new_thread(threaded, (client_socket, addr))

server_socket.close()