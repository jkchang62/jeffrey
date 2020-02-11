#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

## Lab One Program

# Global Variables
# Booleans for completed objectives
objectiveOneCompleted = False
objectiveTwoCompleted = False
objectiveThreeCompleted = False

# Wheels and sensors, respectively
leftWheel = Motor(Port.A)
rightWheel = Motor(Port.D)
touchSensor = TouchSensor(Port.S2)
ultraSonicSensor = UltrasonicSensor(Port.S3)

# Stopwatch for objective three
stopWatch = None

## Note: 32 refers to the center button (center dark grey button in the instructions)

# Objective One: Odometry
# While loop that finishes when objective one is completed
while not (objectiveOneCompleted):
    if (32 in brick.buttons()):
        # Code to move forward goes here...

        print("Objective One Completed")
        objectiveOneCompleted = True

# Buffer
wait(1000)

# Objective Two: Ranging
# While loop that finishes when objective two is completed 
while not (objectiveTwoCompleted):
    if (32 in brick.buttons()):

        while (ultraSonicSensor.distance() >= 500):
            # Experiment with what angular velocity should be set - arg for the run method
            leftWheel.run()
            rightWheel.run()

            # Change buffer time accordingly
            wait(500)

        # End goal. Once the robot is 50cm away from the object, turn everything off and beep
        print("Objective Two Completed")
        leftWheel.stop()
        rightWheel.stop()
        brick.sound.beep()
        objectiveTwoCompleted = True

# Buffer
wait(1000)

# Objective Three: Bumping
# While loop that finishes when objective three is completed
while not (objectiveThreeCompleted):
    if (32 in brick.buttons()):

        # Code that reverses the robot goes here...
        while not (touchSensor.pressed()):
            # Experiment with what angular velocity should be set - arg for the run method
            leftWheel.run()
            rightWheel.run()

            # Checking if the robot is ~50cm away from the objec to track how long it'll take to get back to that same position
            # Change the margin of error dependng on the angular velocity 
            if (ultraSonicSensor.distance() >= 480 and ultraSonicSensor.distance() <= 520):
                stopWatch = Stopwatch()

            # Change buffer time accordingly
            wait(500)

        # End goal. Stopwatch is paused and the wheels will begin to turn counterclockwise for a certain duration of time, ideally back to 50cm away
        # Stopping the stopwatch and changing the direction of the wheels
        stopWatch.pause()
        leftWheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        rightWheel = Motor(Port.D, Direction. COUNTERCLOCKWISE)

        # Running and stopping the wheels after a certain amount of time
        leftWheel.run_time(..., stopWatch.time(), Stop.BRAKE)
        rightWheel.run_time(..., stopWatch.time(), Stop.BRAKE)
        leftWheel.stop()
        rightWheel.stop()
        
        print("Objective Three Completed")
        objectiveThreeCompleted = True

print("Program is finished.")