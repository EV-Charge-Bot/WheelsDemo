import Jetson.GPIO as GPIO
#import time, serial
GPIO.setmode(GPIO.BOARD)  
#GPIO.setup(#of pin,GPIO.OUT)
#FL:
FL_IN1=7
FL_IN2=11

#FR:
FR_IN1=12
FR_IN2=15

#BF:
BL_IN1=19
BL_IN2=21

#BR:
BR_IN1=26
BR_IN2=23

#Initialize FL_ENA, FL_IN1, and FL_IN2
#FL_PWM= [pin_num] #ENA
GPIO.setup(FL_IN1,GPIO.OUT)
GPIO.setup(FL_IN2,GPIO.OUT)

#Initialize FR_ENA, FR_IN1, and FR_IN2
#FR_PWM= [pin_num] #ENA
GPIO.setup(FR_IN1,GPIO.OUT)
GPIO.setup(FR_IN2,GPIO.OUT)

#Initialize BL_ENA, BL_IN1, and BL_IN2
#BL_PWM= [pin_num] #ENA
GPIO.setup(BL_IN1,GPIO.OUT)
GPIO.setup(BL_IN2,GPIO.OUT)

#Initialize BR_ENA, BR_IN1, and BR_IN2
#BR_PWM= [pin_num] #ENA
GPIO.setup(BR_IN1,GPIO.OUT)
GPIO.setup(BR_IN2,GPIO.OUT)

while (1):
    x=input()
    if x=='f':
        print('forward')
        # FL_Forward
        GPIO.output(FL_IN1, GPIO.HIGH)
        GPIO.output(FL_IN2, GPIO.LOW)

        # FR_Forward
        GPIO.output(FR_IN1, GPIO.HIGH)
        GPIO.output(FR_IN2, GPIO.LOW)

        # BL_Forward
        GPIO.output(BL_IN1, GPIO.HIGH)
        GPIO.output(BL_IN2, GPIO.LOW)

        # BR_Forward
        GPIO.output(BR_IN1, GPIO.HIGH)
        GPIO.output(BR_IN2, GPIO.LOW)
        #x='z'

        
    elif x=='b':
        print('backward')
        # FL_Backward
        GPIO.output(FL_IN1, GPIO.LOW)
        GPIO.output(FL_IN2, GPIO.HIGH)
        
        # FR_Backward
        GPIO.output(FR_IN1, GPIO.LOW)
        GPIO.output(FR_IN2, GPIO.HIGH)

        # BL_Backward
        GPIO.output(BL_IN1, GPIO.LOW)
        GPIO.output(BL_IN2, GPIO.HIGH)

        # BR_Backward
        GPIO.output(BR_IN1, GPIO.LOW)
        GPIO.output(BR_IN2, GPIO.HIGH)
        #x='z'   
        
    elif x=='s':
        print('stop')
        # FL_Stop
        GPIO.output(FL_IN1, GPIO.LOW)
        GPIO.output(FL_IN2, GPIO.LOW)

        # FR_Stop
        GPIO.output(FR_IN1, GPIO.LOW)
        GPIO.output(FR_IN2, GPIO.LOW)

        # BL_Stop
        GPIO.output(BL_IN1, GPIO.LOW)
        GPIO.output(BL_IN2, GPIO.LOW)

        # BR_Stop
        GPIO.output(BR_IN1, GPIO.LOW)
        GPIO.output(BR_IN2, GPIO.LOW)
        #x='z'
        
    elif x=='l':
        print('left')
        # FL_Left
        GPIO.output(FL_IN1, GPIO.LOW)
        GPIO.output(FL_IN2, GPIO.HIGH)

        # FR_Left
        GPIO.output(FR_IN1, GPIO.HIGH)
        GPIO.output(FR_IN2, GPIO.LOW)

        # BL_Left
        GPIO.output(BL_IN1, GPIO.HIGH)
        GPIO.output(BL_IN2, GPIO.LOW)

        # BR_Left
        GPIO.output(BR_IN1, GPIO.LOW)
        GPIO.output(BR_IN2, GPIO.HIGH)
        
    elif x=='r':
        print('right')
        # FL_Right
        GPIO.output(FL_IN1, GPIO.HIGH)
        GPIO.output(FL_IN2, GPIO.LOW)

        # FR_Right
        GPIO.output(FR_IN1, GPIO.LOW)
        GPIO.output(FR_IN2, GPIO.HIGH)

        # BL_Right
        GPIO.output(BL_IN1, GPIO.LOW)
        GPIO.output(BL_IN2, GPIO.HIGH)

        # BR_Right
        GPIO.output(BR_IN1, GPIO.HIGH)
        GPIO.output(BR_IN2, GPIO.LOW)
        
    elif x=='ccw':
        print('ccw')
        # FL_CCW
        GPIO.output(FL_IN1, GPIO.LOW)
        GPIO.output(FL_IN2, GPIO.HIGH)

        # FR_CCW
        GPIO.output(FR_IN1, GPIO.HIGH)
        GPIO.output(FR_IN2, GPIO.LOW)

        # BL_CCW
        GPIO.output(BL_IN1, GPIO.LOW)
        GPIO.output(BL_IN2, GPIO.HIGH)

        # BR_CCW
        GPIO.output(BR_IN1, GPIO.HIGH)
        GPIO.output(BR_IN2, GPIO.LOW)
        
    elif x=='e':
        GPIO.cleanup()
        print('clean up')
        break
    
    else:
        print('---Enter Different Data---')
