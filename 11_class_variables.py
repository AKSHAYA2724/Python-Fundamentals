class phone():
    chargertype = "B-Type" #class variable
    def __init__(self,brand,price):
        self.brand = brand  #instance variable
        self.price = price  #instance variable
    def display(self):
        print("Brand:" , self.brand)
        print("Price:" , self.price)
        print("chargertype:" , self.chargertype)

phone.chargertype = "C-Type"
poco = phone("poco","10000")
poco.display()

vivo = phone("vivo","20000")
vivo.display()
        