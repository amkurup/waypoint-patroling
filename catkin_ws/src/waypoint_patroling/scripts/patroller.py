#!/usr/bin/env python
import rospy
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from move_base_msgs.msg	import MoveBaseAction, MoveBaseGoal


def patroller():
    mvbs = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    mvbs.wait_for_server()
    rospy.loginfo("Waiting for the move_base action server to come up")

    pt = MoveBaseGoal()
    pt.target_pose.header.frame_id = 'map'
    pt.target_pose.header.stamp = rospy.Time.now()
    pt.target_pose.pose.position = Point(1,2,0)

    pt.target_pose.pose.orientation.x = 0
    pt.target_pose.pose.orientation.y = 0
    pt.target_pose.pose.orientation.z = 0
    pt.target_pose.pose.orientation.w = 1

    while not rospy.is_shutdown():
        mvbs.send_goal(pt)
        mvbs.wait_for_result()

if __name__ == "__main__":
    rospy.init_node("mapper")
    try:
        patroller()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
