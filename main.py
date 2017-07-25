# -*- coding: utf-8 -*-

ID = '00:16:53:00:F5:A9'

# Just the imports for using nxt
import nxt.locator
from nxt.motor import *
from nxt.motor import Motor, PORT_A, PORT_B, PORT_C
from nxt.sensor import Light, Sound, Touch, Ultrasonic
from nxt.sensor import PORT_1, PORT_2, PORT_3, PORT_4

# Locate the brick
b = nxt.locator.find_one_brick()
print "connected"

# Here you can change the frequencies to change the notes
FREQ_C = 523
FREQ_D = 587
FREQ_E = 659
FREQ_F = 698
FREQ_G = 784

# NXT plays a tone when is ready to play

b.play_sound_file(False, 'Good.rso')

# Reset the speed control (the motor tacho count)
Motor(b, PORT_A).reset_position(True)

if b:
    while True:
        if Touch(b, PORT_4).get_sample():
            note = Ultrasonic(b, PORT_1).get_sample()
            print note
            time = Motor(b, PORT_A).get_tacho().block_tacho_count
            print time
            if time > 0 and time < 20:
                time = 100
            elif time > 20 and time < 40:
                time = 500
            else:
                time = 1000
            if note < 9:
                b.play_tone(FREQ_C, 100+time)
                print "C"
            elif note >= 9 and note < 13:
                b.play_tone(FREQ_D, 100+time)
                print "D"
            elif note >= 13 and note < 17:
                b.play_tone(FREQ_E, 100+time)
                print "E"
            elif note >= 17 and note < 20:
                b.play_tone(FREQ_F, 100+time)
                print "F"
            else:
                b.play_tone(FREQ_G, 100+time)
                print "G"

else:
   print 'No NXT bricks found'
