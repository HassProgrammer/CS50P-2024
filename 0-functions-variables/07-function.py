def hello(to):
    print("Hello,", to)
name = input("What's your name?:")
hello(name)

#Default arguments--------
def hello(to = "World"):
    print("Hello,", to)
hello()
name = input("What's your name?:")
hello(name)