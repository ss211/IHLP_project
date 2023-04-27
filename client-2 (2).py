#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import random
client2 = socket.socket()
host = '127.0.0.2'
port = 3002
print('Waiting for client3 connection response')
try:
    client2.connect((host, port))
except socket.error as e:
    print(str(e))

cards2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
i=0

while len(cards2) > 0:
    value = random.choice(cards2)
    cards2.remove(value)
    print(f"sending value {value}")
    client2.send(str.encode(str(value)))
    res = client2.recv(1024)
    print(f"response: {res.decode('utf-8')}")
    i=i+1
print("client exiting loop")

client2.close()


# In[ ]:




