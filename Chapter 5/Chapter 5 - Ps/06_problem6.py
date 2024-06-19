# Creat an empty dictionary. Allow 4 friends to enter their favourite languages as value and use key as their names. Assume that the names are unique.

d = {}

name = input("Enater the friend name: ")
lang = input("Enter the language name: ")
d.update({name: lang})
name = input("Enater the friend name: ")
lang = input("Enter the language name: ")
d.update({name: lang})
name = input("Enater the friend name: ")
lang = input("Enter the language name: ")
d.update({name: lang})
name = input("Enater the friend name: ")
lang = input("Enter the language name: ")
d.update({name: lang})

print(d)
