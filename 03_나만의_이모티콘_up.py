from microbit import *

while True:
    display.scroll("HEART")                  #디스플레이에 "HEART"라고 스크롤 형태로 표시
    display.show(Image.HEART)                #디스플레이에 큰하트 이미지 표시
    sleep(500)                               #0.5초 지연
    display.show(Image.HEART_SMALL)          #디스플레이에 작은하트 이미지 표시
    sleep(500)                               #0.5초 지연