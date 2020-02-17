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
ultraSonicSensor = UltrasonicSensor(Port.S1)
touchSensor = TouchSensor(Port.S4)
robot = DriveBase(leftWheel, rightWheel, 56, 224)

## Note: 32 refers to the center button (center dark grey button in the instructions)!
print("Reading input...")

# Objective One: Odometry
# While loop that finishes when objective one is completed.
while not (objectiveOneCompleted):
    if (32 in brick.buttons()):
        # Move the robot forward.
        robot.drive_time(50, 0, 5000)

        # Finish the objective.
        print("Objective One Completed")
        objectiveOneCompleted = True

# Buffer
wait(1000)
print("Reading input...")

# Objective Two: Ranging
# While loop that finishes when objective two is completed.
while not (objectiveTwoCompleted):
    if (32 in brick.buttons()):
        # Keep the robot moving until it is <= 50 cm away from the object.
        while (ultraSonicSensor.distance() > 500):
            # Move the robot forward.
            robot.drive(150, 0)

            # Buffer
            wait(500)

        # Finish the objective.
        print("Objective Two Completed")
        brick.sound.beep()
        objectiveTwoCompleted = True

# Buffer
wait(1000)

# Objective Three: Bumping
# While loop that finishes when objective three is completed.
while not (objectiveThreeCompleted):
    # Stopwatch for objective three; used for the goal of moving the robot backwards 50cm.
    stopWatch = StopWatch()
    stopWatchActivated = False

    if (32 in brick.buttons()):
        # While loop that runs as long as the robot has not hit an object.
        while not (touchSensor.pressed()):
            # Moves the robot forwards.
            robot.drive(150, 0)

            # Checking if the robot is ~50cm away from the objec to track how long it'll take to get back to that same position.
            if (ultraSonicSensor.distance() >= 490 and ultraSonicSensor.distance() <= 510 and not stopWatchActivated):
                # Restart the stopwatch and start tracking new time.
                stopWatch.reset()

            # Buffer
            wait(50)

        # End goal. Stopwatch is paused and the wheels will begin to turn counterclockwise for a certain duration of time, ideally back to 50cm away
        # Stopping the stopwatch and changing the direction of the wheels
        print("Contact has been made")
        robot.stop()
        stopWatch.pause()

        # Reinitializing the wheels and drive base to go backwards
        leftWheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        rightWheel = Motor(Port.D, Direction. COUNTERCLOCKWISE)
        robot = DriveBase(leftWheel, rightWheel, 56, 224)

        # Running and stopping the wheels after a certain amount of time
        robot.drive_time(150, 0, stopWatch.time())
        
        # Finish the objective.
        print("Objective Three Completed")
        objectiveThreeCompleted = True

print("Program is finished.")