###################################### single inheritance #################################################

# class kookie():
#     def breakie(self):
#         print("This is kookie's class")

# class aksh(kookie):
#     def purple(self):
#         print("This is aksh's class")

# hey = aksh()
# hey.purple()
# hey.breakie()

###################################### Multiple inheritance #################################################

# class dad():
#     def phone(self):
#         print("dad phone")

# class mom():
#     def sweet(self):
#         print("mom sweet")

# class son(dad,mom):
#     def purple(self):
#         print("son class")

# hey = son()
# hey.phone()
# hey.sweet()

###################################### Multilevel inheritance #################################################

# class grandpa():
#     def phone(self):
#         print("Grandpa Phone")

# class dad(grandpa):
#     def money(self):
#         print("dad money")

# class son(dad):
#     def laptop(self):
#         print("son class")

# ak = son()
# ak.money()
# ak.phone()

###################################### Hierachy inheritance #################################################

class dad():
    def money(self):
        print("Dad Money")
class son1(dad):
    pass  #empty class
class son2(dad):
    pass
class son3(dad):
    pass

s2 = son2()
s2.money()

###################################### Hybird inheritance #################################################
class dad():
    def money(self):
        print("Dad Money")
class land():
    def imp(self):
        print("Important land")
class son1(dad,land):
    pass  #empty class
class son2(dad):
    pass
class son3(dad):
    pass

s2 = son2()
s2.money()
s1=son1()
s1.imp()

