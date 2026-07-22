#Function-default argument

def apply_discount(price, discount=10):
    return price- (price*discount/100)
print(apply_discount(100))
print(apply_discount(100, 25)) #25 is the discount argument