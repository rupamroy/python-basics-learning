students = []
# example of a simple class with a method
class Student:
    #class or static attribute
    school_name = "Abbots creek elementary"

    # self is an argument which is always passed and need not be passed explicitly
    # it is a reference to the class instance
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)
    
    def  __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

class HigSchoolStudent(Student):
    school_name="Durant High school"

    # this is an overidden function
    def get_school_name(self):
        return "This is a high school"

    # overriden function calling the base class function
    def get_name_capitalize(self):
        return super().get_name_capitalize() + '-HS'

james = HigSchoolStudent("james")
print(james.get_name_capitalize())
print(james.get_school_name())
print(james.get_name_capitalize())