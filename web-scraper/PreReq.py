file = open("prereq.txt", "r")

for line in file.readlines():
  print(line)


# build prereq hashmap
prereq = {
  cs1171: [cs1301, 'or', cs15xx, 'or', ]
}


takenCourses = [....]
requiredCoursesToGraduate = [....]
nextSemesterCourses = generate(takenCourses, requiredCoursesToGraduate)
requiredCoursesToGraduate = requiredCoursesToGraduate - nextSemesterCourses
takenCourses = takenCourses + nextSemesterCourses
nextSemesterCourses = generate(takenCourses, requiredCoursesToGraduate)
