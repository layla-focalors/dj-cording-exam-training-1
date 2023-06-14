import random

random_count = random.randint(10, 20)
usr_input = 0

while random_count != usr_input:
    usr_input = int(input("숫자 입력(10~20) : "))
    if usr_input < random_count:
        print("정답보다 작습니다. 다시 입력하세요.")
    elif usr_input > random_count:
        print("정답보다 큽니다. 다시 입력하세요. ")
    else:
        break
print("정답입니다.")