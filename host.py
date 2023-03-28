
import socket
import os
import sys
import platform

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = socket.gethostbyname(socket.gethostname())
server_port = 31338

server = (server_address, server_port)
sock.bind(server)
print("Listening on " + server_address + ":" + str(server_port))

def shutdown():
  match platform.system():
    case 'Linux':
      os.system('systemctl poweroff')
    case 'Windows':
      os.system('shutdown /s /t 0')


while True:
    payload, client_address = sock.recvfrom(1024)
    match payload.decode():
      case "ping":
        print("pinged", file=sys.stderr)
        sock.sendto("pong".encode(), client_address)
      case "shutdown":
        print("shutdown", file=sys.stderr)
        sock.sendto("ack".encode(), client_address)
        shutdown()
      case _:
        print("unknown payload: " + payload.decode(), file=sys.stderr)
