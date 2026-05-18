# file

# print("Numeric Grading Section")

# file = open("score.txt", "w")

# while True:
# 	name = input("Input name : ")
# 	if name == "":
# 		break

# 	score = input("Input score : ")

# 	file.write(name + "," + score + "\n")
# 	print("Data", name, "has been saved")

# file.close()
# print("Program finished")

print("Showing score data")

try:
	with open("score.txt", "r") as file:
		for line in file:
			data = line.strip().split(",")
			print(data[0], ":", data[1])
except FileNotFoundError:
	print("File not found!!")

print("Program finished")