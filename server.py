# socketとosモジュールインポート
import os
import socket

# UNIXソケットをストリームモードで作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# サーバが接続を待つUNIXソケットのパスを設定
server_address = '/temp/socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(16)
            data_str = data.decode('utf-8')
            print('Received' + data_str)
            if data:
                respones = 'Processing ' + data_str
                connection.sendall(respones.encode())
            else:
                print('no data from', client_address)
                break
    finally:
        print("Closing current connection")
        connection.close()