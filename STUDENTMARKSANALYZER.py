print("Hello Sir")    
print ("°°°WELCOME°°°")    
print("STUDENT MARKS ANALYZER")    
    
Students = int(input("How Many Students: "))    
    
marks = []        #list For marks store    
    
    
for i in range(Students):    
	m = int(input("Student Marks: "))    
	marks.append(m)    
while True:      #To Working On Loop    
	print("A:Make Marks List")    
	print("B:Make Sum Of Marks")    
	print("C:Make Average Of Marks")    
	print("D:Highest And Lowest Marks")    
	print("E:Even / Odd marks")    
	print("F: Pass/Fail")    
	print("S: Stop")    
	option = input("What You Want: ")    
	option_r = option.upper()    
	if option_r == "A":    
		print("List Of All Students Marks:",marks)    
	elif option_r == "B":    
		sum = 0    
		for i in marks:    
			sum = sum + i    
		print("Sum Of Marks: ",sum)    
	elif option_r == "C":    
		sum = 0    
		for i in marks:    
			sum = sum + i    
		average = sum/Students    
		print("Average Of Marks",average)    
	elif option_r == "D":    
		highest = marks[0]    
		lowest = marks[0]    
		for i in marks:    
			if i>highest:    
				highest = i    
			elif i<lowest:    
				lowest = i    
		print("Highest Marks In Class: ",highest)    
		print("Lowest Marks In Class: ",lowest)    
	elif option_r == "E":    
		even = []    
		odd = []    
		for i in marks:    
			if i%2 == 0:    
				even.append(i)    
			else:    
				odd.append(i)    
		print("Even Numvers Are: ",even)    
		print("Odd Numvers Are: ",odd)    
	elif option_r == "F":    
				pass_fail = []    
				for i in marks:    
					if i>=33:    
						result = "pass"    
						pass_fail.append(result)    
					else:    
						result= "fail"    
						pass_fail.append(result)    
					    
				print(pass_fail)    
	else:    
		print("Thanks For Using STUDENT MARKS ANALYZER")    
		print("Good Luck")    
		break