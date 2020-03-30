#moving the arm back down
def sample2():

    medium_motorA.on_for_degrees(speed = 10, degrees = -110)
    sleep(5)
#go to sample 2 position 
    mdiff.on_arc_left(SpeedRPM(50), 1200, 400)
    sleep(5)
#moving the arm up with second sample and next commands are going to cache site 
    medium_motorA.on_for_degrees(speed = 10, degrees = 110)
sample2()
sleep(2)
mdiff.turn_left(speed = 50, degrees = 38)
sleep(2)
mdiff.on_for_distance(speed = 50, distance_mm = 800)
sleep(2)
mdiff.turn_right(speed = 50, degrees = 65)
sleep(2)
mdiff.on_for_distance(speed =50, distance_mm = 750)
sleep(2)
mdiff.turn_right(speed = 50, degrees = 55)
sleep(2)
mdiff.on_for_distance(speed = 50, distance_mm = 260)
#moving the arm down near the cache site
medium_motorA.on_for_degrees(speed = 10, degrees = -110)
sleep(2)
mdiff.on_for_distance(speed = 50, distance_mm = -50)
sleep(2)
#moving the arm up after disengaging with both samples
medium_motorA.on_for_degrees(speed = 10, degrees = 110)
sleep(2)
mdiff.turn_left(speed = 50, degrees = 50)
mdiff.on_for_distance(speed = 50, distance_mm = 250)
mdiff.turn_right(speed = 50, degrees = 65)
mdiff.on_for_distance(speed = 50, distance_mm = 900)
mdiff.turn_left(speed = 50, degrees = 40)
sleep(2)
#moving the arm down for sample 4
medium_motorA.on_for_degrees(speed = 10, degrees = -110)  
sleep(2)
mdiff.on_arc_right(SpeedRPM(50), 100, 175)
sleep(2)
mdiff.on_for_distance(speed = 50, distance_mm = 300)
#moving the arm up with sample #4 
medium_motorA.on_for_degrees(speed = 10, degrees = 110)
sleep(2)
#getting sample 3
def sample3():
    mdiff.on_for_distance(speed = 50,distance_mm = 350)
    sleep(2)
    #putting arm down
    medium_motorA.on_for_degrees(speed = 10, degrees = -110)
    mdiff.on_arc_right(SpeedRPM(50), 70, 90)
    #putting arm back up
    medium_motorA.on_for_degrees(speed = 10, degrees = 110)
sample3()
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
