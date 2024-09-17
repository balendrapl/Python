# ⭐⭐⭐⭐⭐ 
s = set()
s.add(20)
s.add(20.0)
s.add('20') 
print(len(s))
# length of s after these operations is 2 instead of 3 bcoz
# in python, on comparision of int & float datatype, if they are numerically equal then they are consider one value
a= 1 == 1.0
b = 1.5 == "1.5"
print(a,b)