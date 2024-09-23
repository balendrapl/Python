
post = input("Enter the post: ")

#1st method
if("Harry" in post):
    print ("Yes, this post is talking about “Harry”")
else:
    print("This post is not talking about “Harry”")


#but if we write its other forms like haRry, HarrY, harry, HARRY, etc. then it will not detect it in the above method
#2nd ⭐⭐⭐⭐⭐
if("Harry".lower() in post.lower()):
    print ("Yes, this post is talking about “Harry”")
else:
    print("This post is not talking about “Harry”")

# "Harry".lower() in post.lower() --> it mean that lowercase wala Harry (i.e. harry) agar post me h & sirf post me hi ni balki uss post ko lowercase me karne ke baad bhi h 
# then print that "Yes, this post is talking about “Harry”"