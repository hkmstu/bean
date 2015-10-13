import pdb
import time
import RPi.GPIO as GPIO

class robots_motor:

    def __init__(self, pin_lst=[]):
    
        # ( pin_left_0, pin_left_1, control_left, pin_right_0, pin_right_1, control_right )
        # (13, 15, 12), (16, 18, 22) 
        if len(pin_lst) < 4:
           self.pins = (13, 15, 12, 16, 18, 22) 
        else:
           self.pins = pin_lst
        self.pwms = []
        # 1. pins init.
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        for i in range(len(self.pins)):
            GPIO.setup(self.pins[i], GPIO.OUT)
            GPIO.output(self.pins[i], GPIO.LOW)
        # 2. init pwm.
        for i in range(2):
            pwm = GPIO.PWM(self.pins[3*i+2], 20)
            pwm.start(0)
            self.pwms.append(pwm)
    
    def set_speed(self, rate):

        self.pwms[0].ChangeDutyCycle(rate)
        self.pwms[1].ChangeDutyCycle(rate)

    def stop(self):

        for i in range(len(self.pins)):
            GPIO.output(self.pins[i], GPIO.LOW)

    def set_speed_and_direction(self, which, rate, direction=0):

        self.pwms[which].ChangeDutyCycle(rate)
        status = (GPIO.LOW, GPIO.HIGH)
        if direction == 1:
            status = (GPIO.HIGH, GPIO.LOW)
        for i in range(2):
            GPIO.output(self.pins[which*3], status[0])
            GPIO.output(self.pins[which*3+1], status[1])

    def left(self, rate=90):

        self.set_speed_and_direction(0, rate, 1) 
        self.set_speed_and_direction(1, rate, 0) 

    def right(self, rate=90):

        self.set_speed_and_direction(1, rate, 1) 
        self.set_speed_and_direction(0, rate, 0) 

    def forward(self, rate=50):

        self.set_speed_and_direction(0, rate, 0) 
        self.set_speed_and_direction(1, rate, 0) 

    def back(self, rate=50):

        self.set_speed_and_direction(0, rate, 1) 
        self.set_speed_and_direction(1, rate, 1)

    def action(self, info):

        act = getattr(self, info)
        return act()

if __name__ == '__main__':

    #pdb.set_trace()
    rbm = robots_motor()
#    try:
#        #rbm.forward()
#        rbm.action('right')
#        time.sleep(2)
#    except KeyboardInterrupt:
#        rbm.stop()
    rbm.stop()
