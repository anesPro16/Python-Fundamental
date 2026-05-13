# while else loop

corect_pass = "***"
attempt = 0

attempt_full = 2

while attempt < attempt_full:
	password = input("Input password : ")
	attempt += 1

	if password == corect_pass:
		print("Login Successfully")
		break
	else:
		print(f"password invalid! remainning attempt {attempt_full - attempt}")
else:
	print("Too much attempt, sorry you can not access!")