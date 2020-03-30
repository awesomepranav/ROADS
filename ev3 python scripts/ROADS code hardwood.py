#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveDifferential
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS
from ev3dev2.wheel import EV3Tire 
from time import sleep 
from ev3dev2.motor import MediumMotor, OUTPUT_A
medium_motorA = MediumMotor(OUTPUT_A)
large_motorB = LargeMotor(OUTPUT_B)
large_motorC = LargeMotor(OUTPUT_C)
STUD_MM = 8
#created mdiff object
mdiff = MoveDifferential(OUTPUT_B, OUTPUT_C, EV3Tire, 16 * STUD_MM)
# move straight
mdiff.on_for_distance(speed = 50, distance_mm = 690)
sleep(5)
# turn left for 60 degrees
mdiff.turn_left(speed = 50, degrees = 60)
#arc with radius 150 and distance 65
mdiff.on_arc_right(SpeedRPM(60), 150, 65)
mdiff.on_for_distance(speed = 50, distance_mm = -145)
sleep(5)
# moving the arm down
medium_motorA.on_for_degrees(speed = 10, degrees = -110)
mdiff.on_arc_left(SpeedRPM(60), 125,67)
sleep(10)
mdiff.on_for_distance(10,50)
sleep(5)
#moving the arm up
medium_motorA.on_for_degrees(speed = 10, degrees = 110)
sleep(2)
#moving the arm back down
medium_motorA.on_for_degrees(speed = 10, degrees = -110)
sleep(5)
#arc with radius 1200 and distance 400
mdiff.on_arc_left(SpeedRPM(50), 1200, 400)
sleep(5)
#moving the arm up with second sample and next commands are going to cache site 
medium_motorA.on_for_degrees(speed = 10, degrees = 110)
sleep(2)
mdiff.turn_left(speed = 50, degrees = 38)
sleep(2)
mdiff.on_for_distance(speed = 50, distance_mm = 800)
sleep(2)
mdiff.turn_right(speed = 50, degrees = 75)
sleep(2)
mdiff.on_for_distance(speed = 50, distance_mm = 700)
sleep(2)
mdiff.turn_right(speed = 65, degrees = 45)
sleep(2)
#moving the arm down near the cache site
medium_motorA.on_for_degrees(speed = 10, degrees = -110)
sleep(2)
mdiff.on_for_distance(speed = 50, distance_mm = -50)
sleep(2)
#moving the arm up after disengaging with both samples
medium_motorA.on_for_degrees(speed = 10, degrees = 110)
sleep(2)
mdiff.turn_left(speed = 50, degrees = 65)
mdiff.on_for_distance(speed = 50, distance_mm = 250)
mdiff.turn_right(speed = 50, degrees = 75)
mdiff.on_for_distance(speed = 50, distance_mm = 900)
mdiff.turn_left(speed = 50, degrees = 40)
sleep(2)
#moving the arm down for sample 4
medium_motorA.on_for_degrees(speed = 10, degrees = -110)  
sleep(2)
mdiff.on_arc_right(SpeedRPM(60), 100, 175)
sleep(2)
#moving the arm up with sample #4 
medium_motorA.on_for_degrees(speed = 10, degrees = 110)
#sleep while picking up the second green piece
#sleep a second after each command finishes 
#mdiff.turn_left(speed = 50, degrees = 90)
#sleep(1)
#mdiff.on_for_distance(speed = 50, distance_mm = 1500)
#sleep(1)
#mdiff.turn_right(speed = 50, degrees = 90)
#sleep(1)
#mdiff.on_for_distance(speed = 50, distance_mm = 1000)
#sleep(1)
#mdiff.turn_right(speed = 50, degrees = 90)
#sleep(1)
#mdiff.on_for_distance(speed = 50, distance_mm = 750)
#sleep while dropping the 2 green samples in the cache circle 
#medium_motorA.on_for_degrees(speed = 50, degrees = 180)
#sleep(10)
#mdiff.turn_left(speed = 10, degrees = 50)
#sleep(1)
#mdiff.on_for_distance(speed = 50, distance_mm = 2000)
#sleep(1)
#mdiff.turn_right(speed = 50, degrees = 50)
