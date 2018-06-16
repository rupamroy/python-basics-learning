# Define a list
student_names = []

# define iwth members
student_names = ["Mark", "Rupam", "Debapam"]

# Getting List elements
student_names[0] == "Mark"
student_names[1] == "Rupam"

# Getting the last element in a list
student_names[-1] == "Debapam"

# replacing in a list
student_names[0] = "Jessy"

# add to the end
student_names.append("Homer")

# find if an element is thete in the list
"Rupam" in student_names == True

# Length of a list
len(student_names) == 4

# You can have multiple types in any list, though it is not recommended

# delete a list element
del student_names[2] 

# List slicing
students = ["Rupam", "Rishabh", "Ridansh"]
students[1:] == ["Rishabh", "Ridansh"]
students[1:-1] == ["Rishabh"]

