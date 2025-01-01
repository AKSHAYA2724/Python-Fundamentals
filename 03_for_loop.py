#........................................EXAMPLE 1.............................................

# for i in "apple":
#     print(i)

# for i in range(1,11):
#     val = i*2
#     print(i," x 2 =",val)

#........................................EXAMPLE 2.............................................

# a = int(input('enter num1:'))
# b = int(input('enter num2:'))
# for i in range(a+1,b):
#     print(i)

#........................................EXAMPLE 3.............................................

# a = int(input('enter num1:'))
# b = int(input('enter num2:'))
# even =0
# odd =0
# for i in range(a,b+1):
#     if(i%2!=0):
#      odd=odd+1
#     else:
#        even = even+1
# print("odd",odd)
# print("even",even)

#........................................EXAMPLE 4.............................................

# count =0
# for i in range(1,100+1):
#     if(i%3==0 and i%5==0):
#         count = count+1
# print(count)

# sum =0
# for i in range(1,6):
#     sum = sum + i
# print(sum)

#........................................EXAMPLE 5.............................................

a=[]
for i in range(1,11):
    b = int(input())
    a.append(b)
sum1 =0
avg =0
for i in a:
    sum1 = sum1 + i
avg = sum1/10
print(avg)