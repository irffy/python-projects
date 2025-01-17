#for loops

# for i in range(3):
#     print("Irfan")

print("******************")
list = ["a","b","c",1,2]    
for j in list:
    print(j)

print("******************")
for j in list:
    if j == "c":
        break
    print(j)    

print("******************")
for j in list:
    if j == "c":
        continue
    print(j)    
print("******************")
count = 0
while count<5:
    print(count)
    count+=1