"""Aung Zay Ya@Edy """
name= input("enter name")
#error check for the name to blank
while len(name)<=1:
    name=input ("Enter the name")

print (name[::2])
