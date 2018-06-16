
# looping using a for loop
students = ["Rupam", "Rishabh", "Ridansh"]
for name in students:
    print("Student name is {0}".format(name))

# the normal for loop is done on python using a ramge
for index in range(10):
    x+=10
    print("The value of X is {0}".format(x))

# range(start, stop, [step])

# break
for name in students:
    if name == "Rishabh":
        print("!Found" + Rishabh)
        break
    print("currently testing " + name)
# the above code will ptint till Rishabh

#continue
for name in students:
    if name == "Rishabh":
        continue
    print("currently testing " + name)
# the above code will print all names but Rishabh