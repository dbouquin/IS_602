# Class review:
# A class is a "blue print for an object and an object is an instance of a class"
# One class (specify how it works and what types of variables are a part of it) can be used to
# create many objects - e.g. metadata
# Inside class we define methods - methods are specific to a class. Object is passed inside a method
# Method helps us get all information inside an object
# First write a "constructor" - TWO underscores before and after
# member variables - variables that are related to a specific class

# Example of creating a class:
class Student (object):
    def __init__(self, name, grade, grade_level):
        self.name = name # input parameter 'name' is asigned to a member variable (inside the class) called 'name'
        self.grade = grade
        self.grade_level = grade_level

        # Try creating some different methods for the object
    def describe(self):
        print "My name is", self.name, ". My grade is", self.grade_level, "."

    def has_A(self): #does the student have an A?
        if self.grade == "A":
            return "Yes"
        else:
            return "No"

    def set_grade(self, grade): #change grade once it's been set_grade
        self.grade = grade
        print "Grade changed"

# Example of creating an object from the class:
student1 = Student("Bob", "F", 12)
student1.describe()
print "Has A?", student1.has_A()
student1.set_grade("A")
print "Has A?", student1.has_A()

student2 = Student("Laura", "A", 10)
student2.describe()
print "Has A?", student2.has_A()
student2.set_grade("C")
print "Has A?", student2.has_A()
