import pygame

def init():
    pygame.init()
    win=pygame.display.set_mode((400,400)) #set window size

def getKey(keyName): #tells whether a key has been pressed or not
    answer=False
    for i in pygame.event.get():
        pass #clears the pygame event queue without processing any events
    keyInput=pygame.key.get_pressed()
    myKey=getattr(pygame, 'K_{}'.format(keyName)) #puts keyName inside {}
    if keyInput[myKey]:
        answer=True
    pygame.display.update()
    return answer


def main():
    #print(getKey("a")) #will print True/False depending on whether "a" has been pressed or not
    if getKey("LEFT"):
        print("Left arrow key pressed")
    if getKey("RIGHT"):
        print("Right arrow key pressed")
    if getKey("UP"):
        print("Up arrow key pressed")
    if getKey("DOWN"):
        print("Down arrow key pressed")


if __name__ == '__main__': #checks if this is the main file running
    init() #if so then it will run init function
    while True:
        main() #and then constantly runs main function