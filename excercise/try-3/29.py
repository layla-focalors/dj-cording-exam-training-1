import random
card = random.randint(1,2)
print("동전 던지기 게임을 시작합니다.")
if card == 1:
    name = "앞"
elif card == 2:
    name = "뒷"
print(f"{name}면입니다.\n게임이 종료되었습니다.")