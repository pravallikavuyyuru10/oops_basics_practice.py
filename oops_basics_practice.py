class Student:
    college = "ABC College"#Class Variable

    def __init__(self, name, age, course):
        self.name = name #Instance Variable
        self.age = age
        self.course = course
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("College:", Student.college)

student1 = Student("Pravallika", 20, "CSE")
student2 = Student("Rahul", 21, "ECE")

student1.display()
student2.display()
    
