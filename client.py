import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '192.168.1.201'
server_port = 31338

client_socket.connect((server_address, server_port))

message = 'Hello World'
client_socket.send(message.encode())
response = client_socket.recv(1024).decode()
print(response)
print("Test passed" if message == response else "Test failed")
