#!/usr/bin/env python
'''improvingSAKLD ROS Node'''
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    '''improvingSAKLD Publisher'''
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('improvingSAKLD', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
