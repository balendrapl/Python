name = "Baalu"
print(len(name))
print (name.endswith("alu"))
print (name.startswith("ba")) #Ba

a = "baalu is a very very AWESOME boy. he is good at explaining."
print (name.endswith("ing")) #ing.
print(a.count("a"))
print(a.capitalize()) #to make 1st letter of whole line capital 
#we can also write it as 
capitalized_sting = a.capitalize()
print (capitalized_sting) # and similarly for other string functions
print(a.find("v"))
print(a.replace("a","x"))

print(a.lower()) #Converts all characters to lowercase
print(a.upper()) #Converts all characters to uppercase

b= ["hello","World"]
print(" ".join(b))  #joins elements of a list into a string, separated by a specified separator.

s = "   Hello   world  "
print(s.strip())  # Output: "Hello   world" #Removes any leading and trailing whitespace (or specified characters).

#⭐⭐⭐⭐⭐
name= "Baalu"
age = 18
print("My name is {} and I am {} years old.".format(name,age))
