################################# Example 1 ############################################

# try:
#     a = int(input())
#     b = int(input())
#     print(a+b)
# except Exception as e:
#     print("Error",e)

################################# Example 2  types of exception handling ############################################ 

# try:
#     a=int(input())
#     b=int(input())
#     c=input()
#     print(a+b)
#     print(c/a)
# except ValueError as e:
#     print("valueerror",e)
# except TypeError as e:
#     print("typeerror",e)

################################# Example 3  finally ############################################ 

try:
    a=int(input())
    b=int(input())
    c=input()
    print(a+b)
    print(c/a)
except ValueError as e:
    print("valueerror",e)
except TypeError as e:
    print("typeerror",e)

finally :
    print("Done")