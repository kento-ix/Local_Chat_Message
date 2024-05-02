import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'
print('connecting to {}' .format(server_address))

try:
    sock.connect(server_address)
    print('Success connecting to server.')

except socket.error as err:
    print(err)
    sys.exit(1)


try:
    while True:
        message = input("(Sender)Enter message: ")
        sock.sendall(message.encode())

        data = sock.recv(100)
        if data:
            print("Response from server: ", data.decode())
        else:
            break

except Exception as e:
    print("Error:", e)

finally:
    print('closing socket')
    sock.close()