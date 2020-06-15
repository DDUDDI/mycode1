import socket

# 서버의 주소
HOST = '127.0.0.1'
PORT = 1234 # 서버가 실행 중인 포트번호

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 접속
client_socket.connect((HOST, PORT))

# 메시지 전송
client_socket.sendall('Hello Server!'.encode()) # encode

# 메시지 수신
data = client_socket.recv(1024)
print('Received: ', repr(data.decode()))

client_socket.close()
print('클라이언트 종료...')