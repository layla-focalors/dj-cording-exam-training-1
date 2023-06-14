tp = 0
while True:
    ket = int(input("숫자를 입력하시오 : "))
    tp += ket
    continue_ = input("계속?(yes/no) : ")
    if continue_ == "no":
        break
    elif continue_ == "yes":
        pass

print(f"합계는 : {tp}")