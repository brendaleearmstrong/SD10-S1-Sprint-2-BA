# Desription: Robotmaster S1 shows his stuff dancing to "We are the Champions!"
# Song: We Are the Champions

from robomaster import robot, chassis, gimbal, media
import time

robot = robot.Robot()
chassis = robot.chassis
gimbal = robot.gimbal
media = robot.media

# Define a function to perform a dance to "We Are the Champions"
def perform_champions_dance():
    # Play the song "We Are the Champions"
    media.play(rm_define.media_music, volume=50, file_path="we_are_the_champions.mp3")
    time.sleep(2)  # Wait for 2 seconds
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
    # Stop the song "We Are the Champions"
    media.stop(rm_define.media_music)

# Call the function to perform the dance to "We Are the Champions"
perform_champions_dance()
