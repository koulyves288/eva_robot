## Launch Terminal

The built in terminal in Ubuntu is not stable enough to run mupltiple terminal instances. Use the Terminator terminal instead

## Launch Isaac Sim - Open new terminal
cd ~isaacsim
./isaac-sim-selector.h

Action: Press PLAY inside the simulator

## Make the robot move - Open new terminal

ros2 topic pub --rate 10 /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.2, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.5}}"

Optional: You can also user the following command to lanuch teleop : ros2 run teleop_twist_keyboard teleop_twist_keyboard

## Launch SLAM (Mapping mode) - Open new terminal

ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True

## Launch Rviz - Open new Terminal

ros2 run rviz2 rviz2 --ros-args -p use_sim_time:=True

In RViz: Set Fixed Frame to map. Add Map (Topic: /map, QoS: Transient Local). Add LaserScan.

## AMCL, NAV2 Stack(Needs a map path) - Open new terminal

Note: DO NOT RUN THIS YET UNTIL YOU HAVE  A MAP SAVED

ros2 launch nav2_bringup bringup_launch.py use_sim_time:=True map:=/path/to/your_map.yaml

Note: You must replace /path/to/your_map.yaml with the actual file path of the map you saved

## How to Save Your Map - Open new terminal

When you are done driving the robot and like the map you see in RViz, run this command before closing anything:

ros2 run nav2_map_server map_saver_cli -f ~/my_new_map

Note: This creates my_new_map.pgm and my_new_map.yaml in your home folder


## Setting up xbox controller

### Test the controller to make sure it communicates with ubuntu

sudo apt install jstest-gtk -y
jstest-gtk

Note: This will Open the tool, click your controller, and click Properties. Move the sticks. If the bars move, Ubuntu sees it.

### Install the ROS 2 Drivers

sudo apt update
sudo apt install ros-jazzy-joy ros-jazzy-teleop-twist-joy -y

### Check if ROS is hearing the controller: In a new terminal

ros2 topic echo /joy

### Create config file for the controller
nano ~/my_xbox.yaml
Paste the content below:
teleop_twist_joy_node:
```yaml
ros__parameters:
    axis_linear:  {x: 1}   # Left Stick Up/Down
    scale_linear: {x: 0.7} # Max Speed (m/s)
    scale_linear_turbo: {x: 1.5}
    
    axis_angular: {yaw: 3} # Right Stick Left/Right
    scale_angular: {yaw: 1.0} # Turn Speed (rad/s)
    
    enable_button: 0       # Button 'A'
    require_enable_button: true
```
    
Press Ctrl+O, Enter to save.

Press Ctrl+X to exit.

### Launch the new file: In new terminal
ros2 launch teleop_twist_joy teleop-launch.py joy_config:='xbox' config_filepath:=/home/<user>/my_xbox.yaml

### Increase Forward speed (Linear)
ros2 param set /teleop_twist_joy_node scale_linear.x 1.5

### Increase turn speed (Angular)
ros2 param set /teleop_twist_joy_node scale_angular.yaw 1.5

### Checking controller data
ros2 topic echo /cmd_vel
ros2 topic echo /joy


