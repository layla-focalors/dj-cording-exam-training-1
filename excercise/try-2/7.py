health = 100

while health > 0:
    health -= int(input(f"주인공의 체력은 {health} 입니다\n얼마의 데미지를 입히시겠습니까 : "))
print("주인공이 죽었습니다.")