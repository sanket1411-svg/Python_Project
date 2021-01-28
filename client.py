# multi threading client program 
import socket 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

#client_socket.connect(("192.168.90.89", 9999));
client_socket.connect(("127.0.0.1", 9999));
print("client_socket = ", client_socket);
while True:

    data =  input();
    data = data.encode();
    client_socket.send(data);
    data = client_socket.recv(1024);
    print("server:", data.decode());
    if data == "exit":
        break;
client_socket.close();