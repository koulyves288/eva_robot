#!/bin/bash

# 1. Start Isaac Sim in the background
# (Update path to your specific USD file)
echo "🚀 Launching Isaac Sim..."
~/isaacsim/isaac-sim.sh --file ~/home/koulyves/documents/eva_robot/eva_urdf_v3.usd &
ISAAC_PID=$!

# 2. Wait for Isaac Sim to fully load
# (Adjust seconds depending on how fast your PC loads the stage)
echo "⏳ Waiting 30 seconds for Sim to initialize..."
sleep 30

# 3. Launch the ROS Stack (SLAM, Controller, RViz)
echo "🤖 Launching ROS 2 Stack..."
ros2 launch ~/home/koulyves/documents/eva_robot/eva_stack.launch.py

# Cleanup: When you close the terminal, kill Isaac Sim too
kill $ISAAC_PID