import socket
import sys

# TCP/IPソケットを作成
# 通信を可能にするためのエンドポイント
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'
print('connectint to {}'.format(server_address))

# サーバー接続
try:
    sock.connect(server_address)

except socket.error as err:
    print(err)
    # 異常終了
    sys.exit(1)

try:
    # ソケット通信ではデータをバイト形式で送る
    message = b'Sending a message to the server side'
    sock.sendall(message)

    # サーバー応答待ち時間を2秒
    sock.settimeout(2)
    try:
        while True:
            data = str(sock.recv(32))

            if data:
                print('Server response: ' + data)
            else:
                break
    except TimeoutError:
        print('Socket timeout, ending listening for server messages') 

finally:
    print('closing socket')
    sock.close()
