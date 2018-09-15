'''Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.'''
u_name = input("Enter the name :")
u_age = input("Ener the age: ")
curr_age = int(u_age)
years100 = (100-curr_age)
print("You will turn 100 years old after ",years100," Years")