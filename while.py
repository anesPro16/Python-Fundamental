number = 1
while number <= 7:
	print(number)
	number += 1

password = ""

while password != "***":
	password = input("Input password: ")
	if password != "***":
		print("password invalid!")

print("password corect")