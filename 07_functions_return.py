# def aksh():
#     print("hello akshaya")

# aksh()

#........................................EXAMPLE 1.............................................

# a = int(input())
# b = int(input())

# def add():
#     print(a+b)
# def sub():
#     print(a-b)
# def mul():
#     print(a*b)
# def div():
#     print(a/b)

# add()
# sub()
# mul()
# div()

#........................................EXAMPLE 2.............................................

# a = int(input())
# def findevenodd(a):
#     if(a%2==0):
#         print("even number")
#     else:
#         print("odd number")

# findevenodd(a)

#........................................EXAMPLE 3.............................................

# def printrange(a,b):
#     for i in range (a,b+1):
#         print(i,end=" ")
# a = int(input())
# b = int(input())
# printrange(a,b)

#........................................EXAMPLE 4.............................................

# def aksh():
#     return "aksh"
# print(aksh())

s_username = "aksh"
s_pass ="2724"
def match():
    a = input("enter name: ")
    b = input("enter password: ")
    if(s_username==a and b==s_pass):
        return True
    else:
        return False

print(match())
