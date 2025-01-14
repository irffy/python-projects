name = "Irfan Ahmed"
print(f"Full String: {name}")
str = name.split(" ")
print("FirstName is:", str[0])
print(f"FirstName uppercase:",str[0].upper())
print("Length of FirstName:", len(str[0]))

str1 = "Arhaan"
str2 = "Ibrahim"
fullname = str1+" "+str2
print("Full name:", fullname)
newname = fullname.replace("Arhaan", "Irfan")
print("Replaced new name", newname)
text = "___Some spaces around___"
stripped_text = text.strip("_")
print("Stripped text:", stripped_text)
