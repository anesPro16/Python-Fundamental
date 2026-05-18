# function

def function_name():
	print("This is function example \n")

function_name()

def greeting(name):
	print(f"Hi {name}, How are you? \n")

greeting("Aldi")
greeting("Nez")

def rumus_luas_segitiga(alas, tinggi):
	luas = alas * tinggi / 2
	print(f"luas segitiga : {luas} \n")

rumus_luas_segitiga(3, 5)

def bilangan_pangkat(angka, pangkat):
	return angka**pangkat;


print("2 pangkat 3 = ",bilangan_pangkat(2, 3))

def greeting2(name, greeting="Hi"):
	print(greeting, name)

greeting2("Nez")
greeting2("Aldi", "Good morning")

def users(name, username, role):
	print("\nName", name)
	print("Username", username)
	print("Role", role)
	print("="*12)

users("Nez", "nez123", "murid")

def create_account(username, password="***", is_active=False):
	print("")
	print("Username  : ", username.title())
	print("Password  : ", password)
	print("Is Active : ", is_active)
	print("")

create_account("Nez")
create_account("Aldi", is_active=True)

def local_fun():
	a = 2
	print(f"value a is {a}")

local_fun()
# print(a) # NameError: name 'a' is not defined, because a is local variable

global_name = "Nez"

def show_name():
	print(f"Name : {global_name}")

show_name()

def change_name():
	global global_name
	global_name = "Nes"
	print(f"Name : {global_name}")

change_name()
show_name()

def print_list(*list):
	for item in list:
		print(item)

print_list(2,4,6,8)

def print_diction(**dict):
	for key, value in dict.items():
		print(key, value)

print_diction(name="Nez", password="***", is_active=True)