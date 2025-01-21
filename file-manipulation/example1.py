# File maninpulation by reading file and write file
file_path = 'test.txt'
key = 'NAME'
value = 'IRFARHAAAN'
with open(file_path, 'r') as file :
    a = file.readlines()
    print(a)
    for i in a:
        print(i)
with open(file_path, 'w') as file:
      for i in a:
        if key in i:
           print(key)
           file.write(key+"="+value+"\n")
        else:
          file.write(i)  