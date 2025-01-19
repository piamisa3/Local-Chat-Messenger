import socket
import sys
import os

if len(sys.argv) > 1:
    message = sys.argv[2]
else:
    message = input('pleas imput message!')

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/tmp/udp_socket_file'

address = '/tmp/udp_client_socket_file'

try:
    os.unlink(address)
except FileNotFoundError:
    pass

sock.bind(address)

try:
    print('sending {!r}'.format(message))
    sent = sock.sendto(message.encode(), server_address)

    print('waiting to receive..................')

    data, server = sock.recvfrom(4096)

    print('received {!r}'.format(data.decode('utf-8')))

finally:
    print('closing socket')
    sock.close()
