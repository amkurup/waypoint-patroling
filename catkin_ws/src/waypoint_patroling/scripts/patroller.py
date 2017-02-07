#!/usr/bin/env python
import sys
import rospy
import actionlib
#from tf import transformations as t
#from tf import TransformListener
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from move_base_msgs.msg	import MoveBaseAction, MoveBaseGoal


# Initialize Waypoint coordinates
coordinates = [[0 for x in range(3)] for y in range(8)]
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
coordinates[6][0] = -8
coordinates[6][1] = -2
coordinates[6][2] = 1
coordinates[7][0] = 8
coordinates[7][1] = -8
coordinates[7][2] = 1


# Function decides initial waypoint based on robot's current position
def setup_route(x, y):
    if ((x >= -6) and (x <= -2)) and ((y >= -3) and (y <= 0)):
        # Set course for WP 1
        start = 0
    elif ((x >= 5) and ((y > -7) and (y <= 4))):
        # Set course for WP 2
        start = 1
    elif ((x >= 1) and (x < 5)) and ((y >= -7) and (y <= -3)):
        # Set course for WP 3
        start = 2
    elif ((x >= 5) and (y >= 4)) or (((x >= 1) and (x <= 5)) and (y >= 7)):
        # Set course for WP 4
        start = 3
    elif ((x > -7) and (x <= -2)) and ((y >= 0) and (y <= 5)):
        # Set course for WP 5
        start = 4
    elif ((x <= -1) and (y >= 5)) or ((x <= -7) and (y < -4)):
        # Set course for WP 6
        start = 5
    elif ((x <= -7) and (y <= 4)) or ((x <= -4) and (y <= -3)):
        # Set course for WP 7
        start = 6
    elif (x >= 1) and (y <= -7):
        # Set course for WP 8
        start = 7
    elif ((x >= -2) and (x <= 5)) and ((y >= -3) and (y < 7)):
        # For deciding in area with angled obstacles
        diff = x - y
        print "diff: %d" % diff
        if (diff <= 1) and (diff >= -1):
            # Set course for WP 1
            start = 0
        elif (diff >= 2):
            # set course for WP 2 or 3
            start = 1
        else:
            # Set course for WP 4 or 5
            start = 3
    elif ((x <= 1) and (x >= -4)) and (y <= -3):
        # For deciding in area with angled obstacle
        diff = x - (-1 * y)
        print "diff: %d" % diff
        if (diff >= -5):
            # Set course for WP 3
            start = 2
        else:
            # Set course for WP 8
            start = 7
    else:
        rospy.loginfo("Assert")
    rospy.loginfo("Start: %d" % start)
    return start


def patroller(i):
    mvbs = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    rate = rospy.Rate(50)

    mvbs.wait_for_server()
    rospy.loginfo("Waiting for the move_base action server to come up")
    backtrack = False # variable used to decide when to reverse patrol route


    while not rospy.is_shutdown():
        pt = MoveBaseGoal()
        pt.target_pose.header.frame_id = 'map'
        pt.target_pose.header.stamp = rospy.Time.now()
        pt.target_pose.pose.position = Point(coordinates[i][0], coordinates[i][1], 0)

        pt.target_pose.pose.orientation.x = 0
        pt.target_pose.pose.orientation.y = 0
        pt.target_pose.pose.orientation.z = 0
        pt.target_pose.pose.orientation.w = coordinates[i][2]
        # Send next waypoint goal, wait until goal is reached, iterate to next waypoint
        mvbs.send_goal(pt)
        mvbs.wait_for_result()
        # Complete current patrol route until route ends, then backtrack
        if backtrack == False:
            if i >= 7:
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
        rate.sleep()
if __name__ == "__main__":
    rospy.init_node("mapper")
    try:
        # Take in robot's initial starting coordinates
        origin_x = int(sys.argv[1])
        origin_y = int(sys.argv[2])
        rospy.loginfo("Recieved coordinates: [%d, %d]" % (origin_x, origin_y))
        first_waypoint = setup_route(origin_x, origin_y)
        patroller(first_waypoint)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
