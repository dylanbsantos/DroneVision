import math
import time
from time import  sleep
from djitellopy import tello
import keyPressModule as kpm
import numpy
import cv2


######################################## PARAMETERS ########################################
forwardSpeed=117/10 #forward speed in cm/s (117cm in 10s) (gave it 15cm/s)
angularSpeed=360/10 #angular speed in degrees/s (10s to rotate 360 degrees) (gave it 50d/s)
interval=0.25

distanceInterval=forwardSpeed*interval #gives distance every time 1 unit is moved
angularInterval=angularSpeed*interval #gives angle every time 1 unit is moved
###########################################################################################
x,y=500,500
angle=0
yaw=0

kpm.init()
drone=tello.Tello()
drone.connect()
print("Battery of Drone is", drone.get_battery())

points=[(0,0),(0,0)]

def getKeyboardInput():
    leftRight, forwardBack, upDown, yawVelocity = 0,0,0,0
    angularSpeed=50
    speed=50 #50cm/s
    global x,y,yaw, angle
    distance=0

    if kpm.getKey("LEFT"):
        leftRight = -speed
        distance=distanceInterval
        angle=-180

    elif kpm.getKey("RIGHT"):
        leftRight = speed
        distance=-distanceInterval
        angle=180

    if kpm.getKey("w"):
        upDown = speed
    elif kpm.getKey("s"):
        upDown = -speed

    if kpm.getKey("UP"):
        forwardBack = speed
        distance=distanceInterval
        angle=270

    elif kpm.getKey("DOWN"):
        forwardBack = -speed
        distance=distanceInterval
        angle=-90

    if kpm.getKey("a"):
        yawVelocity = -angularSpeed
        yaw-=angularInterval

    elif kpm.getKey("d"):
        yawVelocity = angularSpeed
        yaw+=angularInterval

    if kpm.getKey("q"):
        drone.land()
    if kpm.getKey("e"):
        drone.takeoff()

    sleep(interval)
    angle+=yaw
    x += int(distance * math.cos(math.radians(angle)))
    y += int(distance * math.sin(math.radians(angle)))

    return [leftRight, forwardBack, upDown, yawVelocity, x, y]

def drawPoints(img, points):
    for point in points:
        cv2.circle(img,point, 5, (0,0,255), cv2.FILLED)
    cv2.circle(img, points[-1], 8, (0, 255, 0), cv2.FILLED)
    cv2.putText(img,f'({(points[-1][0]-500)/100},{(points[-1][1]-500)/100})m',
                (points[-1][0]+10,points[-1][1]+30),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),1) #subtract 500 because 500 is starting pos, div 100 to give value in metres not cm

while True:
    values= getKeyboardInput()
    drone.send_rc_control(values[0],values[1],values[2],values[3])

    img=numpy.zeros((1000,1000,3), numpy.uint8)
    if (points[-1][0] != values[4] or points[-1][1] != values[5]):
        points.append((values[4],values[5]))
    drawPoints(img, points)
    cv2.imshow("Output",img)
    cv2.waitKey(1)