from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from launch_ros.actions import Node

def generate_launch_description():

    set_tb3_model = SetEnvironmentVariable(
        name='TURTLEBOT3_MODEL',
        value='burger'
    )

    set_gazebo_model_path = SetEnvironmentVariable(
        name='GAZEBO_MODEL_PATH',
        value='/opt/ros/humble/share/turtlebot3_gazebo/models'
    )

    set_gazebo_plugin_path = SetEnvironmentVariable(
        name='GAZEBO_PLUGIN_PATH',
        value='/opt/ros/humble/lib'
    )

    gazebo = ExecuteProcess(
        cmd=[
            'ros2', 'launch',
            'turtlebot3_gazebo',
            'empty_world.launch.py'
        ],
        output='screen'
    )
    
    odom_logger = Node(
        package='robot_control_interface',
        executable='odom_logger_node',
        output='screen'
    )

    click_node = Node(
        package='robot_control_interface',
        executable='click_control_node',
        output='screen'
    )

    return LaunchDescription([
        set_tb3_model,
        set_gazebo_model_path,
        set_gazebo_plugin_path,
        gazebo,
        click_node,
        odom_logger
    ])
