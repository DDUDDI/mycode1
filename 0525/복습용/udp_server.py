import socket, sys

UDP_IP_ADDRESS = '127.0.0.1'
UDP_PORT = 12345
# 버퍼 사이즈 설정
buffer = 4096

# UDP: SOCK_DGRAM
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((UDP_IP_ADDRESS, UDP_PORT))

# UDP는 비접속지향형이므로 accept, listen 필요 X
while True:
    print('Waiting for client...')

    # UDP이므로 addr(IP주소, PORT번호)도 같이 받음
    data, addr = server_socket.recvfrom(buffer)
    data = data.strip()
    # data를 전송한 client의 address 출력
    print('Received from address: ', addr)
    # client가 전송한 data를 decoding해 출력
    print('Message: ', data)

    try:
        response = 'Hi %s' % sys.platform
    except Exception as e:
        response = '%s' % sys.exc_info()[0]

    print('Response', response)
    # UDP는 sendto()를 사용하여 addr 지정
    server_socket.sendto(response.encode(), addr)

server_socket.close() # client는 안 닫아줘도 되는지??