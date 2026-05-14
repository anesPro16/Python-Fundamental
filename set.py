# set

tables = {"users", "classes", "teacher"}
print(tables)

tables.add("students")
print(tables)

tables.add("students")
print(tables)

tables.remove("teacher")
print(tables)

for i in tables:
	print(i)