python_course = True
java_course = False
int(python_course) == 1
int(java_course) == 0
str(python_course) == "True"

aliens_found = None # this is similar to null, it id different then undefined



number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")

if number:
    print("Number is defined and truthy")

text = "Python"
if text:
    print('Text is defined and truthy')

if number != 5:
    print('This will not  execute')

if not python_course:
    print("This will also not execute")

if number == 5 and python_course:
    print("This code wil execute")

if number == 5 or python_course:
    print("This course will execute")
    
a=1
b=2
"bigger" if a > b else "smaller" 