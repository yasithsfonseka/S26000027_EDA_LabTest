data = {"name": "Alice", "age": 30, "city": "New York"}
print(data["name"])
print(data["age"])  
print(data["city"])

print(data.get("name"))
print(data.get("country", "USA"))

for value in data.values():
    print(f"Value: {value}")

for key, value in data.items():
    print(f"{key}: {value}")

#///////////////////////////////////////

students = ("Alice", "Bob", "Charlie", "David")
print(students[0])
print(students[1])

print(len(students))

print(students[:3])
print(students[-2:])

students[0] = "Eve"  # This will raise a TypeError since tuples are immutable
