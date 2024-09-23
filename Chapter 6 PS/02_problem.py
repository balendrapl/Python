m1 = int(input("Enter your marks in Physics: "))
m2 = int(input("Enter your marks in Maths: "))
m3 = int(input("Enter your marks in Chemistry : "))
total_percentage = (m1+m2+m3)/3
if(m1>100 or m1<0 or m2>100 or m2<0 or m3>100 or m3<0):
    print("Invalid number")
elif(m1>=33 and m2>=33 and m3>=33 and total_percentage >=40):
    print('''You are passed!
    Your percentage = ''',total_percentage)
else:
    print('''You are failed!
    Your percentage = ''',total_percentage)
