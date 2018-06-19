class HighSchoolStudent(Student):
    school_name="Durant High school"

    # this is an overidden function
    def get_school_name(self):
        return "This is a high school"

    # overriden function calling the base class function
    def get_name_capitalize(self):
        return super().get_name_capitalize() + '-HS'
