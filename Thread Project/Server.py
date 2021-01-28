import socket
import threading;

#thread to handle communication with client.
def client_handler(client_socket):
    client_name = client_socket.getpeername();
    client_name = client_name[0]+ "/" + str(client_name[1]);
    while True:
    
        data = client_socket.recv(1024);
        data = data.decode();
        print("client {}:".format(client_name),data);
        if(data=="exit"):
            break;
        else:
            client_socket.send(input().encode());
    client_socket.close();

#main thread.

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
#server_socket.bind(("192.168.90.155",9999));
server_socket.bind(("127.0.0.1",9999));
server_socket.listen(); #optional
#waiting for clients
while True: # infinite loop
    print("waiting for clients");
    client_socket, addr = server_socket.accept(); #blocking call
    th1 = threading.Thread(target=client_handler,args=(client_socket,));
    th1.start();
    
server_socket.close();
