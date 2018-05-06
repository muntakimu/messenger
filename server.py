import client
from socket import *
print("Enter the host(ex: 127.0.0.1): ")
host=str(input())
print('Enter the port(ex:4498): ')
port=int(input())

def Server():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print("Listening for connections.. ")
    q, addr = s.accept()
    data = input("Enter Message to be send:  ")
    q.send(data.encode())
    s.close()
    client.Client()



def StartServer():
    s= socket(AF_INET,SOCK_STREAM)
    s.bind((host,port))
    s.listen(1)
    q, addr= s.accept()
    data=input("Enter Message: ")
    q.send(data.encode())
    s.close()