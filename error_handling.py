# error handling

# print("'(' was never closed" # SyntaxError: '(' was never closed

# print(undefined_var) # NameError: name 'undefined_var' is not defined

# value_error = int("one") # ValueError: invalid literal for int() with base 10: 'one'

data = [2,4,6]
# print(data[3]) # IndexError: list index out of range

users = {"name" : "Nez"}
# print(users["id"]) # KeyError: 'id'

# print(1/0) # ZeroDivisionError: division by zero

# try:
# 	num = int(input("number   : "))
# 	num2 = int(input("number 2 : "))
# 	result = num / num2
# 	print(f"Result {num} : {num2} = {result}")
# except ValueError:
# 	print("Input is not number!")
# except ZeroDivisionError:
# 	print("Input can not division by zero!")
# except:
# 	print("Ups, something wrong!")

# print("Program Finished")

try:
	num = int(input("number: "))
except ValueError:
	print("Input is not number!")
else:
	print(f"The number you entered {num} ")
	if num > 0:
		print("Positive")
	elif num < 0:
		print("Negative")
	else:
		print("Zero number")
finally:
	print("Program Finished")