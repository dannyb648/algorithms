def isSubString(): 
	input1 = raw_input("Please enter a string: ")
	input2 = raw_input("Please enter another: ")
	if(len(input1) >= len(input2)):
		stringA = input2
		stringB = input1
	else:
		stringA = input1
		stringB = input2
	for i in range(0,((len(stringB) - len(stringA)) + 1)):
		if(stringB[i:i + len(stringA)] == stringA):
			return True
	return False
