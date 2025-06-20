from djitellopy import tello # give access to the tello library
from time import sleep # will need to do delays between movements

drone=tello.Tello()
drone.connect() #connects Tello to the code
print("Battery of drone:",drone.get_battery()) #displays how much battery the drone has

drone.takeoff() #drone takes off
drone.send_rc_control(0,50,0,0) #velocity forwards
sleep(2) #delay 2 secs
drone.send_rc_control(30,0,0,100) #velocity rightwards
sleep(2) #delay 2 secs
drone.send_rc_control(0,0,0,0) #stops
drone.land() #drone lands