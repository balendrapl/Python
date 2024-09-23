a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))
c = int(input("Enter the number3: "))
d = int(input("Enter the number4: "))

#my method
# if (a>b):
#     if(a>c):
#         if(a>d):
#             print(f"{a} is the greatest number")
#         else:
#             print(f"{d} is the greatest number")
#     else:
#         if(c>d):
#             print(f"{c} is the greatest number")
#         else:
#             print(f"{d} is the greatest number")

# else:
#     if(b>c):
#         if(b>d):
#             print(f"{b} is the greatest number")
#         else:
#             print(f"{d} is the greatest number")
#     else:
#         if(c>d):
#             print(f"{c} is the greatest number")
#         else:
#             print(f"{d} is the greatest number")

if(a>b and a>c and a>d):
    print("Greatest no. is", a)
elif(b>a and b>c and b>d):
    print("Greatest no. is", b)
elif(c>b and c>a and c>d):
    print("Greatest no. is", c)
elif(d>b and d>c and d>a):           
    print("Greatest no. is", d)
#instead of these above 2 lines we can also write 
# else:
#     print("Greatest no. is",d)




#to find greatest no. in a list
# m = []
# n1 = int(input("Enter the number1: "))
# m.append(n1)
# n2 = int(input("Enter the number2: "))
# m.append(n2)
# n3 = int(input("Enter the number3: "))
# m.append(n3)
# n4 = int(input("Enter the number4: "))
# m.append(n4)
# maxi = m[0]
# if i in range[1,4]:         # incomplete
         