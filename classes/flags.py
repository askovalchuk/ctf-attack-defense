#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)
s = 'close'
while True:
    data = conn.recv(1024)
    print (data)
   # if data == s:
      #  conn.send(('goodbye').encode())
      #  break
    conn.send(('received\n').encode())
    

conn.close()