name = "Baalu"
shortname = name[0:3]
print(shortname)
shortname = name[1:5]

print(shortname)
character1 = name[0]
print(character1)

print(name[-4:-1])
print(name[-4:0]) # it will give nothing but a blank line bcoz negative index me 0 is not present
# we should note that negative index me last character ko print karne ke liye use below line syntax
print(name[-4:])
#colon ke aage ya piche empty rakhne se extreme length ko consider kiya jata h
print(name[:])
print(name[:3])