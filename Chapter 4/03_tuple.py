a = () # empty tuple
b =(1,) # for single element we have to add coma bcoz without coma it consider it as int datatype
c = (2)
d = (5,35.46,497,False,"Baalu")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
a[0] = 453  #this will give error as just like string, tuple is immutable 