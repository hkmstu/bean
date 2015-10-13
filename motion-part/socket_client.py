import sys
import time
import socket

HOST='0.0.0.0'
PORT=2001

cmd_dic = { 'forward':'\xff\x00\x01\x00\xff', 'back':'\xff\x00\x02\x00\xff', \
        'left':'\xff\x00\x03\x00\xff', 'right':'\xff\x00\x04\x00\xff', \
        'stop':'\xff\x00\x00\x00\xff'}

class socket_client():

    def __init__(self):

        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((HOST,PORT))

    def send_cmd(self, info):

        if info not in ('forward','back','left','right','stop'):
            return
        self.client.sendall(cmd_dic[info])
        #time.sleep(1)
        #self.client.sendall(cmd_dic['stop'])

def main(): 
    
    sc = socket_client()
    sc.send_cmd('forward')

if __name__ == '__main__':
    main()
