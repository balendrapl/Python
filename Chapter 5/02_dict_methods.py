d = {} #empty dictionary
marks = {
    "Baalu" : 100,
    "Shayam" : 85,
    "Rohan" : 49,
    32 : "Aman"   # ese bhi likh sakte h but here key=32 & value= 'Aman'
}
print (marks.items())
print (marks.keys())
#print (marks.values())
print (marks.get(32))

marks.update({"Shayam": 89, "Kallu":81})
print (marks)

print(marks.get("Baalu"))
print(marks["Baalu"])
# though above 2 prints will give same result but they are not same bcoz

print(marks.get("Baalu2")) #prints none        #as key doesn't exist in dictionary
print(marks["Baalu2"])     #returns an error   #as key doesn't exist in dictionary


