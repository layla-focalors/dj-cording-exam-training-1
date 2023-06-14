import random

random_number = random.randint(10, 20)
answer = "1"

while answer != random_number:
    answer = int(input("숫자 입력(10~20) : "))
    if answer > random_number:
        print("숫자보다 큽니다.")
    elif answer < random_number:
        print("정답보다 작습니다.")
print("정답입니다.")