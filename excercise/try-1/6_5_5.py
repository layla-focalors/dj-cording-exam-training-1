user_input = "yes"; total = 0

while user_input == "yes":
    count = int(input("숫자를 입력하시오 : "))
    total += count
    user_input = input("계속? yes/no) : ")

print(f"합계는 : {total}")