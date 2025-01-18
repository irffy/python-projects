import os

folders_list = input("Enter folders list:").split()
# print(folders_list)

for i in folders_list:
    try:
        list_dir = os.listdir(i)
        print(f"*******List of directories under {i} are:*******")
        # print(os.listdir(i))
        for i in list_dir:
            print(i)
    except FileNotFoundError:
        print("Dir not found:")        