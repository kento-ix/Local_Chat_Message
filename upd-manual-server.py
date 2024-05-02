import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '/tmp/socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}' .format(server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('Connection from', client_address)
        while True:
            data = connection.recv(1024)
            if data:
                print("Response from client: ", data.decode())
            else:
                print('No data received, client disconnected')
                break

            data_str = data.decode()
            response = input("(Receiver)Enter message: ")
            connection.sendall(response.encode())
    finally:
        print("Closing current connection.")
        connection.close()