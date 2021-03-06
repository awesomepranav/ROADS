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
mdiff = MoveDifferential(OUTPUT_B, OUTPUT_C, EV3Tire, 16 * STUD_MM)
mdiff.on_for_distance(speed = 50, distance_mm = 690)
sleep(5)
mdiff.turn_left(speed = 50, degrees = 80)
mdiff.on_arc_right(SpeedRPM(60), 150, 65)
mdiff.on_for_distance(speed = 50, distance_mm = -145)
sleep(5)
medium_motorA.on_for_degrees(speed = 10, degrees = -110)
mdiff.on_arc_left(SpeedRPM(60), 150,67)
sleep(10)
mdiff.on_for_distance(10,50)
#sleep while picking up the first green piece
#medium_motorA.on_for_degrees(speed = 10, degrees = -110)
sleep(5)
#mdiff.turn_left(speed = 35, degrees = 10)
sleep(2)
medium_motorA.on_for_degrees(speed = 10, degrees = 110)
sleep(2)
mdiff.on_arc_right(SpeedRPM(60), 5200, 400)
sleep(5)
medium_motorA.on_for_degrees(speed = 10, degrees = -110)
sleep(5)
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
