class Order:

    def __init__(self,item , price):
        self.item = item 
        self.price = price

    def __gt__(self,s2):
        return self.price > s2.price

s1=Order("chips",20)
s2=Order("Cola",40)

print(s1>s2)
        