marks = {
    "Baalu" : 100,
    "Shayam" : 85,
    "Rohan" : 49
}
print(marks["Rohan"])

# Why was the need of Dictionary in Python
# Suppose we have marks of 10000 students & we want to search for a studuent marks
# then in such case Dictionary looks up almost all its elements at once & throw out our required thing 
# Even though we can do so in list by making ⭐"list of list"⭐ as well but its syntax will be little bit complex & slower
#mark = [ ["Baalu",100],["Rohan",49]]
#print(mark["Baalu"])    #error dont know why