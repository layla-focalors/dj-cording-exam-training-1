import random

random_key = random.randint(1, 100)
usr_input = 0

while usr_input != random_key:
    usr_input = int(input("예상 숫자를 입력하세요 : "))
    if usr_input > random_key:
        print("DOWN")
    elif usr_input < random_key:
        print("UP")
print(" 정답")