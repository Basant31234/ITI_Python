
import os



while True:
	os.system('cls')
	print("\n\n\t------------Welcome to ITI calculator------------\n")
	mode = int (input ("\n\n\n\tStandard mode      press 1\n\tProgrammer mode    press 2\n\tConversion mode    press 3\n\tExit               press 0\n\n\n\tPLEASE CHOOSE THE OPERATION NUMBER : "))
	os.system('cls')
	
	# Standard mode
	if mode ==1 :
		
		while True:
		
			print("\n\n\t------------STANDARD MODE------------\n\n\n")
			print(" \tFOR EXAMPLE : 2 * 3 + 6 - 9 \n\n")
			Result=eval(input("\n\tEnter the numbers and the operations [ + - * / % ] \n\t"))
			print("\n\tResult = ",Result)
			
			exit=int(input("\n\n\n\n\n\t\t\tEXIT -----> PRESS 0 "))
			break
		
	# Programmer mode	
	elif mode ==2 :

		while True:
		
			print("\n\n\t------------PROGRAMMER MODE------------\n\n\n")
			print(" \tFOR EXAMPLE : 2 << 3 \n\n")
			Result=eval(input("\n\tEnter the numbers and the operations [ << >> &  | ^ ~] \n\t"))
			print("\n\tResult = ",Result," = ", bin(Result))
			
			exit=int(input("\n\n\n\n\n\t\t\tEXIT -----> PRESS 0 "))
			break	
	
	# Conversion mode	
	
	elif mode ==3 :	
		print("\n\n\t------------CONVERSIOM MODE------------\n\n\n")
		n1=int(input("\n\tENTER AN INTEGER NUMBER : "))
		
		while True:	
			
			oper=int(input("\n\tchoose the operation\n\t  1-TO Binary\n\t  2-To hexa\n\t  3-To oct\n\t  0-EXIT\n\n\n\t THE OPERATION NUMBER IS "))	
				
			if oper ==1:
				print("\n\t THE BINARY OF ",n1," = ",bin(n1))
				
			elif oper ==2:
				print("\n\t THE HEXA OF ",n1,"   = ",hex(n1))
				
			elif oper ==3:
				print("\n\t THE OCTA OF ",n1,"   = ",oct(n1))
				
			exit=int(input("\n\n\n\n\n\t\t\tEXIT -----> PRESS 0 "))
			break	
				
				
				
	elif mode ==0:
		break
