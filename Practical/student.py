class Students:
    def __init__(self, name, id, marks):
        self.name = name
        self.id = id
        self.marks = marks
    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}")
    def total_marks(self):
        total = sum(self.marks)
        print(f"Total Marks: {total}")
    def average_marks(self, marks):
        return self.total_marks / len(self.marks)
s = Students("Alice", 12345, [85, 90, 78])
s.display_info()
s.total_marks()