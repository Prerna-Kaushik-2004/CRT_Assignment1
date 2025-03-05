import socket  #to connect

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     #Dgram is used to send the data
ip_address="10.10.11.106"
port = 1234
complete=(ip_address,port)

msg=input("Enter your message: ")
encode_msg=msg.encode("ascii")

s.sendto(encode_msg,complete)