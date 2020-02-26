#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch

# Lab Two Program
# Team Members
# - Katherine Li (730210643)
# - Jonathan Chang (730169520)

# Global Variables
# Wheels and sensors, respectively
leftWheel = Motor(Port.A)
rightWheel = Motor(Port.D)
ultraSonicSensor = UltrasonicSensor(Port.S2)
touchSensor = TouchSensor(Port.S3)

# Objective One: Detect the Wall.
while not (32 in brick.buttons()):
    # Move the robot forward.
    leftWheel.run(200)
    rightWheel.run(200)

    # If the robot bumps into the wall, stop the robot and back it up by 5cm.
    if (touchSensor.pressed()):
        # Stops the wheels once contact has been made.
        leftWheel.stop()
        rightWheel.stop()

        # Reinitializing the wheels to move the robot backwards.
        leftWheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        rightWheel = Motor(Port.D, Direction. COUNTERCLOCKWISE)

        # Moving the robot 5cm back.
        leftWheel.run(110)
        rightWheel.run(110)
        wait(2500)
        leftWheel.stop()
        rightWheel.stop()

        break

# Reinitialize the wheels to run forward again.
leftWheel = Motor(Port.A)
rightWheel = Motor(Port.D)

# Objective Two: Turn Right at the Wall.
leftWheel.run(150)
wait(3000)
leftWheel.stop()

# Continue the robot
rightWheel.run(300)
leftWheel.run(300)

# Objective Three: Following the Wall.
# While loops that ends once the the wall ends.
# Maximum distance of the ultrasonic sensor is 255 cm
while (ultraSonicSensor.distance() < 2050):

    # If the distance between the wall is too close, rotate more than the left wheel dramatically.
    if (ultraSonicSensor.distance() < 60): 
        rightWheel.run(200)
        leftWheel.run(300)

    # If the distance between the wall is close, rotate the left wheel faster.
    elif (ultraSonicSensor.distance() < 150):
        rightWheel.run(250)
        leftWheel.run(300)

    # If the distance between the wall is too far, rotate the right wheel faster.
    elif (ultraSonicSensor.distance() > 200):
        rightWheel.run(300)
        leftWheel.run(250)

    # Else, rotate the wheels at the same rate and go straight.
    else:
        rightWheel.run(300)
        leftWheel.run(300)


# Objective Four: Turn at the End of the Wall.
# Turn the robot
leftWheel.stop()
rightWheel.run(140)
wait(3000)
rightWheel.stop()

# Move the robot 70cm
leftWheel.run(486.1)
rightWheel.run(486.1)
wait(6000)
leftWheel.stop()
rightWheel.stop()