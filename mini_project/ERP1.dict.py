emp = {}

def main_menu():
	print("1.Add employee")
	print("2.Delete employee")
	print("3.search employee by name")
	print("4.Change employee data")
	print("5.Display")
	print("6.exit")
	

def add_emp():
	serial = int(input("Enter serial number "))
	if serial not in emp:
		temp = {
			"name": input("\tEnter name "),
			"age" : int(input("\tEnter age ")),
			"gender" : input("\tEnter gender "),
			"place" : input("\tEnter place "),
			"salary" : int(input("\tEnter salary ")),
			"pr_comp" : input("\tEnter previous company "),
			"joining_date" : input("\tEnter joining date ")
	}
	
				
		emp[serial] = temp
	else:
		print("serial no already taken")
			
def del_emp():
	serial_no = int(input("Enter serial no to delete "))
	for i in (emp.copy()).keys():
		if i == serial_no:
			del emp[i]
		
def search_emp_name():
	name = input("Enter name ")
	flag = False
	for i in emp.values():
		if i['name'] == name:
				
			flag = True
			print("\tCongo! Name exists")
				
				
	if flag == False:
		print("\tOops! Name does not exist")

def change_menu():
	print("1.Change name")
	print("2.Change age")
	print("3.Change gender")
	print("4.Change salary")
	
def change_by_name():
	m = input("\tEnter name ")
	n = input("\tEnter new name ")
	flag = False
	for i in emp.values():
		if i['name'] == m:
			flag = True
			i['name'] = n
					
	if flag == False:
		print("\tEnter valid name")
				
def change_by_age():
	age = int(input("\tEnter age "))
	new_age = int(input("\tEnter new age "))
	flag = False
	for i in emp.values():
		if i['age'] == age:
			flag = True
			i['age'] = new_age
			
	if flag == False:
		print("\tEnter valid age")
				
def change_by_gender():
	gender = input("\tEnter gender")
	new_g = input("\tEnter new gender")
	flag = False
	for i in emp.values():
		if i['gender'] == gender:
			Flag = True
			i['gender'] = new_g
					
	if flag == False:
		print("\tEnter valid gender")
		
def change_by_salary():
	sal = int(input("\tEnter salary"))
	new_s = int(input("\tEnter new salary"))
	flag = False
	for i in emp.values():
		if i['salary'] == sal:
			flag = True
			i['salary'] = new_s
					
	if flag == False:
		print("\tEnter invalid salary")
	
				
def Display():
	for i,j in emp.items():
		print(f"\t{i} | {j['name']} | {j['age']} | {j['gender']} | {j['salary']} | {j['pr_comp']} | {j['joining_date']} " )


	
while True:
	main_menu()
	
	ch = int(input("Enter your choice "))
	
	if ch == 1:
		#Add employee
		add_emp()
			
		
		
	elif ch == 2:
		#Delete employee
		del_emp()
			
				
	elif ch == 3:
		#search employee by name
		search_emp_name()
				
	elif ch == 4:
		#Change employee data
		change_menu()
		
		cho = int(input("Enter your choice "))
		
		if cho == 1:
			change_by_name()
					
		elif cho == 2:
			change_by_age()
					
		elif cho == 3:
			change_by_gender()
					
		elif cho == 4:
			change_by_salary()
	elif ch == 5:
		# Display
		Display()
					
	elif ch == 6 :
		break
		
	else:
		print("invalid choice")
	
