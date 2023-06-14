address = input("배송지(현재는 korea와 us만 가능) : ")
product_price = int(input("상품의 가격 : "))
if address == "korea":
    if product_price >= 20000:
        trip = 0
    else:
        trip = 3000
elif address == "us":
    if product_price >= 100000:
        trip = 0
    else:
        trip = 8000
print(f"배송비 = {trip}")
