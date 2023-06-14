typer = int(input("홀수는 1, 짝수는 2를 입력해주세요 : "))

for i in range(1, 101):
    if typer == 1 and i % 3 == 0:
        print(i, end = " ")
    elif typer == 2 and i % 2 == 0:
        print(i, end = " ")