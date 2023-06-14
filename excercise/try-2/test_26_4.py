print("사이다-700원 콜라-800원 물-1200원")
money = int(input("얼마를 입력하시겠습니까 : "))
menu = int(input("선택) 1-사이다 2-콜라 3-물 : "))

if menu == 1:
    if money >= 700:
        money -= 700
        print(f"사이다가 나왔습니다. 덜컹\n잔돈 {money} 원 반환합니다.")
    else:
        print(f"음료수를 뽑을 수 없습니다.\n잔돈 {money}원 반환합니다.")
elif menu == 2:
    if money >= 800:
        money -= 800
        print("콜라가 나왔습니다. 덜컹\n잔돈 {money} 원 반환합니다.")
    else:
        print(f"음료수를 뽑을 수 없습니다.\n잔돈 {money}원 반환합니다.")
elif menu == 3:
    if money >= 1200:
        money -= 1200
        print("물이 나왔습니다. 덜컹\n잔돈 {money} 원 반환합니다.")
    else:
        print(f"음료수를 뽑을 수 없습니다.\n잔돈 {money}원 반환합니다.")