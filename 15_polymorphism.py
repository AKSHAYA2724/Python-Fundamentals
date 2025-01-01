# def add(a,b,c=0):
#     print(a+b+c)

# add(1,2)
# add(1,2,3)

class animal():
    def sound(self):
        print("Animal makes a sound")

class dog(animal):
    def sound(self):
        print("Dog barks")

class bird(animal):
    def sound(self):#override
        print("Birds sing")

b = bird()
b.sound()