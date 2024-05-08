from microbit import *  # 마이크로비트 모듈의 모든 명령 사용

while True:             # 무한 반복
    if button_a.is_pressed() and button_b.is_pressed(): # 만약 A, B를 동시에 누르면
        for a in range(5):                              # 5회 반복
            display.show(Image.HEART)                   # 내장된 HEART 이미지 출력
            sleep(100)                                  # 0.1초 지연
            display.show(Image.HEART_SMALL)             # 만약 내장된 HEART_SMALL 이미지 출력
            sleep(100)                                  # 0.1초 지연
    elif button_a.is_pressed():         # 그렇지 않고(A, B를 동시에 누르지 않고) 만약, A버튼을 누르면
        display.show("Fighting!")       # LED 디스플레이에 Fighting! 출력
    elif button_b.is_pressed():         # 그렇지 않고 만약, B버튼을 누르면
        display.scroll("Do your BEST!") # LED 디스플레이에 Do your BEST! 출력

    sleep(100)
