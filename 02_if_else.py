#........................................EXAMPLE 1.............................................

# if(False):
#     print("yes")
# else:
#     print("no")

#........................................EXAMPLE 2.............................................

# mark = int(input('enter mark:'))
# if(mark>=35):
#     print("pass")
# else:
#     print("fail")

#........................................EXAMPLE 3.............................................

# income = int (input())
# if(income>7000):
#     print("Not eligible for schorship")
# else:
#     print("Schorship is available ")

#........................................EXAMPLE 4.............................................

# num = int(input("enter number:"))
# if(num%2==0):
#     print("number is even")
# else :
#      print("number is odd")

#........................................EXAMPLE 5.............................................

# score = int (input("enter score"))
# if(score>70):
#     print("good student")
# elif(score<=70 and score>35):
#     print("average student")
# else:
#     print("poor student")

#........................................EXAMPLE 6.............................................

# a = int(input())
# b = int(input())
# cal = input()
# if(cal == 'add'):
#     print(a+b)
# elif(cal == 'sub'):
#     print(a-b)
# elif(cal == 'mul'):
#     print(a*b)
# elif(cal =='div'):
#     print(a/b)
# else:
#     print("invalid operation")

#........................................EXAMPLE 7.............................................

# salary = int(input("salary:"))
# age = int(input("age:"))
# if(salary>=20000 or age<=25):
#     loan = int(input('loan:'))
#     if(loan>50000):
#         print("maximum loan amount is 50000")
#     else:
#         print("you are eligible")
# else:
#     print("you are not eligible")

#........................................EXAMPLE 8.............................................

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
total = a+b+c+d+e
avg = total/5
if(avg<=35):
    print("Additional class is required")
else:
    print("you are good to go")