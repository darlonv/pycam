import argparse
import socket
import pickle
import cv2

SERVER_TCP_PORT = 8084
SERVER_IP = '127.0.0.1'

##Parameters
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', type=str, default='127.0.0.1',  help='Server IP addres. Default: localhost')
parser.add_argument('-p', '--port', type=int, default=8084, help='Server TCP Port. Default: 8084')

args = parser.parse_args()

if args.port:
    SERVER_TCP_PORT=args.port
if args.ip:
    SERVER_IP=args.ip


#Loop connecting and gettin frames
while True: 

    #Socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Server connection
    # print(f'== Conectando a {dest}:{port}==')
    client.connect((SERVER_IP, SERVER_TCP_PORT))

    data = []
    while True:
        #Get frame
        pacote = client.recv(4096)
        if not pacote: 
            break
        data.append(pacote)


    if data:
        #Unpack frame
        frame = pickle.loads(b"".join(data))
    
        #Show frame
        cv2.imshow('Image', frame)

        #Wait until ESC key is pressed
        c = cv2.waitKey(1)
        if c == 27:
            break

#Close connections and windows
client.close()
cv2.destroyAllWindows()

    