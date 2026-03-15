import socket

host = "127.0.0.1"
port = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected with", addr)

file = open("received_file.txt", "wb")

while True:
    data = conn.recv(1024)
    if not data:
        break
    file.write(data)

file.close()
conn.close()
server.close()

print("File received successfully")