#........................................EXAMPLE 1.............................................

# class student:
#     def __init__(self):
#         self.name =" "
#         self.reg_no=" "
#     def display(self):
#         print("Name:",self.name)
#         print("Register Number:",self.reg_no)

# s1 = student()
# s1.name = "kookie"
# s1.reg_no="21650"
# s1.display()

#........................................EXAMPLE 2.............................................

# class fruit:
#     def __init__(self,col):
#         self.color=col

# bts = fruit("Purple")
# print(bts.color)

#........................................EXAMPLE 3.............................................

# class teacher:
#     def __init__(self,n1,r1):
#         self.name = n1
#         self.reg = r1
#     def display(self):
#         print("Name:",self.name)
#         print("Register Number:",self.reg)

# t1 = teacher("Aksh","1")
# t2 = teacher("Saaba","2")
# t1.display()
# t2.display()

#........................................EXAMPLE 4.............................................

class calculator:
    
    def __init__(self,a,b):
        self.val1 = a
        self.val2 = b
        self.c =""
    def add(self):
        self.c = self.val1+self.val2
        print("Addition value:",self.c)
    def sub(self):
        self.c = self.val1-self.val2
        print("Subtraction value:",self.c)
    def mul(self):
        self.c = self.val1*self.val2
        print("Multiplication value:",self.c)
    def div(self):
        self.c = self.val1/self.val2
        print("Division value:",self.c)

all = calculator(10,3)
all.add()
all.sub()
all.mul()
all.div()