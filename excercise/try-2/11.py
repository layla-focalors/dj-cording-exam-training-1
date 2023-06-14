import random
keychain = random.randint(1, 100)

while True:
    predict = int(input("예상 숫자를 입력하세요 : "))
    if predict > keychain:
        print("DOWN")
    elif predict < keychain:
        print("UP")
    elif predict == keychain:
        break
print("정답")