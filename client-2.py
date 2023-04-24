#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import random
client2 = socket.socket()
host = '127.0.0.1'
port = 2005
print('Waiting for connection response')
try:
    client2.connect((host, port))
except socket.error as e:
    print(str(e))

cards2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
i=0

while i<len(cards2):
    value = random.choice(cards2)
    cards2.remove(value)
    client2.send(str.encode(str(value)))
    res = client2.recv(1024)
    print(res.decode('utf-8'))
    i=i+1

client2.close()


# In[ ]:




