# list
empty_list = []

numbers = [2,4,6]

tables = ["users", "classes", "teacher"]

data = ["integer", 2, "string", "float", 3.5]
print(data)

users = ["user_id", "role_id", "username", "password", "image"]
print(users[0])

users[2] = "email"
print(users)

users.append("is_active")
print(users)
users.insert(2, "name")
print(users)

users.remove("email")
print(users)

users.pop()
print(users)

del users[4]
print(users)

print(len(users))

mix = tables + data
print(mix)

for user in users:
	print(user)

for x in range(0, len(users)):
	print(users[x])

if "user_id" in users:
	print("exist")
else:
	print("not exist")
