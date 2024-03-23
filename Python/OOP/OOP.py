import csv


class nahiyan:
    discount = 0.05
    allProducts = []

    def __init__(self, productName, quan, price=0):
        assert price >= 0, f"price {price} is not greater than or equal to zero!"
        self.name = productName
        self.quantity = quan
        self.price = price
        # self.discount
        # print(f"The product name is {self.name}")
        nahiyan.allProducts.append(self)

    def total_price(self):
        # self ---> product1 object--->for this "total = product1.total_price()"
        return self.quantity*self.price

    def newPrice(self):
        return self.total_price()-self.total_price()*self.discount

    def __repr__(self):
        return f"nahiyan({self.name},{self.discount},{self.quantity},{self.price})"

    @classmethod
    def getObj(cls):
        with open('H:/Programming_Learning_Path/Python/OOP/products.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                nahiyan(productName=item.get('name'), quan=item.get(
                    'quantity'), price=int(item.get('price')))

    @staticmethod
    def is_integer(taka):  # 5.0,8.5,1.0,2,4
        if isinstance(taka, float):
            return taka.is_integer()
        elif isinstance(taka, int):
            return True
        else:
            return False

# will implement with class method and CSV file
# product1 = nahiyan("mobile", 2, 30)
# product2 = nahiyan("Laptop", 3, 20)
# product3 = nahiyan("Tablet", 2, 10)
# product4 = nahiyan("Watch", 4, 40)


# product2.discount = 0.1
# product3.discount = 0.3

# print(
#     f"The values of first product is {product1.name} {product1.quantity} {product1.price}")
# print(
#     f"The values of second product is {product2.name} {product2.quantity} {product2.price}")
# print(
#     f"The values of third product is {product3.name} {product3.quantity} {product3.price}")

# total = product1.total_price()
# print(total)
# total = product2.total_price()
# print(total)  # print(product1.name) # print(product1.quantity) # print("----data types----") # print(type(product1)) # print(type(product1.name)) # print(type(product1.quantity)) # -----normal convention---- # product = int(input()) # quantity = input() # print(type(product),type(quantity))
# newPrice = total - (total*product2.discount)
# print(
#     f"the discount value for product1 is {nahiyan.discount} and the new price is {product1.newPrice()}")
# print(
#     f"the discount value for product1 is {product2.discount} and the new price is {product2.newPrice()}")
# print(
#     f"the discount value for product1 is {product3.discount} and the new price is {product3.newPrice()}")
# print(
#     f"the discount value for product1 is {product4.discount} and the new price is {product4.newPrice()}")
# print(dir(product1))
# print(dir(product2))

nahiyan.getObj()  # inplementing class method
# for product in nahiyan.allProducts:
#     print(
#         f"The values of first product is {product.name} {product.quantity} {product.price}")
print("----------")
for product in nahiyan.allProducts:
    print(product)

print(nahiyan.is_integer(7.8))
print(nahiyan.is_integer(5.0))
print(nahiyan.is_integer(1))
