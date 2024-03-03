class nahiyan:
    discount = 0.05

    def __init__(self, productName, quan, price=0):
        assert price >= 0, f"price {price} is not greater than or equal to zero!"
        self.name = productName
        self.quantity = quan
        self.price = price
        # self.discount
        print(f"The product name is {self.name}")

    def total_price(self):
        # self ---> product1 object--->for this "total = product1.total_price()"
        return self.quantity*self.price

    def newPrice(self):
        return self.total_price()-self.total_price()*self.discount


product1 = nahiyan("mobile", 2, 30)
product2 = nahiyan("Laptop", 3, 20)
product3 = nahiyan("Tablet", 2, 10)
product4 = nahiyan("Watch", 4, 40)
# product3.name = 2
product2.discount = 0.1
product3.discount = 0.3
print(
    f"The values of first product is {product1.name} {product1.quantity} {product1.price}")
print(
    f"The values of second product is {product2.name} {product2.quantity} {product2.price}")
print(
    f"The values of third product is {product3.name} {product3.quantity} {product3.price}")

total = product1.total_price()
print(total)
total = product2.total_price()
print(total)  # print(product1.name) # print(product1.quantity) # print("----data types----") # print(type(product1)) # print(type(product1.name)) # print(type(product1.quantity)) # -----normal convention---- # product = int(input()) # quantity = input() # print(type(product),type(quantity))
# newPrice = total - (total*product2.discount)
print(
    f"the discount value for product1 is {nahiyan.discount} and the new price is {product1.newPrice()}")
print(
    f"the discount value for product1 is {product2.discount} and the new price is {product2.newPrice()}")
print(
    f"the discount value for product1 is {product3.discount} and the new price is {product3.newPrice()}")
print(
    f"the discount value for product1 is {product4.discount} and the new price is {product4.newPrice()}")
# print(dir(product1))
# print(dir(product2))
