x = 0

while True:
    x += 3
    if x >= 10:
        break
    if x % 2 == 0:
        continue
    print(x, end=' ')