#need to calculate price
#need to create products
#need to calculate taxes
#need to calculate commission

FABRIC_PRICE = 30.00
ACCESSORY_PRICE = 20.00
SHOE_PRICE = 15.00

TAX = 13
COMMISSION = 10

fabrics = int(input("How many fabrics do you want?: "))
fabrics_price = fabrics * FABRIC_PRICE
accessories = int(input("How many accessories do you want: "))
accessories_price = accessories * ACCESSORY_PRICE
shoes = int(input("How many pairs of shoes do you want: "))
shoes_price = shoes * SHOE_PRICE

total = fabrics_price + accessories_price + shoes_price
price = total + (total * (TAX/100))

commission = price * (COMMISSION/100)

#print outs
print("The price of your fabrics is: $" + str(fabrics_price))
print("The price of your accessories is: $" + str(accessories_price))
print("The price of your shoes is: $" + str(shoes_price))
print("The total price is: $" + str(total))
print("The price with taxes is: $" + str(price))
print("Your sales rep will get this much commission: $" + str(commission))
