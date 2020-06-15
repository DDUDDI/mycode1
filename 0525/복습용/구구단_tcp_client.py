import socket

HOST = '127.0.0.1'
PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOL_SOCKET)
client_socket. connect((HOST, PORT))

while True:

    # 숫자 입력
    num = input('숫자를 입력하세요: ')
    # 숫자 전송 (client -> server)
    client_socket.send(num.encode())
    # 숫자 수신 (server -> client)
    data= client_socket.recf(1024)
    linelist = data.decode().split('\n')
    for i in linelist:
        print(i)

    if num == 'x':
        break

client_socket.close()
print('클라이언트 종료...')