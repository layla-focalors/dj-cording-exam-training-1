product_price = int(input("상품의 가격 : "))
card_type = input("카드 종류를 입력하시오 : ")

if product_price <= 20000 and card_type == "python":
    print("배송료가 없습니다.")
else:
    print("배송료는 3000원입니다.")