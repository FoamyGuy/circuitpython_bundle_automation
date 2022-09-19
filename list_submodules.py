import os

drivers = os.listdir("libraries/drivers/")
helpers = os.listdir("libraries/helpers/")

drivers.sort()
helpers.sort()

f = open("drivers.txt", 'w')
for submodule in drivers:
    f.write("{}\n".format(submodule))
f.close()

f = open("helpers.txt", 'w')
for submodule in helpers:
    f.write("{}\n".format(submodule))
f.close()
