from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    cop_node = Node(
        package="autonomy",
        executable="cop",
    )
    sim_node = Node(
        package="simusv",
        executable="boatsim"
    )
    task_node = Node(
        package="autonomy",
        executable="taskman"
    )
    mission_node = Node(
        package="autonomy",
        executable="missionman"
    )
    ld.add_action(cop_node)
    ld.add_action(sim_node)
    ld.add_action(task_node)
    ld.add_action(mission_node)
    return ld