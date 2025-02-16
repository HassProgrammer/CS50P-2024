name = input("What's your name:")
# Say hello to user
print("Hello,")
print(name)
#--------------------
print("Hello,", end="")
print(name)
#--------------------
print("Hello,", end="---")
print(name)
#---------Sep-----------
print("Hello,", name, sep="")
#---------Sep-----------
print("Hello,",name, sep="-------")
#--------Remove whitespace------------
name = name.strip()
print(f"***This test for remove whitespace {name}")
#--------Capitalize------------
name =  name.capitalize()
print(name)

#--------Title------------
name  = name.title()
print(name)

# Remove whitespace from str and capitalize user's name
name = name.strip().title()
print(name)    