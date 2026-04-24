from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Déclaration des arguments que l'utilisateur peut passer en ligne de commande
    res_arg = DeclareLaunchArgument(
        'resolution',
        default_value='720p',
        description='Résolution de la caméra'
    )
    
    fps_arg = DeclareLaunchArgument(
        'fps',
        default_value='30',
        description='Images par seconde'
    )

    # Configuration du nœud utilisant ces arguments
    camera_node = Node(
        package='challenge_9_launch',
        executable='camera_exe',
        parameters=[{
            'resolution': LaunchConfiguration('resolution'),
            'fps': LaunchConfiguration('fps')
        }]
    )

    return LaunchDescription([
        res_arg,
        fps_arg,
        camera_node
    ])
