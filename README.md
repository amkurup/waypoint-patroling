# waypoint-patroling
EE5900: Group #2 Assignment #4

#Team --
> Akhil (Team Lead)

> Roger

> Philip

# Working of the project
> The initial map is created using launch file 1. This map has been edited previously and saved.
> The random script will generate random points between 0 to 7 and shift it by -5.
> These points are then used as the X and Y coordinates to launch the 2nd file. This file spawns 
the jackal in the random location and traverses it through the map following the waypoints.
> This motion is stored in a rosbag file and is used by the 3rd launch file to play-back the motion
on the original map.

1. Clone the repository

2. Follow these steps to setup the environment:
  > $ cd catkin_ws/src

  > $ catkin_init_workspace

  > $ cd ..

  > $ git submodule init

  > $ git submodule update

3. Build the project as follows:
  > $ catkin_make

  > $ source devel/setup.bash

4. To run the complete project:
  > $ cd catkin_ws

  > $ ./random.sh

  > after the complete map has been traversed, use ctrl-C to stop

  > give a couple of minutes for gzserver to stop completely

  > $ ./random2.sh

