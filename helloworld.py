answer = 42
pi= 3.14159

int(pi) == 3
float(answer) == 42.0

"Hello world" == 'Hello world' == """Hello world"""

"hello".capitalize() == "HELLO"
"hello".replace("e", "a") == "hallo"
"hello".isalpha() == True
"hello".isdigit() == True


"some, csv, values".split(',') == ["some", "csv", 'values']

name = "Rupam"

machine = "Tensorflow"

"Hello {0} I am {1}".format(name, machine)

f"Hello {name} I am {machine}"