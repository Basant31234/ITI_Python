import time
import os


Types=["Fruits","QUA","LE"]
Fruits=["Apple" ,"Orange" ,"Mango"]
LE=[2.5,			3.5 ,		5]
QUA=[50,			50,			50]
buy=[]
multiply=[]



print("\n------------Welcome to ITI shop------------\n")

myTime = time.ctime()
print(myTime)

print("-----------------------------------------------")

#main menu
while True :

	selection=input("""
 For customer 			   press 1 
 For owner    			   press 2 
 For exist    			   press 0

 your choise is """)
	print("-----------------------------------------------")	
	os.system('cls')
	
	#customer mode
	
	if selection=="1":
		while True :
			print("\n------------Welcome to ITI shop------------\n")
			cus=input("""\nto show our products        press 1\nTo Buy from our products    press 2\nTo print the bill           press 3\nTo back                  press 0\nyour choise is """)
			print("-----------------------------------------------")
			
			if cus=="1":
				print(Types)
				for list in zip(Fruits,QUA,LE):
					print(list)
			
			if cus=="2":
				os.system('cls')
				
				print("\n------------Welcome to ITI shop------------\n")	
				for n in range ( len(Fruits) ):
					print("Please enter the QUA of",Fruits[n])
					k=int(input())
					buy.append(k)
					
					#to know the remaining
				sub_QUA=[]
				for x,y in zip(QUA,buy):
					sub_QUA.append(x-y)
				QUA=sub_QUA
						
			if cus=="3":
				os.system('cls')
				print("\n------------Welcome to ITI shop------------\n\n\n\n")	
				
				
				for x,y in zip(LE,buy):
					multiply.append(x*y)
					
				print(Types)
				for list in zip(Fruits,buy,multiply):
					print(list)
					
				print("\n\n\n**************************\n\n\nTOTAL PRICE=",sum(multiply),"\nprices include VAT")
				print("\n\n\n**************************\n\n\nSERVED BY :BASANT KARIEM\nBrought to you by ITI SHOP")
				
				myTime = time.ctime()
				print(myTime)
				print("-----------------------------------------------")
				break
				
				
			if cus=="0":
				break
		
		
		#owner mode
		
	elif selection=="2":
		pa=int(input("PASSWORD\n"))
		if pa==1234:
			os.system('cls')
			while True :
				
				
				print("\n------------Welcome to ITI shop------------\n")
				own=input("""\nTo Add new products       press 1\nTo Show Products  	  press 2\nTo Change cost		  press 3\nTo Change Quanity	  press 4\nTo back		          press 0\nyour choise is """)
				print("-----------------------------------------------")
				
				if own=="1":
					os.system('cls')
					print("\n------------Welcome to ITI shop------------\n")
					
					added=input("please add the product: ")
					Fruits.append(added)
					
					q_added=input("please add the quantity: ")
					QUA.append(q_added)
					
					a_co=input("please add the cost: ")
					LE.append(a_co)
					
					print("-----------------------------------------------")
					print("THE NEW MENU:")
					
					print("\n",Types)
					for list in zip(Fruits,QUA,LE):
						print(list)
					
						
				elif own=="2":
					os.system('cls')
					print("\n------------Welcome to ITI shop------------\n")
					print(Types)
					for list in zip(Fruits,QUA,LE):
						print(list)
					
					
				
				if own=="3":
					os.system('cls')
					print("---THE OLD MENU---\n")
					
					print(Types)
					for list in zip(Fruits,QUA,LE):
						print(list)
						
					ch_fruit=input("\nPlease enter the fruit name:")
					ch_cost=int(input("Please enter tht new price:"))
					
					ind_fruit=Fruits.index(ch_fruit)
					LE.insert(ind_fruit,ch_cost)
					
					print("\n---THE NEW MENU---\n")
					
					print(Types)
					for list in zip(Fruits,QUA,LE):
						print(list)
						
						
				if own=="4":
					os.system('cls')
					print("---THE OLD MENU---\n")
					
					print(Types)
					for list in zip(Fruits,QUA,LE):
						print(list)
						
					QUA_fruit=input("\nPlease enter the fruit name:")
					ch_QUA=int(input("Please enter tht new Quantity:"))
					
					ind_fruit=Fruits.index(QUA_fruit)
					QUA.insert(ind_fruit,ch_QUA)
					
					print("\n---THE NEW MENU---\n")
					
					print(Types)
					for list in zip(Fruits,QUA,LE):
						print(list)
				
				
				if own=="0":
					break
					
		else :
			print("WRONG PASSWORD")
		
		
		
	elif selection=="0":
		print("-------------------THANK YOU-------------------")
		
		break
