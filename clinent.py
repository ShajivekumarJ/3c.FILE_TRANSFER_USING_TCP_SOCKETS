import socket

host = "127.0.0.1"
port = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

file = open("received_file.txt", "rb")

data = file.read(1024)

while data:
    client.send(data)
    data = file.read(1024)

file.close()
client.close()

print("File sent successfully")
