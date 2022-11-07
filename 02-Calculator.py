

while True:
	mode=int(input("Standard mode      press 1\nProgrammer mode    press 2\nConversion mode    press 3\nExit               press 0\n"))
	
	
	# Programmer mode
	if mode ==1 :
	
		n1=int(input("\nThe first number:"))
		n2=int(input("The second number:"))
		while True:
			
			oper=int(input("\nchoose the operation\n1-addition\n2-subtraction\n3-multiplication\n4-division\n5-module\n6-power\n7-square root\n\n0-EXIT\n"))
			if oper ==1:
				print("\n",n1,"+",n2,"=",n1+n2)
				
			elif oper ==2:
				print("\n",n1,"-",n2,"=",n1-n2)	
				
			elif oper ==3:
				print("\n",n1,"*",n2,"=",n1*n2)
				
			elif oper ==4:
			
				if n2==0:
					print(n2," ERROR")
				else:
					print("\n",n1,"/",n2,"=",n1/n2)
					
			elif oper ==5:
				print("\n",n1,"%",n2,"=",n1%n2)
				
			elif oper ==0:
				break
		
	# Programmer mode	
	elif mode ==2 :
	
		n1=int(input("\nThe first number:"))
		n2=int(input("The second number:"))

		print(n1,"=",bin(n1))
		print(n2,"=",bin(n2))

		while True:
			
			oper=int(input("\nchoose the operation\n1-shift right\n2-shift left\n3-AND\n4-OR\n5-XOR\n6-NOT\n\n0-EXIT\n"))
			
			if oper ==1:
				print("\n",n1,">>",n2,"=",n1>>n2,"=",bin(n1>>n2))
				
			elif oper ==2:
				print("\n",n1,"<<",n2,"=",n1<<n2,"=",bin(n1<<n2))
				
			elif oper ==3:
				print("\n",n1,"&",n2,"=",n1&n2,"=",bin(n1&n2))
				
			elif oper ==4:
				print("\n",n1,"|",n2,"=",n1 | n2,"=",bin(n1 | n2))
				
			elif oper ==5:
				print("\n",n1,"^",n2,"=",n1 ^ n2,"=",bin(n1 ^ n2))
				
			elif oper ==6:
				print("\n~",n1,"=",~n1,"=",bin(~n1))
				
			elif oper ==0:
				break
				
	
	# Conversion mode	
	
	elif mode ==3 :		
		n1=int(input("\nThe integer number:"))
		
		while True:	
	
			oper=int(input("\nchoose the operation\n1-TO Binary\n2-To hexa\n3-To oct\n0-EXIT\n"))	
				
			if oper ==1:
				print("\n",n1,"=",bin(n1))
				
			elif oper ==2:
				print("\n",n1,"=",hex(n1))
				
			elif oper ==3:
				print("\n",n1,"=",oct(n1))
				
			elif oper ==0:
				break
				
				
	elif mode ==0:
		break
