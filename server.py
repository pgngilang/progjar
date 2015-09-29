#Tugas Progjar B
#oleh Prasetya Gilang N
#NRP 5113100104
#Program Chating 2 Client
#File Server

import sys
import socket

# Create a TCP/IP socket
sock1994 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1995 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 1994)
print >>sys.stderr, 'mulai koneksi %s port %s' % server_address
sock1994.bind(server_address)
server_address = ('localhost', 1995)
print >>sys.stderr, 'mulai koneksi %s port %s' % server_address
sock1995.bind(server_address)

# Listen for incoming connections
sock1994.listen(1)
sock1995.listen(1)

# Wait for a connection
print >>sys.stderr, 'menunggu koneksi'
connection1994, client_address = sock1994.accept()
print >>sys.stderr, 'Koneksi diterima dari', client_address
connection1995, client_address = sock1995.accept()
print >>sys.stderr, 'koneksi diterima dari', client_address

# input nama client 1
nama1 = connection1994.recv(100)
print >>sys.stderr, 'menerima chat dengan nama %s' % nama1
print >>sys.stderr, 'menghubungkan %s ke client 2' % nama1

# input nama client 2
nama2 = connection1995.recv(100)
print >>sys.stderr, 'menerima chat dengan nama %s' % nama2
print >>sys.stderr, 'menghubungkan %s ke %s' % (nama2, nama1)

while True:    	
    # menunggu pesan dari client 1
    data_kirim = connection1994.recv(100)
    if not data_kirim :
	print >> sys.stderr, '%s terputus' % nama1
	break    
    else :
        print >>sys.stderr, 'menerima %s dari %s' % (data_kirim, nama1)
        print >>sys.stderr, 'mengirim ke %s' % nama2
        chat_kirim = nama1 + " : " + data_kirim
        connection1995.sendall(chat_kirim)
    
    # menunggu pesan dari client 2
    data_kirim = connection1995.recv(100)
    if not data_kirim :
	print >> sys.stderr, '%s terputus' % nama2
	break
    else :
    	print >>sys.stderr, 'menerima %s dari %s' % (data_kirim, nama2)
        print >>sys.stderr, 'mengirim ke %s' % nama1
        chat_kirim = nama2 + " : " + data_kirim
    	connection1994.sendall(chat_kirim)    
connection.close()             
