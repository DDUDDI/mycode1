import socket, sys

UDP_IP_ADDRESS = '127.0.0.1'
UDP_PORT = 12345
buffer = 4096

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
socket_server.bind((UDP_IP_ADDRESS, UDP_PORT))

# UDP는 비접속지향형이므로 accept, listen 필요 X
while True:
    print('Waiting for client...')
    data, addr = socket_server.recvfrom(buffer)
    data = data.strip() # 공백 제거
    print('Data Received from address: ', addr)
    print('message: ', data.decode())

    try:
        response = 'Hi %s' % sys.platform
    except Exception as e:
        response = '%s' % sys.exc_info()[0]

    print('Response', response)
    socket_server.sendto(response.encode(), addr) # sendto: TCP와의 차이점점

socket_sever.close()