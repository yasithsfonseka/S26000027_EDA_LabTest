students = ("Alice", "Bob", "Charlie", "David", "Eve")
print(students[0])  # Output: Alice
print(students[2])  # Output: Charlie

print("Total Number of Students :", len(students))  # Output: Total Number of Students : 5
print("First Three Students :", students[:3])  # Output: First Three Students : ('Alice', 'Bob', 'Charlie') 
print("Last Two Students :", students[-2:])  # Output: Last Two Students : ('David', 'Eve') 
#students[0] = "Alex"  # This will raise a TypeError because tuples are immutable
print("Last Student :", students[-1])  # Output: Last Student : Eve
print(students)  # Output: ('Alice', 'Bob', 'Charlie', 'David', 'Eve')