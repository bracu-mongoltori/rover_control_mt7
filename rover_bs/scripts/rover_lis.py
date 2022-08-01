#! /usr/bin/env python3

from time import sleep 
import rospy
from std_msgs.msg import String

def keys_callback(data):
    print(data.data)
    sleep(0.01)

rospy.init_node('rover_lis', anonymous=True)
sub = rospy.Subscriber("rover_keys", String, keys_callback)


rospy.spin()