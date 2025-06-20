from djitellopy import tello
import keyPressModule as kpm
from time import sleep

kpm.init()
drone=tello.Tello()
drone.connect()
print("Battery of Drone is", drone.get_battery())

def getKeyboardInput():
    leftRight, forwardBack, upDown, yawVelocity = 0,0,0,0
    speed=50
    if kpm.getKey("LEFT"):
        leftRight = -speed
    elif kpm.getKey("RIGHT"):
        leftRight = speed

    if kpm.getKey("w"):
        upDown = speed
    elif kpm.getKey("s"):
        upDown = -speed

    if kpm.getKey("UP"):
        forwardBack = speed
    elif kpm.getKey("DOWN"):
        forwardBack = -speed

    if kpm.getKey("a"):
        yawVelocity = -speed
    elif kpm.getKey("d"):
        yawVelocity = speed

    if kpm.getKey("q"):
        drone.land()
    if kpm.getKey("e"):
        drone.takeoff()

    return [leftRight, forwardBack, upDown, yawVelocity]


while True:
    values= getKeyboardInput()
    drone.send_rc_control(values[0],values[1],values[2],values[3])
    sleep(0.05)