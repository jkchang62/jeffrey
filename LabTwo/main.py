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
ultraSonicSensor = UltrasonicSensor(Port.S1)
touchSensor = TouchSensor(Port.S4)

print("Reading input...")

# print(ultraSonicSensor.distance())

# print("Done.")

# Objective One: Detect the Wall.
while (32 in brick.buttons()) {
    # Move the robot forward.
    leftWheel.run(200)
    rightWheel.run(200)

    # If the robot bumps into the wall, stop the robot and back it up by 50cm.
    if (touchSensor.pressed()) {
        # Stops the wheels once contact has been made.
        leftWheel.stop()
        rightWheel.stop()

        # Reinitializing the wheels to move the robot backwards.
        leftWheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        rightWheel = Motor(Port.D, Direction. COUNTERCLOCKWISE)

        # Moving the robot 50cm back.
        leftWheel.run(55)
        rightWheel.run(55)
        wait(4000)
        leftWheel.stop()
        rightWheel.stop()

        # Testing purposes
        print("The robot is " + ultraSonicSensor.distance() + " cm away from the wall")

        break
    }
}

# Reinitialize the wheels to run forward again.
leftWheel = Motor(Port.A)
rightWheel = Motor(Port.D)

# Objective Two: Turn Right at the Wall.
# Determine the angular velocity required to turn a quarter circle.
# Rotate the robot's left wheel until it is parallel to the wall
# Let Θ = 90° or 1.5708 rad and t = 5s, then w = 0.31416
# Using the equation v = wr, and w = 0.31416 and r = ?, then v = ?
leftWheel.run()
leftWheel.stop()

# Objective Three: Following the Wall.
# While loops that ends once the the wall ends.
# Maximum distance of the ultrasonic sensor is 255 cm
while (ultraSonicSensor.distance() < 2550) {
    if (ultraSonicSensor.distance() < 175) {
        while (ultraSonicSensor.distance() < 175) {
            rightWheel.stop()
            leftWheel.run(10)
        }
    } else if (ultraSonicSensor.distance() > 200) {
        while (ultraSonicSensor.distance() > 200) {
            leftWheel.stop()
            rightWheel.run(10)
        }
    }

    rightWheel.run(55)
    leftWheel.run(55)    
}

# Objective Four: Turn at the End of the Wall.

# Needs to move 6.20cm forwards before turning?
leftWheel.run(34)
rightWheel.run(34)
wait(4000)

# Turn the robot
# ...

# Move the robot 70cm
leftWheel.run(25.21)
rightWheel.run(25.21)
wait(6000)
leftWheel.stop()
rightWheel.stop()