#!/bin/bash

# script to generate random points and spawn the jackal

# Intro to Robotics - EE5900 - Spring 2017
#          Assignment #4

#       Project #4 Group #2
#         Akhil (Team Lead)
#            Philip
#            Roger
#
# Revision: v1.1

cd catkin_ws/src/waypoint_patroling/rosbag_files/
bagFileName=`ls *`
echo "ROSbag file: $bagFileName found!"
cd -

echo "roslaunch waypoint_patroling waypoint_patroling_33.launch bag_file_name:=$bagFileName"
roslaunch waypoint_patroling waypoint_patroling_33.launch bag_file_name:=$bagFileName

