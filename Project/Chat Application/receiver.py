import socket  #to connect

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     #Dgram is used to send the data
ip_address="172.20.10.6"
port=1234
complete=(ip_address,port)
s.bind(complete)  #binding the ip and port
while(True):
    msg=s.recvfrom(1024) #1024--Limit the msg
    decode_msg=msg[0].decode("ascii")
    print(decode_msg)