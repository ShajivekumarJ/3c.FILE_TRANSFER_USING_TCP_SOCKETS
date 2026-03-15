# 3c.CREATION FOR FILE TRANSFER USING TCP SOCKETS
## AIM
To write a python program for creating File Transfer using TCP Sockets Links
## ALGORITHM:
1. Import the necessary python modules.
2. Create a socket connection using socket module.
3. Send the message to write into the file to the client file.
4. Open the file and then send it to the client in byte format.
5. In the client side receive the file from server and then write the content into it.
## PROGRAM:
~~~
SERVER.PY
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
~~~
```
CLINENT.PY:
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

```
## OUTPUT:

![alt text](server.png)
![alt text](clinent.png)

## RESULT
Thus, the python program for creating File Transfer using TCP Sockets Links was 
successfully created and executed.