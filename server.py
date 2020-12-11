#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
import base64
from imageai.Prediction import ImagePrediction
import os
import socketserver, pickle, socket
from sklearn.decomposition import *
from skimage.transform import resize
from sklearn.preprocessing import scale
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
class MySockServer(socketserver.BaseRequestHandler):
   def handle(self):
      print ('New connection from', self.client_address)
      while True:
        data = self.request.recv(1024)
        print('recv: ', data.decode())
        self.request.send('ok'.encode())
        size = int(data.decode())
        print("size", size)
        img = ''
        while len(img) < size:
            data_new = self.request.recv(1024*500).decode()
            img += str(data_new)
            f = open("/geni/imgSave.png", "wb")
            f.write(base64.decodestring(img.encode()))
            f.close()

        # model prediction
        prediction = ImagePrediction()
        prediction.setModelTypeAsResNet()
        prediction.setModelPath('/geni/resnet50_weights_tf_dim_ordering_tf_kernels.h5')
        prediction.loadModel()

        predict, prob = prediction.predictImage("/geni/imgSave.png", result_count=3)
        for i in range(len(predict)):
            print(str(predict[i]) + ' : ' + str(prob[i]))
        # return first prediction
        res = str(predict[0]) + str(prob(0))
        self.request.send(res.encode())
        print('Result sent.')

if __name__ == '__main__':
     HOST = socket.gethostname()
     print(HOST)
     PORT = 1249
     print(PORT)         
     s = socketserver.ThreadingTCPServer((HOST, PORT), MySockServer)
     print ("socket is listening") 
     s.serve_forever()


