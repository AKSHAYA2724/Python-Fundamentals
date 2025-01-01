class company():
    def __init__(self):
        self.__name ="google"
    def display(self):
        print(self.__name)#encapsulation

c1 = company()
c1.display()

#  _name -> protected
#  __name ->private
#  name -> public