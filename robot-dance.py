from robomaster import robot, chassis, gimbal
import time

robot = robot.Robot()
chassis = robot.chassis
gimbal = robot.gimbal

# Define a function to perform a dance
def perform_dance():
    # Move the robot forward
    chassis.move(x=50, y=0, z=0)
    time.sleep(2)  # Wait for 2 seconds
    chassis.stop()  # Stop the robot
    time.sleep(1)  # Wait for 1 second
    # Rotate the gimbal
    gimbal.rotate(30, 0)
    time.sleep(1)  # Wait for 1 second
    # Move the robot backward
    chassis.move(x=-50, y=0, z=0)
    time.sleep(2)  # Wait for 2 seconds
    chassis.stop()  # Stop the robot

# Call the function to perform the dance
perform_dance()