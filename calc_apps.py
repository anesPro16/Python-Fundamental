# simple calculator

def get_valid_number(pesan_input):
	while True:
		try:
			num = float(input(pesan_input))
			return num

		except ValueError:
			print("Input is not number!")

def is_continue():
	while True:
		ask = input("Are you want to exit? (q/n) : ").lower()
		if ask == 'q':
			print("Ok, Nice to meet you :) ")
			return False
		elif ask == 'n' :
			return True
		else:
			print("Input is not valid!")


def add_app():
	print("Program ADD")
	num = get_valid_number("Number : ")
	num2 = get_valid_number("Number2 : ")
	result = num + num2
	print(f"{num} + {num2} = {result} ")

	is_continue()

def minus_app():
	print("Program MINUS")
	num = get_valid_number("Number : ")
	num2 = get_valid_number("Number2 : ")
	result = num - num2
	print(f"{num} - {num2} = {result} ")

	is_continue()

def times_app():
	num = get_valid_number("Number : ")
	num2 = get_valid_number("Number2 : ")
	result = num * num2
	print(f"{num} x {num2} = {result} ")

	is_continue()

def divide_app():
	print("Program DIVIDE")

	num = get_valid_number("Number : ")

	while True:
		num2 = get_valid_number("Number2 : ")
		if num2 == 0:
			print("don\'t input zero!")
		else:
			break

	result = num / num2
	print(f"{num} / {num2} = {result} ")

	is_continue()

def main_app():
	attempt = 0

	attempt_full = 3

	# while True:
	while attempt < attempt_full:
		print("SIMPLE CALCULATOR")
		print("1. ADD")
		print("2. MINUS")
		print("3. TIMES")
		print("4. DIVIDE")
		print("5. Exit")


		try:
			option = int(input("Option : "))

			if option == 1:
				add_app()
			elif option == 2:
				minus_app()
			elif option == 3:
				times_app()
			elif option == 4:
				divide_app()
			elif option == 5:
				print("Ok, Nice to meet you :) ")
				break
			else:
				attempt += 1
				print(f"Error! Option is not valid! Remainning attempt {attempt_full - attempt}")
		except ValueError:
			attempt += 1
			print(f"Error, Please input valid number! Remainning attempt {attempt_full - attempt}")
	else:
		print("Too much attempt, sorry you can not access!")

main_app()
