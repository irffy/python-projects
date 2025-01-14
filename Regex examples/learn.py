import re

text = "apple,banana,orange,grape"
print(text)
split_text = text.split(",")
print(split_text)

pattern = r","
split_text1 = re.split(pattern,text)
print(split_text1)

for item in split_text1:
    print(item)

for i in range(len(split_text1)):
    print(split_text1[i])    
    # print(i)

#####################################################
text1 = "The quick brown fox"
pattern1 = "red"

result = re.search(pattern1,text1)
# print(result)
if result:
    print("Pattern found")
else:
    print("String not found")    
