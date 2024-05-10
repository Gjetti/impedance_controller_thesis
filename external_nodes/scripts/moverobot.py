#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
import numpy as np
import math
data_pose=np.load('/home/georges/zabre_ws/src/external_nodes/data/pose_meas_15.npy')
#position_data=data_pose[:,:3] 
#print(position_data[0])

def publish_end_effector_pose():

    pub = rospy.Publisher('/optitrack_pose', PoseStamped,queue_size=10)

    rospy.init_node('moverobot', anonymous=True)


    #define the pose message
    pose_msg = PoseStamped()
    rospy.sleep(5)

    pose_msg.header.stamp=rospy.Time.now()
    pose_msg.header.frame_id=''
    time=0.0




    while not rospy.is_shutdown():

        pose_msg.pose.position.x = 0.3069 + 0.05 * math.sin(time *2 * math.pi * 0.005)
        pose_msg.pose.position.y = 0.05 * math.sin(time *2 * math.pi * 0.005)
        pose_msg.pose.position.z = 0.4869 +0.05 * math.sin(time *2 * math.pi * 0.005)
        #pose_msg.pose.orientation.x,pose_msg.pose.orientation.y,pose_msg.pose.orientation.z,pose_msg.pose.orientation.w
        pose_msg.pose.orientation.x=0.999997589000513 +0.05 * math.sin(time *2 * math.pi * 0.005)
        pose_msg.pose.orientation.y=7.393322034417396e-05 +0.05 * math.sin(time *2 * math.pi * 0.005)
        pose_msg.pose.orientation.z=0.0001466273739544682 +0.05 * math.sin(time *2 * math.pi * 0.005)
        pose_msg.pose.orientation.w=2.105797886366375e-06 +0.05 * math.sin(time *2 * math.pi * 0.005)
        pub.publish(pose_msg)  
        time+=1
        rospy.sleep(0.1)


"""     for pose in data_pose:
        pose_msg.pose.position.x=pose[0]
        pose_msg.pose.position.y=pose[1]
        pose_msg.pose.position.z=pose[2]
        pose_msg.pose.orientation.x=pose[3]
        pose_msg.pose.orientation.y=pose[4]
        pose_msg.pose.orientation.z=pose[5]
        pose_msg.pose.orientation.w=pose[6]
        pub.publish(pose_msg)
        rospy.sleep(0.1)
    rospy.spin()     
 """




if __name__ == '__main__':
    try:
        publish_end_effector_pose()
    except rospy.ROSInterruptException:
        pass
