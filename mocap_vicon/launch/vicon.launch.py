from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mocap_vicon',
            executable='mocap_vicon_node',
            name='vicon',
            output='screen',
            # prefix=['gdb --args'],
            parameters=[
                {'server_address': 'mocap.perch'},
                {'frame_rate': 120},
                {'max_accel': 10.0},
                {'publish_tf': True},
                {'publish_pts': False},
                {'fixed_frame_id': 'mocap'},
                {'timer_pub_freq': 50},
                {'model_list': ['crazy_mpc1', 'crazy_jirl_test01']},
            ],
            remappings=[
                # Uncomment and modify the remapping if needed
                # ('vicon/model_name/odom', '/model_name/odom'),
            ]
        )
    ])
