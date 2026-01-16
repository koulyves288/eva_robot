import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # PATHS
    slam_pkg_path = get_package_share_directory('slam_toolbox')
    teleop_pkg_path = get_package_share_directory('teleop_twist_joy')
    
    # YOUR FILES (Update these paths!)
    xbox_config_file = '/home/koulyves/documents/eva_robot/my_xbox.yaml'
    # It is highly recommended to save your RViz setup once (File -> Save Config As)
    rviz_config_file = '/home/koulyves/documents/eva_robot/default.rviz' 

    return LaunchDescription([
        # 1. LAUNCH XBOX CONTROLLER
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(teleop_pkg_path, 'launch', 'teleop-launch.py')
            ),
            launch_arguments={
                'joy_config': 'xbox',
                'config_filepath': xbox_config_file
            }.items()
        ),

        # 2. LAUNCH SLAM (Delayed 5s to let Sim stabilize)
        TimerAction(
            period=5.0,
            actions=[
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(
                        os.path.join(slam_pkg_path, 'launch', 'online_async_launch.py')
                    ),
                    launch_arguments={'use_sim_time': 'True'}.items()
                )
            ]
        ),

        # 3. LAUNCH RVIZ
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_file],
            parameters=[{'use_sim_time': True}]
        )
    ])