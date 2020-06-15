import socket

# HOST, PORT
HOST = '127.0.0.1'
PORT = 1234

# socket(family, type) 생성
# family: 주소체계, IP4v: AF_INET, IP6v: AF_INET6
# type: # 소켓 타입, TCP: SOCK.STREAM, UDP: SOCK_DGRAM
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 접속
# 클라이언트는 bind, listen의 과정 필요 X
# (HOST, PORT) 튜플 타입
client_socket.connect((HOST, PORT))

# 메세지 전송 (client -> server)
# encode 해서 전송
# send: low-level, 요청한 데이터보다 더 적게 전송 가능
# sendall: high-level, 요청한 데이터의 모든 버퍼 내용 전송
client_socket.sendall('Hello Server'.encode())

# 메세지 수신 (server -> client)
# recv(buffer size): 소켓에서 데이터 수신
# decode 해서 수신
# repr(): 객체를 인간이 이해할 수 있는 표현으로 나타내기 위한 용도?
data = client_socket.recv(1024)
print('Received: ', repr(data.decode()))

client_socket.close()
print('클라이언트 종료...')