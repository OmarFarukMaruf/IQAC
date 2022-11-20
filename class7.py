
students = {"name": "Sohan", "age": 35, "gender": "Male"}

print(students["age"])

print(students.get("name"))

students["cgpa"] = 3.58

# students["age"] = 36
students["age"] += 2

print(students)

students.update({"skill": "prgramming", "address": "Rupatoli"})

print(students)

# students.pop("cgpa")

students.popitem()

print(students)

print(students.setdefault("weight", 56))

# students.clear()

# print(students)

a = ("rahim", "karim", "sofiq")
b = 1000

boys = dict.fromkeys(a, b)

print(boys)


for key in students.keys():
    print(key, " => ", students[key])

for value in students.values():
    print(value)

for item in students.items():
    print(item[0] , " => ", item[1])

for key, value in students.items():
    print(key, " => ", value)

print(students.items())

# name, age, weight = ("rahim", 34, 99)

# print(name)

# name, *others = ("rahim", 34, 99)

# print(others)