import socket

HOST = '127.0.0.1'
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()
print('서버 대기 중...')

(client_socket, addr) = server_socket.accept()
print('Connected by', addr)

while True:
    data = client_socket.recv(1024)
    if not data:
        print('클라이언트 나감')
        break

    print('Received from: ', addr, data.decode())

    # 구구단
    dan = int(data.decode())
    res = []
    for i in range(1, 10):
        line = f'{dan} * {i} = {dan*i}\n'
        res.append(line)

    # client에게 전송하기 위해 list를 string으로 바꾸고 encoding 함
    client_socket.sendall(''.join(res).encode())

client_socket.close()
server_socket.close()
print('서버 종료...')