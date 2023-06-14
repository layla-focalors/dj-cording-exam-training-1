price = int(input("가격을 입력하시오 : "))
card_type = input("카드 종류를 입력하시오 : ")
if price > 20000 and card_type == "python":
    prio = 0
else:
    prio = 3000
print(f"배송료는 {prio}원 입니다. ")