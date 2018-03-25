import re
def analyzeCourseToGraduate():
	file = open("modeling_devices.txt", "r+")
	coursesToGraduate = {
		"Wellness": ["APPH1040", "OR", "APPH1050"],
		"Core A": ["ENGL1101", "ENGL1102", "MATH1552"],
		"Core B": ["CS1301"],
		"Core C": ["AnyHUM"],
		"Core D": ["PHYS2211", "MATH1551", "MATH1554", "Lab"],
		"Core E_1": ["HIST2111", "HIST2112", "INTA1200", "POL1101", "PUBP3000"],
		"Any SS": ["SS1", "SS2", "SS3"],
		"Core F": ["Lab", "CS1100", "CS1331", "CS1332", "CS2050", "MATH2550"],
		"Major Requirements": ["CS2340", ["CS4001", "OR", "CS4002"]],
		"Junior Design": ["Junior Design"]
	}
	core = ["CS", "MATH", "ECE", "ISYE", "CX", "LMC"]
	name = ["Concentration", "Building Devices", "Devices in the Real World", "Computational Science and Engineering"]
	quality = ["one", "two", "three"]
	values = []
	qualities = ""
	for line in file:
		if line in name:
			print(True)
		line = line.split(" ")

		
		i = 0
		for word in line:
			if (word == ' '):
				print("Here")

	# print(coursesToGraduate)
analyzeCourseToGraduate()
