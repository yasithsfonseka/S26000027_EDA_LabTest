class Person:
    def __init__(self, name):
        self.name = name
        self.age = None

    def greet(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the parent class constructor
        self.subject = subject

    def greet(self):
        super().greet()  # Call the parent class greet method
        print("Subject:", self.subject)   


t = Teacher("Alice", "Mathematics")
t.greet()