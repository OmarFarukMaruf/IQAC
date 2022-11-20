students = {"name": "Sohan", "age": 35, "gender": "Male", "name": "Ratul"}
# print(students["age"])
# print(students.get("name"))
# print(students)

students["cgpa"] = 3.58

# students["age"] = 36
students["age"] += 2
print(students)

students.update({"skill": "prgramming", "address": "Rupatoli"})
print("After updating: ", students)

