from fruit_class import Fruits
fr = {}
cart = []


		
def main_menu():
	print("1.Add fruit")
	print("2.Delete fruit by name")
	print("3.Search fruit by name and rate")
	print("4.Change fruit name and rate")
	print("5.Display")
	print("6.Fruit Shop")
	print("7.Exit")
	
def add_fruit():
	fr_id = int(input("\tEnter fruit id "))
	if fr_id not in fr.keys():
		temp = {   
				"name" : input("\tEnter fruit name "),
				"rate" : int(input("\tEnter fruit rate ")),
				"imp_frm" : input("\tImported from? "),
				"imp_date" : input("\tEnter imported date "),
				"buy_price" : int(input("\tEnter buy price "))
					
		}
			
		fr[fr_id] = temp
		
	else:
		print("\tfr_id already taken")
		
def delete_fruit():
	f_id = int(input("\tEnter fruit to delete "))
	if fr_id not in fr.keys():
		print("\tFruit id not found")
			
	else:
		del fr[fr_id]
		
def search_menu():
	print("\t1.Search by name")
	print("\t2.Search by rate")

def search_by_name():
	name = input("\tEnter name ")
	flag = False
	for i in fr.values():
		if i['name'] == name:
			flag = True
			print(f"\t{i['name']} found")
	if flag == False:
		print("\tfruit name not found")
		
def search_by_rate():
	rate = int(input("\tEnter rate "))
	flag = False
	for i in fr.values():
		if i['rate'] == rate:
			flag = True
			print(f"\t{i['rate']} found")
	if flag == False:
		print("\tfruit rate not found")
				
def change_menu():
	print("\t1.Change by name")
	print("\t2.Change by rate")
	
def change_by_name():
	name = input("\tEnter name ")
	new_name = input("\tEnter new name ")
	flag = False
	for i in fr.values():
		if i['name'] == name:
			flag = True
			i['name'] = new_name
					
	if flag == False:
		print("\tfruit not found")
		
def change_by_rate():
	rate = int(input("\tEnter age "))
	new_rate = int(input("\tEnter new age "))
	flag = False
	for i in fr.values():
		if i['rate'] == rate:
			flag = True
			i['rate'] = rate
					
	if flag == False:
		print("\tInvalud rate")
	
def display():
	for i,j in fr.items():
		print(f"\t{j['name']} | {j['rate']} | {j['imp_frm']} | {j['imp_date']} | {j['buy_price']}")
		

def Fruit_shop_menu():
	print("\t1.Add to cart")
	print("\t2.Delete from cart")
	print("\t3.Bill")
	print("\t4.Display the cart")
	print("\t5.Exit")
	
def add_to_cart():
	f_id = int(input("\tEnter fruit id to add to cart "))
	for i,j in fr.items():
		print(i,".",j['name'])
					
	cart.append(fr[f_id])
	
def delete_from_cart():
	idn = int(input("\tEnter fruit to delete "))
	if idn not in cart:
		print("\tInvalid fruit")
					
	else:
		cart.remove(idn)
	
def bill():
	for i in cart:
					
		print(f"{fr_id} | {fr}")
		print("\t\tThank YOU")
		
def display_cart():
	for i in cart:
					
		print(f"{fr}")


while True:

	main_menu()
	
	ch = int(input("Enter your choice: "))
	if ch == 1:
		#Add fruit
		add_fruit()
		
	elif ch == 2:
		#Delete fruit 
		delete_fruit()
				
	elif ch == 3:
		#search fruit by name and rate
		search_menu()
		
		choi = int(input("\tEnter your choice "))
		
		if choi == 1:
			search_by_name()
				
		elif choi == 2:
			search_by_rate()
			
		else:
			print("\tInvalid option")

				
	elif ch == 4:
		#Change fruit by name aand rate
		change_menu()
		
		cho = int(input("\tEnter your choice "))
		
		if cho == 1:
			#Change by name
			change_by_name()
				
		elif cho == 2:
			#Change by age
			change_by_rate()
				
		else:
			print("\tInvalid option")
			
	elif ch == 5:
		#Display
		display()
		
	elif ch == 6:
		#Fruit shop
		while True:
			Fruit_shop_menu()
			
			ch = int(input("\tEnter your choice "))
			
			if ch == 1:
				#add to cart
				add_to_cart()
				
			elif ch == 2:
				#Delete from cart
				delete_from_cart()
					
			elif ch == 3:
				#Bill
				bill()
			elif ch == 4:
				#Display
				display_cart()
					
			elif ch == 5:
				break
				
			else:
				print("\tInvalid option")
				
				
			
				
		
	else:
		print("exit")
		
				
		
		
	
					
		
		
		
