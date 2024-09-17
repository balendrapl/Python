friends = ["Apple","Baalu", 5, 865.53, False, "Mango"]
print(friends[0])

friends.append("Baalu the Great") #append is insertion function which helps in inserting something at the end of lists
print(friends)

l1 = [9,8,6,65,32]
#l1.sort()
#l1.reverse()
l1.insert(2,342425) # insert 342425 such that itsindex in the list is 2
print(l1)

print(l1.pop(3)) #instead of this line we can also use these 2 below lines
print(l1)

value = l1.pop(3) #line1
print (value)     #line2
print(l1)

l1.remove(32)
print(l1)