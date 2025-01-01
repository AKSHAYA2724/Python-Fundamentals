class phone():
    chargerType = "C-Type"#class variable
    def __init__(self):
        self.brand =" "
        self.price ="12000"
    def set(self,price):
        self.price =price
    def get(self):#instance method
        print(self.price)
    
    @classmethod
    def changechargerType(cls):
        cls.changechargerType="B-Type"
        print(cls.changechargerType)
    
    @staticmethod
    def info():
        print("This is static class")


poco = phone()
poco.set(20000)
poco.get()
phone.changechargerType()
poco.info()