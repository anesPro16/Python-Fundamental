# control flow

# numbers = int(input("Input number : "))
# if numbers > 0:
# 	print("Positive")

# if numbers < 0:
# 	print("Negative")

# if numbers == 0:
# 	print("Zero")

# score = int(input("Input score : "))

# if score >= 75:
# 	print("Passed")
# else:
# 	print("Failed")


# score = int(input("Input score : "))

# if score >= 87:
# 	print("A")
# elif score >= 78:
# 	print("B")
# elif score >= 69:
# 	print("C")
# elif score >= 50:
# 	print("D")
# else:
# 	print("E")

# age = int(input("Input age : "))
# is_licenced = input("Are you have licence? (yes/no) : ")

# if age >= 18 and is_licenced == "yes":
# 	print("You can drive")
# else:
# 	print("You can\'t drive")

# email = input("Email : ")
# password = input("Password : ")

# if email == "user":
# 	if password == "***":
# 		print("Login successfully")
# 		print(f"Welcome {email}")
# 	else:
# 		print("password invalid!")
# else:
# 	print("email is not registered!")

# days = input("Input day : ").lower()

# match days:
# 	case "monday" | "tuesday" | "wednesday" | "thursday" | "friday" :
# 		print("Working day")
# 	case "saturday" | "sunday" :
# 		print("Weekend")
# 	case _:
# 		print("day is invalid!")

num = int(input("input numbers : "))

result = "Positive" if num >= 0 else "Negative"
print(result)