from microbit import * # 마이크로비트 모듈의 모든 명령 사용

while True:     # 무한 반복
    pin0.write_digital(1)   # 0번핀에 연결된 빨간색 LED 켜기(켜기:1, 끄기: 0)
    sleep(3000)             # 3초 지연
    pin0.write_digital(0)   # 0번핀에 연결된 빨간색 LED 끄기
    pin1.write_digital(1)   # 1번핀에 연결된 녹색 LED 켜기
    for a in range(6):      # a값이 0에서 5까지 총 6회 반복하기
        display.show(5-a)   # 25개 LED 디스플레이에 5초 카운팅 보여 주기
        sleep(1000)         # 1초 지연
    pin1.write_digital(0)   # 1번핀에 연결된 녹색 LED 끄기
    pin0.write_digital(1)   # 노란색을 만들기 위해 0번핀에 연결된 빨간색 LED 켜기
    pin1.write_digital(1)   # 노란색을 만들기 위해 1번핀에 연결된 녹색 LED 켜기
    display.clear()         # 25개 LED 디스플레이 초기화
    sleep(2000)             # 2초 지연
    pin0.write_digital(0)   # 0번핀에 연결된 빨간색 LED 끄기
    pin1.write_digital(0)   # 1번핀에 연결된 녹색 LED 끄기
