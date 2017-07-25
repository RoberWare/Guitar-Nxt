# -*- coding: utf-8 -*-

ID = '00:16:53:00:F5:A9'

import sys

# Just the imports for using nxt
import nxt.locator
from nxt.motor import *
from nxt.motor import Motor, PORT_A, PORT_B, PORT_C
from nxt.sensor import Light, Sound, Touch, Ultrasonic
from nxt.sensor import PORT_1, PORT_2, PORT_3, PORT_4

print "Finding a brick..."

try:
    # Locate the brick
    b = nxt.locator.find_one_brick()
    print "Brick connected"
except:
    print "Sorry, we couldn't find a nxt brick..."
    sys.exit()

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

# If the brick has been found
if b:
    # Main while
    while True:
        # When you press the button
        try:
            if Touch(b, PORT_4).get_sample():
                # Obtain ultrasonic sample (distance)
                note = Ultrasonic(b, PORT_1).get_sample()
                # Obtain the position of the motor for adjust the note's lenght
                time = Motor(b, PORT_A).get_tacho().block_tacho_count
                # Associate the position of the motor with the lenght of the note
                if time > 0 and time < 20:
                    time = 100
                elif time > 20 and time < 40:
                    time = 500
                else:
                    time = 1000
                # Associate the fret position with a note
                if note < 9:
                    b.play_tone(FREQ_C, 100+time)
                    print "C", note, time
                elif note >= 9 and note < 13:
                    b.play_tone(FREQ_D, 100+time)
                    print "D",note,time
                elif note >= 13 and note < 17:
                    b.play_tone(FREQ_E, 100+time)
                    print "E",note,time
                elif note >= 17 and note < 20:
                    b.play_tone(FREQ_F, 100+time)
                    print "F",note,time
                else:
                    b.play_tone(FREQ_G, 100+time)
                    print "G",note,time
        except:
            print "Brick disconnected"
            sys.exit()

else:
   print 'No NXT bricks found'
