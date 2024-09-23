age = int(input("Enter your age: "))

# if (age>=18 and age<100):
#     print("You are above the age of consent")
# elif (age<0):
#     print("Bhai kisi ki negative age na hoti h")
# else :
#     print("You are below the age of consent")

#better one
if (age>100):
    print("Bhai, aaj kal kisi ki age 100 se jada na ho paati")
elif (age>=18):
    print("You are above the age of consent")
elif (age<0):
    print("Bhai, kisi ki negative age na hoti h")
elif (age==0):
    print("0 is not a valid age")
else :
    print("You are below the age of consent")

print("End of program")