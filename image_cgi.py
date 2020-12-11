#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
print ("Content-type:text/html\r\n\r\n")
import cgi,os
from skimage import io
import socket,pickle
from socket import AF_INET, SOCK_DGRAM
import cgitb
cgitb.enable()
import base64
import cv2
import scipy
import numpy as np
from skimage import io
from fractions import Fraction
from skimage.transform import resize
import time

form=cgi.FieldStorage()
fileitem=form['filename']

if fileitem.filename:
    fn=os.path.basename(fileitem.filename.replace("\\","/"))
    open('/var/www/html/cgi-enabled/'+fn,'wb').write(fileitem.file.read())
    with open('/var/www/html/cgi-enabled/'+fn,'rb') as img:
        img_mes = base64.b64encode(img.read())
    size = len(img_mes)
#connection 
    s = socket.socket()
    s.connect(('node-1.655projecthenry.ch-geni-net.genirack.nyu.edu',1249))
    s.settimeout(3)
    s.send(str(size).encode())
    data = s.recv(1024).decode()
    if data == 'ok':
        t1 = time.time()
        s.sendall(img_mes)
        message = s.recv(1024).decode()
        t2 = time.time()
        print("ATT: ", t2-t1)
    else:
        message = 'error'

#connnection ends
    print ("""
    Content-Type: text/html\n
    <html>
    <head>
    <meta charset="utf-8">
    <title>CS655 Geni Project</title>
    </head>
    <body>
    <h1>Recognition Finished!</h1>
    <p> Image uploaded is:</p>
    <img src='/cgi-enabled/{}'  alt="upload picture" />
    <h2>Result:{}</h2>
    <a href="/index.html">
        <button>try again!</button>
    </a>
    </body>
    </html>
    """.format(fn,message))
#No files
else:
    message='fail'
    print ("""
    Content-Type: text/html\r\n\r\n
    <html>
    <head>
    <meta charset="utf-8">
    <title>CS655 Geni Project</title>
    </head>
    <body>
    <h1>No image uploaded</h1>
    <a href="/index.html">
        <button>try again!</button>
    </a>
    </body>
    </html>
    """)
