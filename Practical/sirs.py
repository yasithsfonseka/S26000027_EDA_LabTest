
students = {
    "S001":{"name":"Alice", "marks":[85, 90, 78]},
    "S002":{"name":"Bob", "marks":[92, 88, 95]},
    "S003":{"name":"Charlie", "marks":[78, 82, 80]}
}

top_avg = 0
top_student = ""
total_marks = 0
for student_id, student_info in students.items():
    marks = student_info["marks"]
    total_marks += sum(marks)
#average_marks = total_marks / (len(students) * len(student_info["marks"]))
#print(f"Average marks of all students: {average_marks:.2f}")
for sid , info in students.items():
    marks = info["marks"]
    total_marks += sum(marks)
    avg = sum(marks) / len(marks)
    print(info["name"], "average marks:", round(avg, 2))
    
    if(avg > top_avg):
        top_avg = avg
        top_student = info["name"]
print("Top student:", top_student, "with average marks:", round(top_avg, 2)) 
class_avg = total_marks / (len(students) * len(student_info["marks"]))
print(f"Average marks of all students: {class_avg:.2f}")