# break
secret_num = 5

while True:
	odds = int(input("Input number : "))
	if odds == secret_num:
		print("You right")
		break
	else:
		print("ups!, nice try")