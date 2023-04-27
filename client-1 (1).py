#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import socket                          
import random
client1 = socket.socket()
host = '127.0.0.2'                              # defined host and port
port = 3002
print('Waiting for client2 connection response')
try:
    client1.connect((host, port))               #try and except method handles connection 
except socket.error as e:
    print(str(e))

cards1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]                #defined cards
i=0

while len(cards1) > 0:
    value = random.choice(cards1)               #choosing cards method
    cards1.remove(value)
    print(f"sending value {value}")             #sending random cards to server
    client1.send(str.encode(str(value)))
    res = client1.recv(1024)                        #response which we get from server
    print(f"response: {res.decode('utf-8')}")
    i=i+1
print("client exiting loop")
client1.close()


# In[ ]:




