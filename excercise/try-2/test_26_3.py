print("## X, Y 좌표의 사분면 위치 찾기 ##")
x = int(input("X축 좌표를 입력해주세요 : ")); y = int(input("Y축 좌표를 입력해주세요 : "))

if x == 0 and y == 0:
    print("원점이다.")
    ps = 0
elif x < 0 and y > 0:
    ps = 2
elif x < 0 and y < 0:
    ps = 3
elif x > 0 and y > 0:
    ps = 1
elif x > 0 and y < 0:
    ps = 4
    # 1, 4사분면
if ps != 0:
    print(f"{ps}사분면")