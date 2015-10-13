import pdb
import time
from robots_motor import robots_motor
from robots_servo import robots_servo

action_dic_s = {'left':(0,'up'), 'right':(0,'down'),
                      'up':(1,'up'), 'down':(1,'down')}

class robots_mod:

    def __init__(self):
    
       self.rbm = robots_motor() 
       self.rbs = robots_servo()

    def action_m(self, motor_info):

        self.rbm.action(motor_info)

    def action_s(self, servo_info):

        control = action_dic_s[servo_info]
        self.rbs.move(control,)

if __name__ == '__main__':
    
    rm = robots_mod()
    rm.action_m('back')
    time.sleep(2)
    rm.action_m('stop')
