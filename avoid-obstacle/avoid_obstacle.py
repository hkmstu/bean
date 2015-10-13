import sys
import pdb
sys.path.append('../motion-part')
import time
import RPi.GPIO as GPIO
from socket_client import socket_client

reverse_dic = {'back':'forward', 'left':'right', 
               'right':'left', 'forward':'back' }

class avoid_obst:

    def __init__(self):

        # back, left, right, forward.   
        self.pin_dic = {'back':7, 'left':11, 'right':21, 'forward':23}
        GPIO.setmode(GPIO.BOARD)
        for i in self.pin_dic.values():
            GPIO.setup(i, GPIO.IN)

    def get_status(self, which):

        return GPIO.input(self.pin_dic[which])

    def get_all_status(self):

        status_dic = {}
        for i in ('forward', 'back', 'left', 'right'):
           status_dic[i] = self.get_status(i) 
        return status_dic

def auto_drive():

    #pdb.set_trace()
    ao = avoid_obst()
    sc = socket_client()
    try:
        while True:
            status_dic = ao.get_all_status()
            for direct, status in status_dic.items():
                if status == 0 and direct != 'forward':
                    sc.send_cmd(reverse_dic[direct])
                elif status == 0 and direct == 'forward':
                    sc.send_cmd(reverse_dic[direct])
                    time.sleep(0.1)
                    sc.send_cmd('right')
                    time.sleep(0.1)
                else:
                    sc.send_cmd('forward')
                time.sleep(0.1)
                sc.send_cmd('stop')
    except keyboardinterrupt:
        sc.send_cmd('stop')

if __name__ == '__main__':

    auto_drive()
