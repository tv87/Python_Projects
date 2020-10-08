# User defined classes
# Question 1
# Part A
class Section:
    def __init__(self, section_id):
        self.section_id = section_id # CS 100_006
        self.enrolled_students = []

    def enroll(self, studentName):
        self.enrolled_students.append(studentName)

    def is_enrolled(self, studentName):
        if studentName in self.enrolled_students:
            return True
        else:
            return False

# Part B
import section
section1 = section.Section("Math111_101")
section1.enroll("Joe Joesephson")
section1.enroll("Mary Smith")
print(section1.is_enrolled("Mary Josephson"))

# Quesstion 2
class State:
    def __init__(self, name):
        self.name = name
        self.universities = []

    def addUniversity(self, universityName):
        self.universities.append(universityName)

    def is_home_of(self, universityName):
        if universityName in self.universities:
            return True
        else:
            return False

import state
mystate = state.State("NJ")
mystate.addUniversity("NJIT")
mystate.addUniversity("Princeton")
print(mystate.is_home_of("MIT"))
    
    
