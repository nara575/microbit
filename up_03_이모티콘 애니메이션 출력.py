from microbit import *

clock1 = Image(
                "99999:"  # 픽셀 정보를 0에서 9의 값으로 표현할 때, 9는 가장 밝게 켜진 상태이고 0은 꺼진 상태
                "09090:"
                "00900:"
                "09090:"
                "99999")

clock2 = Image("99999:" "05050:" "00900:" "09090:" "99999")  # 픽셀 정보에서 5의 값은 중간 밝기

clock3 = Image("99999:" "09090:" "00500:" "09090:" "99999")

clock4 = Image("99999:" "09090:" "00900:" "05050:" "99999")

sand_clock = [clock1, clock2, clock3, clock4]
display.show(sand_clock, loop=True, delay=200)
