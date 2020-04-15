class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def firstClass(self):
        if self.gpa > 7:
            return True

        else:
            return False

