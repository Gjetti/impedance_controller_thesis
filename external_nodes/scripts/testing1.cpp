#include "ros/ros.h"
#include "geometry_msgs/PoseStamped.h"
#include <cmath>
#include <sstream>

int main(int argc, char **argv)
{
    ros::init(argc, argv, "testing1");
    ros::NodeHandle nh;

    // Create a publisher for the custom sine function
    ros::Publisher sine_pub = nh.advertise<geometry_msgs::PoseStamped>("/optitrack_pose", 10);

    ros::Rate loop_rate(1000); // Publish at 10 Hz
    double time=0;
    while (ros::ok())
    {
        // Create a message for the custom sine pose
        geometry_msgs::PoseStamped msg;

        // Assign the position to the message
        msg.pose.position.x = 0.3069+0.05*sin(time*0.01*2*3.14*0.01);
        msg.pose.position.y = 0.05*sin(time*0.01*2*3.14*0.01);
        msg.pose.position.z = 0.4869+0.05*sin(time*0.01*2*3.14*0.01);

        // Set orientation to identity quaternion
        msg.pose.orientation.w = 0.0;
        msg.pose.orientation.x = 1.0;
        msg.pose.orientation.y = 0.0;
        msg.pose.orientation.z = 0.0;

        // Set the header frame ID and timestamp
        msg.header.frame_id = "base_link"; // Set your desired frame ID
        msg.header.stamp = ros::Time::now();

        // Publish the message
        sine_pub.publish(msg);
	time++;
        // Sleep to maintain the desired publishing rate
        loop_rate.sleep();
    }

    return 0;
}

