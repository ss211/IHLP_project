#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import random
client3 = socket.socket()
host = '127.0.0.2'
port = 3002
print('Waiting for all connection response')
try:
    client3.connect((host, port))
except socket.error as e:
    print(str(e))

cards3 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
i=0

while len(cards3) > 0:
    value = random.choice(cards3)
    cards3.remove(value)
    print(f"sending value {value}")
    client3.send(str.encode(str(value)))
    res = client3.recv(1024)
    print(f"response: {res.decode('utf-8')}")
    i=i+1
print("client exiting loop")

client3.close()


# In[ ]:




