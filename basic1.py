product_name1 = "sugar"
product_name2 = "egg"


quan1 = 3
quan2 = 4

price1 = 40
price2 = 6

total_price1 = quan1 * price1
total_price2 = quan2 * price2

discount = 6

total = total_price1 + total_price2

total_after_discount = total - (total*discount)/100

print(total)
print(total_after_discount)


