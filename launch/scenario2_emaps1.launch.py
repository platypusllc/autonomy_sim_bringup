from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction

def generate_launch_description():
    ld = LaunchDescription()
    cop_node = Node(
        package="autonomy",
        executable="cop",
    )
    sensor_node = Node(
        package="autonomy",
        executable="sensors")
    task_node = Node(
        package="autonomy",
        executable="taskman"
    )
    mission_node = Node(
        package="autonomy",
        executable="missionman",
        parameters=[{'mission_filename': './config/scenario2_emaps1.json'}]
    )

    ta = TimerAction(period=5., actions=[task_node])
    ma = TimerAction(period=10., actions=[mission_node])
    ld.add_action(cop_node)
    ld.add_action(sensor_node)
    #ld.add_action(task_node)
    #ld.add_action(mission_node)
    ld.add_action(ta)
    ld.add_action(ma)
    return ld