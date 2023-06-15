gender = input("[남], [여] 중 하나를 입력하세요 : ")
if gender == '여':
    print("입영 대상이 아닙니다.")
elif gender == '남':
    age = int(input("현재 나이를 입력하세요 : "))
    if age >= 20:
        print("입대 대상자 입니다.")
    else:
        print("입영 대상이 아닙니다")