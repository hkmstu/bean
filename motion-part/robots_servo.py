import pdb
import time
import RPi.GPIO as GPIO

angle_lst = (11.5, 9.5, 7.5, 5.5, 3.5)

class robots_servo:

    def __init__(self, pin_lst=[]):
    
        self.pwms = []
        self.angle = [0, 0]
        # ( left_right, up_down )
        if len(pin_lst) < 2:
           self.pins = (24, 26) 
        else:
           self.pins = pin_lst
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        for i, pin in enumerate(self.pins):
            GPIO.setup(pin, GPIO.OUT)
            pwm = GPIO.PWM(pin, 50)
            self.pwms.append(pwm)
            if i == 0:
                pwm.start(7.5)
            else:
                pwm.start(3.5)
            time.sleep(0.3)
            pwm.ChangeDutyCycle(0)
        self.angle = [2, 2]

    def reset(self):
        
        for pwm in self.pwms:
            pwm.ChangeDutyCycle(7.5)
            time.sleep(0.3)
            pwm.ChangeDutyCycle(0)
        self.angle = [2, 2]

    def move(self, which_servo, direct):

        if which_servo not in (0,1):
            return 'error'
        pwm = self.pwms[which_servo]
        if direct == 'up' and self.angle[which_servo]+1 < len(angle_lst):
            angle = angle_lst[self.angle[which_servo]+1]
            pwm.ChangeDutyCycle(angle)
            time.sleep(0.08)
            pwm.ChangeDutyCycle(0)
            self.angle[which_servo] = self.angle[which_servo]+1
        elif direct == 'down' and self.angle[which_servo]-1 >= 0:
            angle = angle_lst[self.angle[which_servo]-1]
            pwm.ChangeDutyCycle(angle)
            time.sleep(0.08)
            pwm.ChangeDutyCycle(0)
            self.angle[which_servo] = self.angle[which_servo]-1

if __name__ == '__main__':

    rbs = robots_servo()
    while True:
        what = raw_input('input\n')
        which, direct = what.split(',')
        rbs.move(int(which), direct)
