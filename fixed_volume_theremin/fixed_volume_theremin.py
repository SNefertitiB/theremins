"""
fixed volumne theremin
theremin adapted from https://projects.raspberrypi.org/en/projects/ultrasonic-theremin/5
"""
from gpiozero import DistanceSensor, TonalBuzzer
from gpizero.tones import Tone
from time import sleep
from theremin_utils import signal_handler_exit

def distance_to_tone_midi(d:float) -> int:
    min_tone = buzzer.min_tone.midi
    max_tone = buzzer.max_tone.midi
    tone_range = max_tone - min_tone
    return min_tone + int(tone_range * d)

def distance_to_tone_hz(d:float) -> int:
    min_tone = buzzer.min_tone
    max_tone = buzzer.max_tone
    tone_range = max_tone - min_tone
    return min_tone + int(tone_range * d)

def loop(p_sens:DistanceSensor, bzr:TonalBuzzer) -> None:
    while True:
        pitch_d = p_sens.distance_cm()
        #TODO: They work at about 2cm to 450cm away, but we think 10cm-250cm is best
        if bzr.is_active and pitch_d > 0.25:
            bzr.stop()
        else:
            hz = distance_to_tone_hz(pitch_d)
            tone = Tone.from_frequency(hz)
            print(f'distance: {pitch_d}\tfrequency: {tone.note}')
            bzr.play(tone)
        sleep(1)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler_exit)   # Ctr+c to exit program
    # sensor set up
    pitch_sensor = DistanceSensor(trigger=17, echo=27)
    # buzzer set up
    buzzer = TonalBuzzer(21, octaves=2)
    print(f'lowest note:{buzzer.min_tone.midi} \thighest note:{buzzer.max_tone.midi}')
    # run the loop
    loop(pitch_sensor, buzzer)