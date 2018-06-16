student = {
    "name" : "Rupam",
    "student_id": 227704,
    "feedback": None
}
student["last_name"] = "Roy"
try:
    last_name = student["last_name"]
    numbered_last_name = last_name + 3
except KeyError:
    print("error finding last name")
except TypeError as error:
    print(error)
    print("cannot add number with string")
except Exception:
    print("Unknown error")

print("This code executes")