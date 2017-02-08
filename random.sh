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

# define X and Y coordinate points
point_x=0
point_y=0
bagFileName=""

# generate random data points within +- 7
point_x=$((RANDOM % 8))
point_y=$((RANDOM % 8))

let "point_x = $point_x - 5"
let "point_y = $point_y - 5"

echo "X location: $point_x"
echo "Y location: $point_y"

# delete rosbag files if any
rm catkin_ws/src/waypoint_patroling/rosbag_files/*

# make intermediate file for launch
cp catkin_ws/src/waypoint_patroling/launch/waypoint_patroling_2.launch catkin_ws/src/waypoint_patroling/launch/waypoint_patroling_22.launch
# cp catkin_ws/src/waypoint_patroling/launch/waypoint_patroling_3.launch catkin_ws/src/waypoint_patroling/launch/waypoint_patroling_33.launch

# replace the spawn locations with the random points
sed -i 's/-x 0 -y 0/-x '$point_x' -y '$point_y'/g' catkin_ws/src/waypoint_patroling/launch/waypoint_patroling_22.launch
# sed -i 's/-x 0 -y 0/-x '$point_x' -y '$point_y'/g' catkin_ws/src/waypoint_patroling/launch/waypoint_patroling_33.launch

echo "roslaunch waypoint_patroling waypoint_patroling_22.launch spawn:="$point_x $point_y""
roslaunch waypoint_patroling waypoint_patroling_22.launch spawn:="$point_x $point_y"

cd catkin_ws/src/waypoint_patroling/rosbag_files/
bagFileName=`ls *`
echo "ROSbag file: $bagFileName found!"
cd -

echo "roslaunch waypoint_patroling waypoint_patroling_33.launch bag_file_name:=$bagFileName"
roslaunch waypoint_patroling waypoint_patroling_33.launch bag_file_name:=$bagFileName

# remove intermedite files
# rm catkin_ws/src/waypoint_patroling/launch/waypoint_patroling_22.launch
# rm catkin_ws/src/waypoint_patroling/launch/waypoint_patroling_33.launch

