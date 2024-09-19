import time

from Led import *
led=Led()
def test_Led():
    try:
        led.ledIndex(0x01,255,0,0)      #Red
        led.ledIndex(0x02,255,125,0)    #orange
        led.ledIndex(0x04,255,255,0)    #yellow
        led.ledIndex(0x08,0,255,0)      #green
        led.ledIndex(0x10,0,255,255)    #cyan-blue
        led.ledIndex(0x20,0,0,255)      #blue
        led.ledIndex(0x40,128,0,128)    #purple
        led.ledIndex(0x80,255,255,255)  #white'''
        print ("The LED has been lit, the color is red orange yellow green cyan-blue blue white")
        time.sleep(3)               #wait 3s
        led.colorWipe(led.strip, Color(0,0,0))  #turn off the light
        print ("\nEnd of program")
    except KeyboardInterrupt:
        led.colorWipe(led.strip, Color(0,0,0))  #turn off the light
        print ("\nEnd of program")
        
from Motor import *            
PWM=Motor()          
def test_Motor(): 
    try:
        PWM.setMotorModel(1000,1000,1000,1000)         #Forward
        print ("The car is moving forward")
        time.sleep(1)
        PWM.setMotorModel(-1000,-1000,-1000,-1000)     #Back
        print ("The car is going backwards")
        time.sleep(1)
        PWM.setMotorModel(-1500,-1500,2000,2000)       #Turn left
        print ("The car is turning left")
        time.sleep(1)
        PWM.setMotorModel(2000,2000,-1500,-1500)       #Turn right 
        print ("The car is turning right")  
        time.sleep(1)  
        
        PWM.setMotorModel(0,0,0,0)               #Stop
        print ("\nEnd of program")
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")
        
from Ultrasonic import *
ultrasonic=Ultrasonic()    
def test_Ultrasonic():
    try:
        while True:
            data=ultrasonic.get_distance()   #Get the value
            print ("Obstacle distance is "+str(data)+"CM")
            time.sleep(1)
    except KeyboardInterrupt:
        print ("\nEnd of program")
             
def stop_obstacle(threshold=10):
	try:
		PWM.setMotorModel(1000,1000,1000,1000)         #Forward
		print ("The car is moving forward")
		
		while True:
			distance = ultrasonic.get_distance()
			print(f"Current distance: {distance} cm")
           
			if distance < threshold:  
				print(f"Obstacle detected at {distance} cm. Stopping the car.")
				PWM.setMotorModel(0, 0, 0, 0) 
				break
           
			time.sleep(0.1)
	except KeyboardInterrupt:
		PWM.setMotorModel(0,0,0,0)
		print ("\nEnd of program")


def avoid_obstacle(threshold=10):
    try:
        PWM.setMotorModel(1000, 1000, 1000, 1000) 
        print("The car is moving forward.")
       
        while True:
            distance = ultrasonic.get_distance()
            print(f"Current distance: {distance} cm")
           
            if distance < threshold: 
                print(f"Obstacle detected at {distance} cm. Stopping the car.")
                PWM.setMotorModel(0, 0, 0, 0) 
                time.sleep(1) 
                print("Reversing the car.")
                PWM.setMotorModel(-1000, -1000, -1000, -1000) 
                time.sleep(0.75) 
                print("Changing direction.")
                PWM.setMotorModel(2000,2000,-1500,-1500) 
                time.sleep(0.75) 
                PWM.setMotorModel(1000, 1000, 1000, 1000) 
                print("The car is moving forward again.")
           
            time.sleep(0.1) 

    except KeyboardInterrupt:
        PWM.setMotorModel(0, 0, 0, 0)
        print("\nProgram stopped.")
        
        
if __name__ == '__main__':

    print ('Program is starting ... ')
    import sys
    if len(sys.argv)<2:
        print ("Parameter error: Please assign the device")
        exit() 
    elif sys.argv[1] == 'Motor':
        test_Motor()
    elif sys.argv[1] == 'Ultrasonic':
        test_Ultrasonic()
    elif sys.argv[1] == 'Stop_obstacle':
        stop_obstacle()
    elif sys.argv[1] == 'Avoid_obstacle':
        avoid_obstacle()
    elif sys.argv[1] == 'Led':
        test_Led

        

