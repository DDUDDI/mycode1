import socket

# 서버의 주소
HOST = '127.0.0.1'
PORT = 1234 # 서버가 실행 중인 포트번호

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 접속
client_socket.connect((HOST, PORT))

while True:

    # 숫자 전송
    num = input('몇 단을 출력하시겠습니까?: ')
    client_socket.sendall(num.encode()) # encode

    # 메시지 수신
    data = client_socket.recv(1024)
    linelist = data.decode().split('\n')
    for i in linelist:
        print(i)

    if num == 'x':
        break

client_socket.close()
print('클라이언트 종료...')