print("## X, Y 좌표의 사분면 위치 찾기 ##")
x = int(input("X축 좌표를 입력해주세요 : "))
y = int(input("Y축 좌표를 입력해주세요 : "))
if x > 0 and y > 0:
    level = 1
elif x > 0 and y < 0:
    level = 4
elif x < 0 and y < 0:
    level = 3
elif x < 0 and y > 0:
    level = 2
elif x == 0 and y == 0:
    print("원점이다.")
    level = 0
if level >= 1:
    print(f"{level}사분면")