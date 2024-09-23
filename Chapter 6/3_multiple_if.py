age = int(input("Enter your age: "))

#if statement no.1
if (age%2 == 0):
    print("Age is even")
# end of if statement no.1

#if statement no.2
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
# end of if statement no.2

print("End of program")