'''Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.'''
num = int(input("Enter a boundary number \n"))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n= []
for i in a:
	if i<num:
		n.append(i)
print(n)
