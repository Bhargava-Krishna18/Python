Employees = []

while True:
	a=1
	print("1. Add student")
	print("2. Delete student")
	print("3. Search Student")
	print("4. Change a Employee Data")
	print("5. Display all Employees") 
	print("6. exit")
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add Employee
		name = input("Enter name")
		Employees.append(name)
	elif ch == 2:
		#Delete Employee
		print(Employees)
		print("Choose name ")
		name = input("Enter name")
		Employees.remove(name)
	elif ch == 3:
		#Search Employee
		name = input("Enter name")
		if name in Employees:
			print(name, "exists")
		else:
			print("oops! Name does not exist")
	elif ch == 4:
		#Change Employee data
		name = input("Enter the name")
		index =	Employees.index(name)
		new_name = input("Enter new name")
		Employees[index] = new_name

	elif ch == 5:
		for i in Employees:
			print(str(a)+ '.'+ i)
			a += 1
	elif ch == 6:
		break
	else:
		print("Invalid Choice")
