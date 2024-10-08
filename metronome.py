from lpminimk3 import Mode, find_launchpads
import random
import time



print(find_launchpads())
lp = find_launchpads()[0]  # Get the first available launchpad
lp.open()  # Open device for reading and writing on MIDI interface (by default)

lp.mode = Mode.PROG  # Switch to the programmer mode

for led in lp.panel.led_range():  # Loop through all LEDs
    led.color = random.randint(1, 127)  # Set LED to a random color

time.sleep(5)  # Keep LEDs on for a while

for led in lp.panel.led_range():
    del led.color  # Turn off LED
