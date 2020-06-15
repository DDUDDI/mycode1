import socket

# test ver
HOST = '127.0.0.1'
PORT = 1234

# TCP소켓: SOCK_STREAM, UDP소켓: SOCK_DGRAM
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 포트 사용중 오류에 대비, 무조건 사용
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# HOST는 로컬호스트인 경우에는 "" 가능, PORT: 1-65535
server_socket.bind((HOST, PORT))

# 클라이언트의 접속을 대기함
server_socket.listen() # server_socket: 대기를 위한 소켓
print('서버 대기 중...')

# 대기중에 클라이언트가 접속하면 클라이언트의 통신용 소켓과 주소를 튜플형으로 리턴
(client_socket, addr) = server_socket.accept() # client_socket: 통신을 위한 소켓

# 접속한 클라이언트의 주소
print('Connected by', addr)

while True:
    data = client_socket.recv(1024) # 클라이언트의 통신용 소켓을 통해 수신

    if not data:
        print('클라이언트 나감')
        break

    print('Received from', addr, data.decode()) # decode

    client_socket.sendall(data) # 클라이언트의 통신 소켓을 통해 전송함

client_socket.close()
server_socket.close()
print('서버 종료...')