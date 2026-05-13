# nested loop

print("times table")

for x in range(1,10):
	for y in range(1, 10):
		result = x * y
		print(x, " x ", y, "= ", result)
	print("-" *  14)