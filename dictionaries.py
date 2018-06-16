# in python what is called an object in javascript is called a dictionary
# this is a typical dictionary
student = {
    "name" : "Rupam",
    "student_id": 227704,
    "feedback": None
}

# has keys and values
# values can be of any types, there is no concept of typed dictionary in python

all_students = [{...}, {...}, {...}] # list of dictionary

#fetch a dictionary value
student['name'] == 'Rupam'
student['last_name'] == KeyError # If key is not existent it results in a key error
# to prevent KeyError
student.get('last_name', 'Unknown') == 'Unknown'

# to get all the keys in a dictionary

student.keys() == ["name", "student_id", "feedback"]
student.values() == ["Rupam", 227707, None]

# to set a value
student['name'] = "James"

# to delete a key value
del student["name"]