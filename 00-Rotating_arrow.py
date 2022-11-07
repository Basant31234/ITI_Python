import time
import os



while True:

	'''right'''
	# virtical space
	for i in range (5):			 
		print("\n")
	x=6
	# upper part
	for i in range (1, x):		
		for m in range (30):
			print(" ", end="")
		for j in range (1, i+1):
			print("* ", end="")
		print("")
		
	# middle part	
	for m in range (23): 			
		print(" ", end="")
	for j in range (2*x):
		print("* ", end="")
	print()		
	
	# lower part
	for i in range (x, 1,-1):		
		for m in range (30):
			print(" ", end="")
		for j in range (1, i):
			print("* ", end="")
		print()	
	
	# delay and clear	
	time.sleep(1)
	os.system('cls')	



	 # '''up'''
	 # virtical space
	for i in range (2): 
		print("\n")
		
		
	n = 12
	for i in range(3):
		for j in range(n+10):
			print(' ', end='')
		for k in range(1):
			print('*', end='')
		print()

	for i in range(3,n,2):
		for j in range(n+11-i):
			print(' ', end='')
		for k in range( i):
			print('*', end=' ')
		print()
		
	for i in range(n+1,n+5):
		for j in range(n+10):
			print(' ', end='')
		for k in range(1):
			print('*', end='')
		print()	
		

	time.sleep(1)
	os.system('cls')

	 # left
	 # virtical space
	for i in range (5): 
		print("\n")
		
		# upper part
	for i in range (1,x) :
		for m in range (1,x-i-i+1+11):
			print(" ",end="")
		for j in range (1,i+1):
			print("* ",end="")
		print()
		
		# middle part
	for m in range (-1):
		print(" ", end="")
	for j in range (2*x):
		print("* ", end="")
	print()
	
	
		# lower part
	for i in range (x, 1,-1):
		for m in range (1,x-i-i+3+11):
			print(" ", end="")
		for j in range (1, i):
			print("* ", end="")
		print()	
		
		# delay and clear
	time.sleep(1)
	os.system('cls')
	
	

	 # down
	 # virtical space
	for i in range (7): 
		print("\n")
		
	
	for i in range(4):
		for j in range(n+10):
			print(' ', end='')
		for k in range(1):
			print('*', end='')
		print()


	for i in range(3,n,2):
		for j in range(n-3+i):
			print(' ', end='')
		for k in range(n+1+3-i,2,-1):
			print('*', end=' ')
		print()
		
		
	for i in range(3):
		for j in range(n+10):
			print(' ', end='')
		for k in range(1):
			print('*', end='')
		print()
		
		
	time.sleep(1)
	os.system('cls')		

	# excit=input("TO EXCIT PRESS 0")
	# if excit ==0:
		# break
	
