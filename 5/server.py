import socket
import pickle
import cryptocode


HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

p, g, A = pickle.loads(conn.recv(1024))
b = 4
B = g ** b % p
conn.send(pickle.dumps(B))
K = A ** b % p
key = str(K)
msg = 'Hello!'
print('Message:', msg)
mgsEncoded = cryptocode.encrypt(msg, key)
conn.send(pickle.dumps(mgsEncoded))
print('Sent message:', mgsEncoded)

conn.close()
