import os

f = open("drivers.txt", "r")
drivers = f.read().split("\n")
f.close()

f = open("helpers.txt", "r")
helpers = f.read().split("\n")
f.close()

print(drivers)
print(helpers)
