#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
import numpy as np

data_pose=np.load('/home/georges/zabre_ws/src/external_nodes/data/pose_meas_15.npy')

def publish_ee_pose():

    pub = rospy.Publisher('/optitrack_pose', PoseStamped,queue_size=10)

    rospy.init_node('moverobot', anonymous=True)

    R=rospy.Rate(1000)

    #define the pose message
    pose_msg = PoseStamped()
    rospy.sleep(5)

    pose_msg.header.stamp=rospy.Time.now()
    pose_msg.header.frame_id=''

    for index, pose in enumerate(data_pose):

        pose_msg.pose.position.x,pose_msg.pose.position.y,pose_msg.pose.position.z,pose_msg.pose.orientation.x,pose_msg.pose.orientation.y,pose_msg.pose.orientation.z,pose_msg.pose.orientation.w=pose
            
        pub.publish(pose_msg)
        print(index)
        rospy.sleep(0.001)

    print('Pose Published')
    print(data_pose[-1])
    rospy.spin()

        


if __name__ == '__main__':
    try:
        publish_ee_pose()
    except rospy.ROSInterruptException:
        pass
