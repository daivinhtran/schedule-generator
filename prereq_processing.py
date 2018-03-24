file = open("prereq.txt", "r")
prereq = {}
specialChars = ['(', 'CS', 'MATH']

for line in file.readlines():
  # clean data
  line = line.replace('"C" or higher ', '')
  line = line.replace('Bus Process Analy/Design ', '')

  # get course name
  spl = line.split(' ')
  courseName = spl[0] + spl[1]
  

  line = ' '.join(spl[2:])

  if 'None' in line:
    print(courseName, 'None')
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


  print(courseName, line)

