import random

random_count = random.randint(10, 20)

while True:
    usr_input = int(input("숫자 입력(10~20) : "))
    if usr_input > random_count:
        print("숫자보다 큽니다. 다시 입력하세요")
    elif usr_input < random_count:
        print("숫자보다 작습니다. 다시 입력하세요")
    elif usr_input == random_count:
        break
print("정답입니다.")