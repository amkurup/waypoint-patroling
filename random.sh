#!/bin/bash

point_x=0
point_y=0

point_x=$((RANDOM % 8))
point_y=$((RANDOM % 8))

let "point_x = $point_x - 5"
let "point_y = $point_y - 5"

echo "X location: $point_x"
echo "Y location: $point_y"

echo "roslaunch waypoint_patroling waypoint_patroling_2.launch spawn:="$point_x $point_y""
#roslaunch waypoint_patroling waypoint_patroling_2.launch spawn:="$point_x $point_y"
sed -i 's/-x 0 -y 0/-x '$point_x' -y '$point_y'/g' catkin_ws/src/waypoint_patroling/launch/waypoint_patroling_2.launch
