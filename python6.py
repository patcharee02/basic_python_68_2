"""
#
# Part: Functions
# 
"""
def myFullname(firstname="Unknown", lastname="Forger"):
    Fullname = firstname + " " + lastname
    return Fullname

print(myFullname("Loid", "Forger"))
print(myFullname("Yor", "Forger"))
print(myFullname("Anya", "Forger"))
print(myFullname("Bond", "Forger"))

def redPotion(hp):
    hp += 50
    return hp

currentHP = 100
print("Current HP:", currentHP)
currentHP = redPotion(currentHP)
print("After using Red Potion, HP:", currentHP)
    