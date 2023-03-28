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
      print("Host online")
      return True
    else:
      print("Host responded incorrectly")
      return False
  except  TimeoutError:
      print("host didn't respond")
      return False
  except ConnectionRefusedError:
    print("connection refused")
    return False

def shutdown_host():
  if (host_online()):
    client_socket.send("shutdown".encode())
    response = client_socket.recv(1024).decode()
    if response == "ack":
      print("Host acknowledged shutting down")
    else:
      print("Unknown response")


shutdown_host()

