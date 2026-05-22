# Guess The Number

def get_valid_number(pesan_input):
	while True:
		try:
			num = int(input(pesan_input))
			return num

		except ValueError:
			print("Input is not number!")

def app_guess():
	import random
	random_num = random.randint(1,10)
	maks = 3
	guess = 0
	while guess < maks:
		guess += 1
		try:
			# input_num = int(input("Input Number : "))
			input_num = get_valid_number("Number : ")
			if input_num > random_num:
				print(f"Ups, too high! Remainning attempt {maks - guess}")
			elif input_num < random_num:
				print(f"hmm, too low! Remainning attempt {maks - guess}")
			else:
				print("Congratulation, you right :) ")
				break
		except ValueError:
			guess -= 1
			print(f"Error! Option is not valid! Remainning attempt {maks - guess}")

	else:
		print("Too much attempt")
		print(f"Random number is {random_num}")

	input("please Enter to continue!")

def app_main():
	while True:
		print("Program Guess number")
		print("1. Guess")
		print("2. Exit")
		print("Good Luck")

		try:
			option = int(input("Option : "))
			if option == 1:
				app_guess()
			elif option == 2:
				print("Program Finished")
				break
			else:
				print("Error, input is not valid!")
		except ValueError:
			print("Error, please input valid number!")

app_main()