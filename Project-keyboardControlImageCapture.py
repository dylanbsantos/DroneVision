import time
from djitellopy import tello
import keyPressModule as kpm
import cv2

kpm.init()
drone=tello.Tello()
drone.connect()
print("Battery of Drone is", drone.get_battery())
global img #makes sure we can use the img on line 33
drone.streamon() #give all frames one by one

def getKeyboardInput():
    leftRight, forwardBack, upDown, yawVelocity = 0,0,0,0
    speed=50

    if kpm.getKey("LEFT"):leftRight = -speed
    elif kpm.getKey("RIGHT"):leftRight = speed

    if kpm.getKey("w"):upDown = speed
    elif kpm.getKey("s"):upDown = -speed

    if kpm.getKey("UP"):forwardBack = speed
    elif kpm.getKey("DOWN"):forwardBack = -speed

    if kpm.getKey("a"):yawVelocity = -speed
    elif kpm.getKey("d"): yawVelocity = speed

    if kpm.getKey("q"): drone.land(); time.sleep(3)
    if kpm.getKey("e"): drone.takeoff()

    if kpm.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg',img) #stores the frame that the drone sees as a unique file name each time
        time.sleep(0.3) #so i dont get a billion images of the same frame
    return [leftRight, forwardBack, upDown, yawVelocity]


while True:
    values= getKeyboardInput()
    drone.send_rc_control(values[0],values[1],values[2],values[3])

    img=drone.get_frame_read().frame #gives the image from the drone
    img=cv2.resize(img,(360,240)) #small frame size means faster
    cv2.imshow("POV: You are a Drone",img) #creates a window to show the result
    cv2.waitKey(1) #give it a delay of 1 millisecond

