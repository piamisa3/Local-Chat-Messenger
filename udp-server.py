import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/udp_socket_file'

try:
    os.unlink(server_address)

except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

sock.bind(server_address)
