#Tugas Progjar B
#oleh Prasetya Gilang N
#NRP 5113100104
#Program Chating 2 Client
#File Client1

import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 1994)
print >>sys.stderr, 'menghubungkan ke %s port %s' % server_address
sock.connect(server_address)

# Send data
nama_saya = raw_input ("ketik nama: ")
sock.sendall(nama_saya)
    
while True:
    # Send data
    message = raw_input ("Anda: ")
    sock.sendall(message)
    data = sock.recv(200)
    print >>sys.stderr, '%s' % data