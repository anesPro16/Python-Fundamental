# dictionary

users = {
	"id": "01K912FR1QZHEWJ6MCVK8WEK5V",
	"username": "murid",
	"password": "******",
	"is_active": False,
}

print(users)

print(users["id"])

users["is_active"] = True
print(users)

users["dummy"] = "dummy"
print(users)

del users["dummy"]
print(users)

for key in users:
	print(key, users[key])

print("")

for key, value in users.items():
	print(key, value)
