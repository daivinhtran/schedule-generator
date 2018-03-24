# Analyze the stack to determine the new stack
def analyzeStacks(stack1, stack2, takenCourses):
	for i in range(len(stack1)-1, -1, -1):
		if stack1[i] in takenCourses:
			stack1[i] = True
		else:
			stack1[i] = False

	for i in range(len(stack2)):
		getVal1 = stack1.pop()
		getVal2 = stack1.pop()
		if (stack2.pop() == 'OR'):
			stack1.append(getVal1 or getVal2)
		else:
			stack1.append(getVal1 and getVal2)

	return stack1

# Anylyze two stack to give out the final output
def finalArr(output, stack3):
	out = []
	for i in range(len(stack3)):
		getVal1 = output.pop()
		getVal2 = output.pop()
		if (stack3.pop() == 'OR'):
			out.append(getVal1[0] or getVal2[0])
		else:
			out.append(getVal1[0] and getVal2[0])

	return out

# Main function to get the takenCourses
def generate():
	# takenCourses = ['cs1301', 'cs1331', 'cs2110']
	takenCourses = ['MATH2605', 'CS2110']

	# requiredCourses = ['cs1332', 'cs2340','cs2110', 'cs3510']
	# requiredCourses = ['cs1301', 'cs1322', 'cs1332', 'cs2340','cs2110', 'cs3510']
	# requiredCourses = ['cs1332', 'cs4400']
	requiredCourses = ['CS3451']

	prereq = {
		# 'cs1301': ['None'],
		# 'cs1331': ['cs1301'],
		# 'cs1322': ['cs1301'],
		# 'cs1332': ['cs1331', 'OR', 'cs1322'],
		# 'cs2340': ['cs1331'],
		# 'cs2110': ['cs1331'],
		# 'cs4400': ['cs2110']
		'CS3451': [['MATH2605', 'OR', 'MATH2401', 'OR', 'MATH2411'], 'AND', ['CS2110', 'OR', 'CS2261']]
	}

	nextSemesterCourses = []
	stack1 = []
	stack2 = []
	stack3 = []
	output = []
	previ = ''
	typeof = ''

	for i in prereq.keys():
		if i in requiredCourses:
			for j in prereq[i]:
				typeof = 'string'
				if (type(j) == type([])):
					previ = 'list'
					for ii in j:
						if (ii == 'OR' or ii == 'AND'):
							stack2.append(ii)
						else:
							stack1.append(ii)
					output.append(analyzeStacks(stack1, stack2, takenCourses))
					stack2 = []
					stack1 = []
				elif ((j == 'AND' or j == 'OR') and previ == 'list'):
					stack3.append(j)
				if (type(j) == type(' ') and (typeof == 'string')):
					if (j == 'None' and (j not in takenCourses)):
						takenCourses.append(i)
						requiredCourses.remove(i)
						if (len(nextSemesterCourses) < 3):
							nextSemesterCourses.append(i)
						elif (len(nextSemesterCourses) > 3):
							nextSemesterCourses = []
							nextSemesterCourses.append(i)
					elif (j != 'None'):
						if j in takenCourses:
							if j not in nextSemesterCourses:
								takenCourses.append(i)
								requiredCourses.remove(i)
								if (len(nextSemesterCourses) < 3):
									nextSemesterCourses.append(i)
								elif (len(nextSemesterCourses) > 3):
									nextSemesterCourses = []
									nextSemesterCourses.append(i)
							else:
								break

		# Only execute when the values of key are multiple arrays
		final = finalArr(output, stack3)
		if (final):
			takenCourses.append(i)
			requiredCourses.remove(i)
			if (len(nextSemesterCourses) < 3):
				nextSemesterCourses.append(i)
			elif (len(nextSemesterCourses) > 3):
				nextSemesterCourses = []
				nextSemesterCourses.append(i)

	print('nextSemesterCourses', nextSemesterCourses)
	print('takenCourses', takenCourses)
	print('requiredCourses', requiredCourses)

generate()