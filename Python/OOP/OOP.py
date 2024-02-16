class nahiyan:
    discount = 0.05
    def __init__(self,productName,quan,price):
        self.name = productName
        self.quantity = quan
        self.price = price
        print(f"The product name is {self.name}")
        
        
    def total_price(self):
        #self ---> product1 object--->for this "total = product1.total_price()" 
         return self.quantity*self.price
    def newPrice(self):
        return self.total_price()-self.total_price()*self.discount
product1 = nahiyan("mobile",2,30)
# product1.name = "mobile" # product1.quantity = 2 # product1.price = 30 
product2 = nahiyan("laptop",3,200) 
total = product1.total_price()
print(total) 
total = product2.total_price() 
print(total) # print(product1.name) # print(product1.quantity) # print("----data types----") # print(type(product1)) # print(type(product1.name)) # print(type(product1.quantity)) # -----normal convention---- # product = int(input()) # quantity = input() # print(type(product),type(quantity))
newPrice = total -(total*product2.discount)
print(f"the discount value for product1 is {nahiyan.discount} and the new price is {product1.newPrice()}")
print(f"the discount value for product1 is {nahiyan.discount} and the new price is {product2.newPrice()}")