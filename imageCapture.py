from djitellopy import tello # give access to the tello library
import cv2

drone=tello.Tello()
drone.connect() #connects Tello to the code
print("Battery of drone:",drone.get_battery()) #displays how much battery the drone has

drone.streamon() #give all frames one by one

while True:
    img=drone.get_frame_read().frame #gives the image from the drone
    img=cv2.resize(img,(360,240)) #small frame size means faster
    cv2.imshow("POV: You are a Drone",img) #creates a window to show the result
    cv2.waitKey(1) #give it a delay of 1 millisecond