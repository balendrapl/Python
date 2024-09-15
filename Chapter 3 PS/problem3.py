string1 = "Baalu is  a good  boy."
print(string1.find("  "))
# if we get -1 then it mean, that thing is not present in given string
#this program gives the index position 
print(string1.replace("  "," "))

#⭐⭐⭐⭐⭐Remember that Strings are inmutable i.e original string jo starting me likh dete h vo vesi hi rehti even after the application of several function or something else
#⭐⭐⭐⭐⭐as when we print it at last we again get the original one without any mutation
print(string1)