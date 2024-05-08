from microbit import *

x = Image('90009:09090:00900:09090:90009')
o = Image('09990:90009:90009:90009:09990')

while True:
    pin0.write_digital(1)
    display.show(x)
    sleep(3000)
    pin0.write_digital(0)
    pin1.write_digital(1)
    display.show(o)
    sleep(5000)
    pin0.write_digital(1)
    pin1.write_digital(1)
    display.clear()
    sleep(2000)
    pin0.write_digital(0)
    pin1.write_digital(0)