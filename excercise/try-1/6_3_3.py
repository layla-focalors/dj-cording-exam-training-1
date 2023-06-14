print("<1부터 n까지의 합계 구하기>")
n = int(input("n의 값 입력 : "))
j = 0

for i in range(1, n + 1):
    j += i
print(f"1부터 {n}까지의 합계 = {j}")