fr = {}
lst = []

def main_menu():
	
	print("1.Add fruit")
	print("2.Delete fruit")
	print("3.Search fruit by name and rate")
	print("4.Change fruit by name and rate")
	
	print("6.Display")
	print("7.Add to cart")
	print("8.Exit")
	
def add_fruit():
	fr_id = input("Enter fruit id ")
	if fr_id not in fr.keys():
		temp =  {  
			
					"name" : input("\t Enter fruit name "),
				  	"rate" : int(input("\t Enter price ")),
				   	"imported_from" : input("\t Imported from? "),
				   	"imported_date" : input("\t Enter imported_date "),
				   	"buy_price" : int(input("\t Enter buy_price "))
				   
		}
			
		fr[fr_id] = temp
		print(fr)	
	else:
		print("fr_id is already taken")
	
def delete_fruit():
	d_id  = input("\tEnter fruit_id to delete ")
	if d_id not in fr.keys():
		print("\tInvalid key")
		
	else:
		del fr[d_id]
		display()
			
def search_menu():
	print("1.Search by name")
	print("2.Search by rate")
					
def search_by_name():
	name = input("Enter name ")
	flag = False
	for i in fr.values():
		if i['name'] == name:
			flag = True
			print(f"\t{i['name']} found")
	if flag == False:
		print("Invalid option")
			
def search_by_rate():
	rate = int(input("Enter price"))
	flag = False
	for i in fr.values():
		if i['rate'] == rate:
			flag = True
			print(f"{i['name']} | {i['rate']} found")
	if flag == False:
		print("Invalid option")
		
def change_menu():
	print("1.change by name")
	print("2.change by rate")
	
def change_by_name():
	m = input("\tEnter name ")
	n = input("\tEnter new name ")
	flag = False
	for i in fr.values():
		if i['name'] == m:
			flag = True
			i['name'] = n
			display()
	if flag == False:
		print("Invalid name")

def change_by_rate():
	m = int(input("\tEnter price "))
	n = int(input("\tEnter new price "))
			
	flag = False
	for i in fr.values():
		if i['rate'] == m:
			flag = True
			i['rate'] = n
			display()
					
	if flag == False:
		print("Invalid rate")
				
	else:
		print("invalid choice")
		
def cart_menu():
	for i,j in fr.items():
	
		print(f"{i} : {j}\n")
			
	print("\t1.Add to cart")
	print("\t2.Delete Cart")
	print("\t3.Display cart")
		
def add_to_cart():
	f_id = int(input("\tEnter fruit id to add to cart "))
	if f_id not in fr.keys():
		lst.append(f_id)
	else:
		print("Invalid fruit id")
		
def delete_cart():
	id_1 = input("\tEnter id to add to cart ")
	if id_1 in fr.keys():
		print("\tInvalid id") 
	else:
		lst.remove(id_1)
		
def display_cart():
	for i in lst:
		print(f"\t cart items {i}")

def display():
	for i,j in fr.items():
		print(f"\t{i} | {j['name']} | {j['rate']} | {j['imported_from']} | {j['imported_date']} | {j['buy_price']}")

while True:
	
	main_menu()
	
	ch = int(input("Enter your choice "))
	
	if ch == 1:
		#add fruit
	
		add_fruit()
			
	elif ch == 2:
		#Delete fruit by name
		delete_fruit()
			
	elif ch == 3:
		#search fruit by name and rate
		search_menu()
		
		cho = int(input("\tEnter your choice "))
		if cho == 1:
			search_by_name()
				
		elif cho == 2:
			search_by_rate()
				
		else:
			print("Invalid opyion")
				


	elif ch == 4:
		#Change fruit by name and rate
		
		change_menu()
		
		choi = int(input("Enter your choice "))
		
		if choi == 1:
			#change by name
			change_by_name()
				
		elif choi == 2:
			#change by rate
			change_by_rate()
				
	elif ch == 5:
		#Add to cart
		
		pass
				
	elif ch == 6:
		#Display
		display()
			
	elif ch == 7:
	
		#Add to cart
		cart_menu()
		
		ch = int(input("\tEnter your choice "))
		
		if ch == 1:
			#Add to cart
			add_to_cart()
			
		elif ch == 2:
			#delete cart
			delete_cart()
				
		elif ch == 3:
			#Display cart
			display_cart()
				
		else:
			print("Invalid choice")
			
	elif ch == 8:
		break
		
		
	else:
		
		print("Invalid option")
