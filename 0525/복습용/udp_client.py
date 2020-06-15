import socket

UDP_IP_ADDRESS = '127.0.0.1'
UDP_PORT = 12345
buffer = 4096

addr = (UDP_IP_ADDRESS, UDP_PORT)
socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input('Enter your message >> ')
    if message == 'exit':
        break

    # UDP client는 connect 과정 X
    socket_client.sendto(message.encode(), addr)

    response, addr = socket_client.recvfrom(buffer)
    print('Server response => %s' % response.decode())

socket_client.close()