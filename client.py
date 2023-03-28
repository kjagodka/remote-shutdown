import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '192.168.1.201'
server_port = 31338

client_socket.settimeout(1)
client_socket.connect((server_address, server_port))

def host_online():
  client_socket.send("ping".encode())
  try:
    if client_socket.recv(1024).decode() == "pong":
      return True #host is online
    else:
      return False #host didn't respond correctly
  except (TimeoutError, ConnectionRefusedError):
    return False #couldn't connect to host

def shutdown_host():
  if (host_online()):
    print("Host is online")
    try:
      client_socket.send("shutdown".encode())
      response = client_socket.recv(1024).decode()
      if response == "ack":
        print("Host acknowledged shutdown request")
      else:
        print("Unknown didn't respond correctly for shutdown request")
    except: (TimeoutError, ConnectionRefusedError):
      print("Host went offline")

shutdown_host()

