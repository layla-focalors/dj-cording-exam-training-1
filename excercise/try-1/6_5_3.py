import random
rand = random.randint(1,2)
print("동전 던지기 게임을 시작합니다.")

if rand == 1:
    print("앞면", end = " ")
else:
    print("뒷면", end = " ")
print("입니다.\n게임이 종료되었습니다.")

