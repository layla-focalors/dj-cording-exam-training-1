count = 0
while True:
    count += int(input("숫자를 입력하시오 : "))
    continue_ = input("계속?(yes/no) : ")
    if continue_== 'yes':
        continue
    elif continue_ == 'no':
        break
    else:
        print("잘못된 입력입니다.")
print(f"합계는 : {count}")