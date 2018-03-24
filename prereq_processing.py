def parser(s):
  coursePrefix = ['MATH', 'CS', 'ECE', 'CX', 'ISYE', 'BMED', 'CEE']
  res = []
  s = s.split(' ')
  i = 0
  while i < len(s):
    if s[i] == '(':
      t = []
      i += 1
      while s[i] != ')':
        if s[i] in coursePrefix:
          t.append(s[i] + s[i+1])
          i += 1
        elif s[i] == 'OR' or s[i] == 'AND':
          t.append(s[i])
        i += 1
      res.append(t)
    elif s[i] in coursePrefix:
      res.append(s[i] + s[i+1])
      i += 1
    elif s[i] == 'OR' or s[i] == 'AND':
      res.append(s[i])
    i += 1

  return res

file = open("prereq.txt", "r")
prereq = {}
specialChars = ['(', 'CS', 'MATH']

for line in file.readlines():
  # clean data
  line = line.replace('CSCL', '')
  line = line.replace('"C" or higher ', '')
  line = line.replace('Bus Process Analy/Design ', '')
  line = line.replace('Math', 'MATH')

  # get course name
  spl = line.split(' ')
  courseName = spl[0] + spl[1]
  
  line = ' '.join(spl[2:])

  if 'None' in line:
    prereq[courseName] = []
    continue

  for i in range(len(line) - 5):
    if line[i] == '(':
      line = line[i:]
      break
    elif line[i:i+2] == 'CS':
      line = line[i:]
      break
    elif line[i:i+3] == 'ECE':
      line = line[i:]
      break
    elif line[i:i+4] == 'MATH':
      line = line[i:]
      break

  line = line[:-1]
  line = line.replace('(', '( ')
  line = line.replace(')', ' )')
  line = line.replace(';', ' ;')
  line = line.replace('or', 'OR')
  line = line.replace('and', 'AND')
  prereq[courseName] = parser(line)

for course in prereq:
  print(course, prereq[course])
