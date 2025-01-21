def login(func):
    print("Hello Irfan!!")
    # func()
    return func

@login
def hello_world():
    print("Hello World!!")

hello_world()    