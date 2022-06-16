import argparse

import socket
import pickle
import cv2

from threading import Thread
from threading import Semaphore



IMG_PROP = 1.0  #Image proportion
TCP_PORT = 8084 #TCP Port

##Parameters
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--size', type=float, default=1.0,  help='Image size, in proportion. Default: 1.0')
parser.add_argument('-p', '--port', type=int, default=8084, help='TCP Port to listen. Default: 8084')

args = parser.parse_args()

if args.size:
    IMG_PROP=args.size
if args.port:
    TCP_PORT=args.port


frame_g = None #Frame (Global)

#Initialize Semaphore, to protect global rariable
semaforo_g = Semaphore(1)

#Tread responsible for the camera. Read frames and saves it on the shared variable
class ThreadCam(Thread):
    def __init__ (self):
        Thread.__init__(self)

        #Open camera
        self.cap = cv2.VideoCapture(0)

        # Check if the webcam is opened correctly
        if not self.cap.isOpened():
            raise IOError("Issue acessing webcam :/")
    
    def run(self):
        global frame_g
        while True:
            #Get camera frame
            ret, frame = self.cap.read()
            #Resize image
            frame = cv2.resize(frame, None, fx=IMG_PROP, fy=IMG_PROP, interpolation=cv2.INTER_AREA)
            #Copies frame to global variable
            semaforo_g.acquire()
            frame_g = frame
            semaforo_g.release()



class ThreadCamServer(Thread):
    def __init__ (self, addr, conn):
        Thread.__init__(self)
        self.addr = addr
        self.conn = conn

    def run(self):
        global frame_g
        
        #Pack frame
        semaforo_g.acquire()
        data_object = pickle.dumps(frame_g)
        semaforo_g.release()

        #Send frame
        if data_object:
            self.conn.send(data_object)

        #Fecha a conexao
        conn.close()



#Objeto socket
serv  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Associa o socket a uma porta local
serv.bind(('0.0.0.0',TCP_PORT))
serv.listen()

print('oi')
#Get camera frames
Camera = ThreadCam()
Camera.start()

#Server waits for connections
print('Server on!')
print(f'Port: {TCP_PORT}')

while True:
    conn, addr = serv.accept()

    ThreadCamServer(addr, conn).start()