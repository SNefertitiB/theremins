import sys, signal

# Global variables -- defined at theremin set-up
MIN_CM = 5     # smallest value distance sensor registers
MAX_CM = 160   # greatest value distance sensor registers
CM_RANGE = MAX_CM - MIN_CM

MIN_FREQ = 27   # lowest note in Hz
MAX_FREQ = 1036 # hightest note in Hz
FREQ_RANGE = MAX_FREQ - MIN_FREQ

MAX_VOLT = 3.3

def cm_to_percent(cm) -> float:
    if cm < MIN_CM or cm > MAX_CM:
        cm = 0
    d = (cm - MIN_CM) / CM_RANGE
    return d

def get_frequency(d:float) -> float:
    frequency = MIN_FREQ + (d * FREQ_RANGE)
    return frequency

def get_voltage(d:float) -> float:
    return d * MAX_VOLT



from time import sleep

def signal_handler_exit(signal, frame):
    print("\nSee you soon!")
    sys.exit(0)