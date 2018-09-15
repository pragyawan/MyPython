'''Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user.'''
u_num = int(input("Enter the number to check if it is even or odd\n"))
if u_num == 0:
	print("The entered number is Zero")
else:
	if (u_num%2) == 0:
		print("The entered number is even")
	else :
		print("The entered number is Odd")