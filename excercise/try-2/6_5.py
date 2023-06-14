product_price = int(input("상품의 가격 : "))
if product_price > 20000:
    price = 0
else:
    price = 3000

print(f"배송비 = {price}")