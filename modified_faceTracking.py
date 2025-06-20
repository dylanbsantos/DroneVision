import cv2
import numpy as np
from djitellopy import tello # give access to the tello library
import time
import os
print(os.path.isfile("Resources/haarcascade_frontalface_default.xml"))  # Should print True


drone=tello.Tello()
drone.connect() #connects Tello to the code
print("Battery of drone:",drone.get_battery()) #displays how much battery the drone has

drone.streamon() #give all frames one by one
drone.takeoff()
drone.send_rc_control(0,0,25,0) #goes a bit higher when taking off to meet average height
time.sleep(1.0) #goes up for 2.2secs



width, height, = 360, 240
forwardBackwardRange = [6200,6800] #sweet spot range
pid = [0.4, 0.4, 0] #proportional, integral, derivative
pError = 0

def findFace(img):
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    imgGrayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGrayscale, 1.1, 5)

    faceListC = [] #list of centre
    faceListA = [] #list of area

    for (x,y,width,height) in faces:
        cv2.rectangle(img, (x, y), (x + width,y + height),(0, 0, 255), 2) #draw rectangle around face
        cx = x + width // 2
        cy = y + height // 2
        area = width * height
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        faceListC.append([cx, cy])
        faceListA.append(area)
    if len(faceListC) != 0: #if its not empty
        i = faceListA.index(max(faceListA)) #give max value of area in INDEX FORM
        return img, [faceListC[i], faceListA[i]] #return image, index of max value of Centre and Area
    else:
        return img, [[0,0], 0] #if its empty return nothing



def trackFace(info, width, pid, pError):
    area = info[1]
    x,y = info[0]
    forwardBackward=0

    error = x - width//2 #x is the face, width//2 is the centre of the image. this finds how far it is (the deviation)
    speed = pid[0]*error + pid[1]*(error-pError)
    speed = int(np.clip(speed,-100,100)) #make sure it does not go below -100 and above 100

    if area > forwardBackwardRange[0] and area < forwardBackwardRange[1]: #the sweet spot where it stays still
        forwardBackward = 0 #don't move forward OR back
        print("staying still")
    if area > forwardBackwardRange[1]:
        forwardBackward = -20 #go back
        print("going back")
    elif area < forwardBackwardRange[0] and area != 0: #make sure if a face is NOT detected it doesnt just go forward
        forwardBackward = 20 #go forward
        print("going forward")




    if x == 0: #if nothing is detected then dont move speed wise
        speed = 0
        error = 0

    #print(speed, forwardBackward)

    drone.send_rc_control(0,forwardBackward,0,speed) #sends forward/Backward and Yaw velocity
    return error

#cap = cv2.VideoCapture(0)
while True:
    #_, img = cap.read()
    img=drone.get_frame_read().frame #gives the image from the drone
    img=cv2.resize(img,(width,height)) #resizes to w and h in the top
    img, info = findFace(img)
    pError = trackFace(info, width, pid, pError)
    #print("Center", info[0],"Area", info[1]) #center used to rotate the drone, area used to move forwards/backwards
    cv2.imshow("Outty Putty", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #if q key is pressed then land drone
        drone.land()
        break
# Additional import from keyPressModule
import keyPressModule as kpm
kpm.init()

# Toggle functionality
keyboardControlEnabled = False

# Main loop modification to include toggle
while True:
    # Toggle check
    if kpm.getKey("t"):
        keyboardControlEnabled = not keyboardControlEnabled
        time.sleep(0.3)  # Delay to prevent rapid toggling

    if keyboardControlEnabled:
        # Keyboard control logic
        vals = getKeyboardInput()
        drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    else:
        # Existing face tracking logic
        import cv2
import numpy as np
from djitellopy import tello # give access to the tello library
import time
import os
print(os.path.isfile("Resources/haarcascade_frontalface_default.xml"))  # Should print True


drone=tello.Tello()
drone.connect() #connects Tello to the code
print("Battery of drone:",drone.get_battery()) #displays how much battery the drone has

drone.streamon() #give all frames one by one
drone.takeoff()
drone.send_rc_control(0,0,25,0) #goes a bit higher when taking off to meet average height
time.sleep(1.0) #goes up for 2.2secs



width, height, = 360, 240
forwardBackwardRange = [6200,6800] #sweet spot range
pid = [0.4, 0.4, 0] #proportional, integral, derivative
pError = 0

def findFace(img):
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    imgGrayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGrayscale, 1.1, 5)

    faceListC = [] #list of centre
    faceListA = [] #list of area

    for (x,y,width,height) in faces:
        cv2.rectangle(img, (x, y), (x + width,y + height),(0, 0, 255), 2) #draw rectangle around face
        cx = x + width // 2
        cy = y + height // 2
        area = width * height
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        faceListC.append([cx, cy])
        faceListA.append(area)
    if len(faceListC) != 0: #if its not empty
        i = faceListA.index(max(faceListA)) #give max value of area in INDEX FORM
        return img, [faceListC[i], faceListA[i]] #return image, index of max value of Centre and Area
    else:
        return img, [[0,0], 0] #if its empty return nothing



def trackFace(info, width, pid, pError):
    area = info[1]
    x,y = info[0]
    forwardBackward=0

    error = x - width//2 #x is the face, width//2 is the centre of the image. this finds how far it is (the deviation)
    speed = pid[0]*error + pid[1]*(error-pError)
    speed = int(np.clip(speed,-100,100)) #make sure it does not go below -100 and above 100

    if area > forwardBackwardRange[0] and area < forwardBackwardRange[1]: #the sweet spot where it stays still
        forwardBackward = 0 #don't move forward OR back
        print("staying still")
    if area > forwardBackwardRange[1]:
        forwardBackward = -20 #go back
        print("going back")
    elif area < forwardBackwardRange[0] and area != 0: #make sure if a face is NOT detected it doesnt just go forward
        forwardBackward = 20 #go forward
        print("going forward")




    if x == 0: #if nothing is detected then dont move speed wise
        speed = 0
        error = 0

    #print(speed, forwardBackward)

    drone.send_rc_control(0,forwardBackward,0,speed) #sends forward/Backward and Yaw velocity
    return error

#cap = cv2.VideoCapture(0)
while True:
    #_, img = cap.read()
    img=drone.get_frame_read().frame #gives the image from the drone
    img=cv2.resize(img,(width,height)) #resizes to w and h in the top
    img, info = findFace(img)
    pError = trackFace(info, width, pid, pError)
    #print("Center", info[0],"Area", info[1]) #center used to rotate the drone, area used to move forwards/backwards
    cv2.imshow("Outty Putty", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #if q key is pressed then land drone
        drone.land()
        break
    if kpm.getKey("q"): 
        drone.land()
        break

    time.sleep(0.05)

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0  # left-right, forward-backward, up-down, yaw-velocity
    speed = 50

    if kpm.getKey("LEFT"): lr = -speed
    elif kpm.getKey("RIGHT"): lr = speed

    if kpm.getKey("w"): ud = speed
    elif kpm.getKey("s"): ud = -speed

    if kpm.getKey("UP"): fb = speed
    elif kpm.getKey("DOWN"): fb = -speed

    if kpm.getKey("a"): yv = -speed
    elif kpm.getKey("d"): yv = speed

    return [lr, fb, ud, yv]
