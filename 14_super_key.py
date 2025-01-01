class a():
    def __init__(self):
        print("A")
    def display(self):
        print("This is class A")

class b():
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("This is class B")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("This is class C")

obj1 = c()