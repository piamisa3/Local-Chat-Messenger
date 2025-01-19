import socket
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/tmp/udp_socket_file'

try:
    os.unlink(server_address)

except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

sock.bind(server_address)

while True:
    print('¥nwaiting to receive message')

    data, address = sock.recvfrom(4096)

    print('Sever: received {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        fake = Faker()
        sent = sock.sendto(fake.name().encode(), address)
        print('Server: sent {} bytes back to {}'.format(sent, address))