#! /usr/bin/env python3
import pygame
from time import sleep 
import rospy
from std_msgs.msg import String

class Controller():
    #this is specific to the rover
    def __init__(self):
        self.up = 119
        self.down = 115
        self.left = 97
        self.right = 100
        self.r = 114
        self.f = 102
        self.t = 116
        self.g = 103
        self.y = 121
        self.h = 104
        self.o = 111
        self.p = 112
        self.n = 110
        self.m = 109
        self.v = 118
        self.b = 98
        self.directions = [self.up, self.down, self.left, self.right, self.r, self.f, self.t, self.g, self.y, self.h, self.o, self.p, self.n, self.m, self.v, self.b]
        self.dir_states = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.outputs = ["up", "down", "left", "right", "r", "f", "t", "g", "y", "h", "o", "p", "n", "m", "v", "b"]
        self.keys_pressed = rospy.Publisher("rover_keys", String, queue_size=10)
        pygame.init()
        rospy.init_node('rover_pub', anonymous=True)
        window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Rover Controller")
        self.window = window

    def controller(self):
        while not rospy.is_shutdown():
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key not in self.directions:
                        break
                    pressed = self.directions.index(event.key)
                    self.dir_states[pressed] = True
                elif event.type == pygame.KEYUP:
                    if event.key not in self.directions:
                        break
                    released = self.directions.index(event.key)
                    self.dir_states[released] = False
            for dir in self.dir_states:
                if dir == True:
                    print(self.outputs[self.dir_states.index(dir)])
                    self.keys_pressed.publish(self.outputs[self.dir_states.index(dir)])
                else:
                    pass
            sleep(0.1)
            
controls = Controller()
if __name__ == "__main__":
    controls.controller()

#w --> 119
#a --> 97
#s --> 115
#d --> 100