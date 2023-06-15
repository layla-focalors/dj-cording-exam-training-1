import random
print(f"주사위 프로그램을 시작합니다. 첫 번째 숫자는\n{random.randint(1,6)}")

while True:
    key = input("아무키나 누르면 주사위가 던져집니다. 종료를 원하시면 'q'를 입력해주세요.")
    if key == 'q':
        break
    else:
        print(random.randint(1,6))
