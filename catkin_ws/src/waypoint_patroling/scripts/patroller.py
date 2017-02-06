#!/usr/bin/env python
import rospy
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from move_base_msgs.msg	import MoveBaseAction, MoveBaseGoal

coordinates = [[0 for x in range(3)] for y in range(7)]
coordinates[0][0] = -3
coordinates[0][1] = -1
coordinates[0][2] = 1
coordinates[1][0] = 7
coordinates[1][1] = -2
coordinates[1][2] = 1
coordinates[2][0] = 1
coordinates[2][1] = -4
coordinates[2][2] = 1
coordinates[3][0] = 3
coordinates[3][1] = 8
coordinates[3][2] = 1
coordinates[4][0] = -3
coordinates[4][1] = 3
coordinates[4][2] = 1
coordinates[5][0] = -5
coordinates[5][1] = 7
coordinates[5][2] = 1
coordinates[6][0] = 8
coordinates[6][1] = -8
coordinates[6][2] = 1

def patroller():
    mvbs = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    mvbs.wait_for_server()
    rospy.loginfo("Waiting for the move_base action server to come up")
    i = 0
    backtrack = False
    while not rospy.is_shutdown():
        pt = MoveBaseGoal()
        pt.target_pose.header.frame_id = 'map'
        pt.target_pose.header.stamp = rospy.Time.now()
        pt.target_pose.pose.position = Point(coordinates[i][0], coordinates[i][1], 0)

        pt.target_pose.pose.orientation.x = 0
        pt.target_pose.pose.orientation.y = 0
        pt.target_pose.pose.orientation.z = 0
        pt.target_pose.pose.orientation.w = coordinates[i][2]

        mvbs.send_goal(pt)
        mvbs.wait_for_result()
        if backtrack == False:
            if i >= 6:
                backtrack = True
                i -= 1
            else:
                i += 1
            print "i: %d" % i
        else:
            if i == 0:
                backtrack = False
                i = 0
            else:
                i -= 1
            print "i is now: %d" % i
if __name__ == "__main__":
    rospy.init_node("mapper")
    try:
        patroller()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
