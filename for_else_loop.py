# for else

words = input("Input word: ")
find_char = input("Input find character: ")

for char in words:
	if char == find_char:
		print(f"Char {find_char} is found in word")
		break
else:
	print(f"Char {find_char} is not found in word!")