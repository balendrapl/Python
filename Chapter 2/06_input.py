#1
a = input("Enter number 1 : ") #iss input se number ni string milega
b = input("Enter number 2 : ")

print("Number a i: ",a)
print("Number b i: ",b)
print("Sum is : ",a+b)  #jab bhi input me koi bhi string hoti h & if we add those strings by using '+' sign then instead of addition they just concatinate i.e combine
                        # e.g "Baalu" + "Great" ---> 'BaaluGreat'. Similarly, "53" + "29" ----> '5329' 

#2
a = int(input("Enter number 1 : ")) # actually yaha pr hamne type casting ka use karke string ko int me change kar diya
b = int(input("Enter number 2 : "))

print("Number a i: ",a)
print("Number b i: ",b)
print("Sum is : ",a+b)