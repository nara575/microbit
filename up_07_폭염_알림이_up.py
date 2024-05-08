#폭염특보 기준을 보면, 폭염 경보는 낮기온 35도 이상, 폭염 주의보는 낮기온 33도 이상
from microbit import *
import music

while True:
    temp = temperature() #온도 센서로 부터 온도값을 temp에 저장
    if temp >= 35: #온도 값이 35도 이상이면
        display.show(Image.ANGRY) #디스플레이에 성난표정 이미지 표시
        music.play("G5:4") #G[5옥타브 솔]음 출력
        sleep(1000) #1초 지연
    elif temp >= 33: #온도 값이 33도 이상이면
        display.show(Image.SURPRISED) #디스플레이에 놀란표정 이미지 표시
        music.play("D4:4") #D[4옥타브 레]음 출력
        sleep(1000) #1초 지연
    else:
        music.stop() #멜로디 정지
        display.scroll(temp) #온도값 디스플레이에 표시