from microbit import *
import music

while True:
    temp = temperature()            # 온도 센서로 부터 온도값을 temp에 저장
    if temp > 30:                   # 온도 센서값이 32도를 초과하면
        display.show(Image.ANGRY)   # 내장된 ANGRY 이미지 출력
        display.scroll(temp)        # 온도 센서값을 LED 디스플레이에 출력
        music.play("B4:2")          # B음 출력
        sleep(10)                   # 0.01초 지연
    else:                           # 온도 센서값이 32도 이하이면
        music.stop()                # 멜로디 정지
        display.scroll(temp)        # 온도 센서값을 LED 디스플레이에 출력
