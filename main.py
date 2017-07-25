# -*- coding: utf-8 -*-

ID = '00:16:53:00:F5:A9'

import nxt.locator
from nxt.motor import *
from nxt.motor import Motor, PORT_A, PORT_B, PORT_C
from nxt.sensor import Light, Sound, Touch, Ultrasonic
from nxt.sensor import PORT_1, PORT_2, PORT_3, PORT_4

b = nxt.locator.find_one_brick()
print "connected"

FREQ_C = 523
FREQ_D = 587
FREQ_E = 659
FREQ_G = 784

b.play_tone_and_wait(FREQ_C, 1000)

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
            if note < 10:
                b.play_tone_and_wait(FREQ_C, 100+time)
            elif note >= 10 and note < 14:
                b.play_tone_and_wait(FREQ_D, 100+time)
            elif note >= 14 and note < 18:
                b.play_tone_and_wait(FREQ_E, 100+time)
            else:
                b.play_tone_and_wait(FREQ_G, 100+time)

else:
   print 'No NXT bricks found'
