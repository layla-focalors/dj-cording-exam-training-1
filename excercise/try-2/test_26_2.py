sexual = input("[남], [여] 중 하나를 입력하세요 : ")
tesn = 0
if sexual == "여":
    tesn = 1
else:
    age = int(input("현재 나이를 입력하세요 : "))
    if age >= 20:
        print("입대 대상자입니다.")
    else:
        tesn = 1
if tesn == 1:
    print("입영 대상이 아닙니다.")