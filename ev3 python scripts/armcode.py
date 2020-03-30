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
medium_motorA.on_for_degrees(speed = 10, degrees = -110)
medium_motorA.on_for_degrees(speed = 10, degrees = 110)
