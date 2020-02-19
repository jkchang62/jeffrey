#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch

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

## Note: 32 refers to the center button (center dark grey button in the instructions)!
print("Reading input...")

# Objective One: Odometry
# While loop that finishes when objective one is completed.
while not (objectiveOneCompleted):
    if (32 in brick.buttons()):
        # Remember the original distance to calculate delta x later.
        originalDistance = ultraSonicSensor.distance()

        # Move the robot forward for 5 seconds and then stop.
        leftWheel.run(515)
        rightWheel.run(515)
        wait(5000)
        leftWheel.stop()
        rightWheel.stop()

        # Finish the objective.
        print("Objective One Completed")
        print("Final distance moved is " + str((originalDistance - ultraSonicSensor.distance()) / 1000) + "m.")
        brick.sound.beep()
        objectiveOneCompleted = True

# Buffer
wait(1000)
print("Reading input...")

# Objective Two: Ranging
# While loop that finishes when objective two is completed.
while not (objectiveTwoCompleted):
    if (32 in brick.buttons()):
        # Keep the robot moving until it is <= 50 cm away from the target.
        while (ultraSonicSensor.distance() > 500):
            # Move the robot forward.
            leftWheel.run(500)
            rightWheel.run(500)

        # Stop the robot from moving once it is within 50cm away from the target.
        leftWheel.stop()
        rightWheel.stop()
        print("The robot is " + str(ultraSonicSensor.distance() / 10) + " cm away.")

        # Finish the objective.
        print("Objective Two Completed")
        brick.sound.beep()
        objectiveTwoCompleted = True

# Buffer
wait(1000)

# Objective Three: Bumping
# While loop that finishes when objective three is completed.
while not (objectiveThreeCompleted):

    if (32 in brick.buttons()):
        # While loop that runs as long as the robot has not hit an object.
        while not (touchSensor.pressed()):
            # Move the robot forwards.
            leftWheel.run(500)
            rightWheel.run(500)

        # Stops the wheels once contact has been made.
        leftWheel.stop()
        rightWheel.stop()

        # Reinitializing the wheels to move the robot backwards.
        leftWheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        rightWheel = Motor(Port.D, Direction. COUNTERCLOCKWISE)

        # Running the wheels for 2.5s before stopping them.
        leftWheel.run(500)
        rightWheel.run(500)
        wait(2520)
        leftWheel.stop()
        rightWheel.stop()
        
        # Finish the objective.
        print("The robot is " + str(ultraSonicSensor.distance() / 10) + " cm away.")
        print("Objective Three Completed")
        objectiveThreeCompleted = True

print("Program is finished.")