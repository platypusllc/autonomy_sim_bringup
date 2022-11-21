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
    ld.add_action(cop_node)
    ld.add_action(sim_node)
    return ld