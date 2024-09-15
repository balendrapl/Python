#my method
name = ("Baalu")
date = ("13Sept. 2024 ") 
print(f"Dear {name},\n\tYou are selected!\n\t{date} ")

#better method
letter = '''Dear <|Name|>,
        You are selected!
        <|Date|> '''
print (letter.replace("<|Name|>","Baalu").replace("<|Date|>","13 Sept. 2024"))
#this is called ⭐chaining of a function (replace)
#its actuall mean is that jis string me name ko replace kiya h usi replaced string me hi ek aur replace kardo i.e date ko bhi