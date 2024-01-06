"""
fixed volumne theremin
theremin adapted from https://projects.raspberrypi.org/en/projects/ultrasonic-theremin/5
"""

from gpiozero import DistanceSensor, TonalBuzzer
from gpizero.tones import Tone
from time import sleep

def distance_to_tone(d):
    min_tone = buzzer.min_tone.midi
    max_tone = buzzer.max_tone.midi
    tone_range = max_tone - min_tone
    return min_tone + int(tone_range * d)

def loop(p_sens, bzr):
    while True:
        pitch_d = p_sens.distance_cm()
        tone = distance_to_tone(pitch_d)
        print(f'distance: {pitch_d}\tfrequency: {tone}')
        bzr.play(Tone(midi=tone))
        sleep(1)

if __name__ == '__main__':
    # sensor set up
    pitch_sensor = DistanceSensor(trigger=17, echo=27)
    # buzzer set up
    buzzer = TonalBuzzer(21, octaves=3)
    # run the loop
    loop(pitch_sensor, buzzer)