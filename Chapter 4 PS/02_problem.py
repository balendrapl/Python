marks = []

studMark = input ("Enter student1 marks: ")
marks.append(studMark)
studMark = input ("Enter student2 marks: ")
marks.append(studMark)
studMark = input ("Enter student3 marks: ")
marks.append(studMark)
studMark = input ("Enter student4 marks: ")
marks.append(studMark)
studMark = input ("Enter student5 marks: ")
marks.append(studMark)
studMark = input ("Enter student6 marks: ")
marks.append(studMark)

marks.sort()
print (marks)

#Note - if the marks do not sort in ascending order then change the data type of input by putting int before it i.e int(input("  ")) 