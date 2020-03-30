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
#mdiff.on_for_distance(speed = 50, distance_mm = 50)
mdiff.turn_left(speed = 50, degrees = 45)
mdiff.on_for_distance(speed = 50, distance_mm = 500)
mdiff.turn_left(speed = 50, degrees = 50)
mdiff.on_for_distance(speed = 50, distance_mm = 600)
mdiff.turn_right(speed = 50, degrees = 90)
mdiff.on_for_distance(speed = 50, distance_mm = 850)
mdiff.turn_right(speed = 50, degrees = 80)
midff.on_for_distance(speed = 50, distance_mm = 600)
sleep(2)
medium_motorA.on_for_degrees(speed = 8, degrees = -110)
sleep(2)
medium_motorA.on_for_degrees(speed = 8, degrees = 110)