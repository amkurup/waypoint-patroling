# waypoint-patroling
Group 2 Assignment 4 (EE5900)

Team --
Akhil (Team Lead)
Roger
Philip

After cloning this repository, follow these steps to setup the Dev environment.
```
$ cd catkin_ws/src
$ catkin_init_workspace
$ cd ..
$ git submodule init
$ git submodule update
```

Finally, the project can be built as follows:

```
$ catkin_make
$ source devel/setup.bash
```

To run patroller.py script:

```
$ rosrun waypoint_patroling patroller.py X Y
```
Arguements X and Y are the initial map coordinates of the jackal on launch, [X, Y].
