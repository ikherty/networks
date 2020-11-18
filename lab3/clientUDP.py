#client
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
message = 'This is the message.  It will be repeated.'

try:
    print('sending "%s"' % message)
    sent = sock.sendto(message.encode(), server_address)
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received "%s"' % data)
finally:
    print('closing socket')
    sock.close()
