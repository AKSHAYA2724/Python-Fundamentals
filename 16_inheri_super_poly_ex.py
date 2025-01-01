#........................................EXAMPLE 1.............................................

# class shape():
#     def area(self):
#         return 0
# class rectangle(shape):
#     def area(self,a,b):
#         c = a*b
#         print(c)

# r = rectangle()
# r.area(2,3)

#........................................EXAMPLE 2.............................................

# class person():
#     def __init__(self,name):
#        self.n = name 
    
# class student(person):
#     def __init__(self,name, grade):
#         super().__init__(name)
#         self.g = grade
#     def display(self):
#         print(self.n,self.g)
        
# s1 = student("aksh","A")
# s1.display()

#........................................EXAMPLE 3.............................................

# class vehicle():
#     def start(self):
#         print("vechile started")
# class car(vehicle):
#     def start(self):
#         print("car started")

# c = car()
# c.start()

#........................................EXAMPLE 3.............................................

class employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class manager(employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.dept = department
    def display(self):
        print(self.name,self.salary,self.dept)
        
m1 = manager("aksh","21","IT")
m1.display()

        