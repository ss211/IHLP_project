#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import random
client1 = socket.socket()
host = '127.0.0.1'
port = 2005
print('Waiting for connection response')
try:
    client1.connect((host, port))
except socket.error as e:
    print(str(e))

cards1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
i=0

while i<len(cards1):
    value = random.choice(cards1)
    cards1.remove(value)
    client1.send(str.encode(str(value)))
    res = client1.recv(1024)
    print(res.decode('utf-8'))
    i=i+1

client1.close()


# In[ ]:




