students = {
    "S001":{"Name": "Alice", "marks": [85, 90, 78]},
    "S002":{"Name": "Bob", "marks": [92, 88, 95]},
    "S003":{"Name": "Charlie", "marks": [78, 82, 80]},
}

total_marks = 0
for student_id, student_info in students.items():
    marks = student_info["marks"]
    total_marks += sum(marks)

for sid, info in students.items():
    marks = info["marks"]
    total_marks += sum(marks)
    avg = sum(marks) / len(marks)
    print(f"Student ID: {sid}, Name: {info['Name']}, Average Marks: {avg:.2f}")

    if(avg > top_avg):
        top_avg = avg
        top_student = info['Name']

print(f"Top Student: {top_student}, Top Average: {top_avg:.2f}")
class_avg = total_marks / len(students) * len(student_info["marks"])
print(f"Class Average: {class_avg:.2f}")