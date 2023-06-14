import random
random_number = random.randint(1, 100)

while True:
    prediction_number = int(input("예상 숫자를 입력하세요 : "))
    if prediction_number < random_number:
        print("UP")
    elif prediction_number > random_number:
        print("DOWN")
    else:
        break
print("정답")