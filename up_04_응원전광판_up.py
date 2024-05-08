from microbit import *

display.show(10)

while True:
    if button_b.is_pressed():
        display.show(10)
    if button_a.is_pressed():
        count = 9
        for a in range(10):
            sleep(1000)
            display.show(count)
            count = count-1