i = 0
while i<5:
    print(“Harry”)
    i = i+1

l = [1, 7, 8]
for item in l:
	print(item)

for i in range(0, 7):		#range(7) can also be used
	print(i)		#prints 0 to 6

l = [1, 7, 8]
for item in l:
	print(item)
else:
	print(“Done”)	#This is printed when the loop exhausts!

for i in range(0, 80):
	print(i)	#This will print 0, 1, 2 and 3
	if i == 3:
		break

        for i in range(4):
	print(“printing”)
	if i == 2:	#if i is 2, the iteration is skipped
		continue
	print(i)

l = [1, 7, 8]
for item in l:
	pass		#without pass, the program will throw an error
