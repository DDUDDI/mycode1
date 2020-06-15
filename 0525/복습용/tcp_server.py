import socket

# HOST, PORT
HOST = '127.0.0.1'
PORT = 1234

# socket(family, type) 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 포트 사용중 오류에 대비, 무조건 사용
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind(): 호스트와 포트를 튜플로 감싸서 전달
# 서버 소켓: bind, 클라이언트 소켓: connect
# HOST는 로컬호스트인 경우에는 "" 가능, PORT: 1-65535
server_socket.bind((HOST, PORT))

# 클라이언트 접속 대기
server_socket.listen()
print('서버 대기 중...')

# 대기 중에 클라이언트가 접속하면 클라이언트의 통신용 소켓과 주소를 튜플형으로 리턴
(client_socket, addr) = server_socket.accept()

# 접속한 클라이언트의 주소
print('Connected by: ', addr)

while True:
    # 메세지 수신 (client -> server)
    data = client_socket.recv(1024)

    # 데이터가 존재하지 않으면...
    if not data:
        print('클라이언트 나감')
        break

    # addr의 client로부터 data decode 해서 수신
    print('Received from ', addr, data.decode())

    # client의 통신 소켓으로 데이터 전송 (server -> client)
    client_socket.sendall(data) #### 여기는 왜 encode 안하지?

client_socket.close()
server_socket.close()
print('서버 종료...')