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

def finalArr(output, stack3):
  out = []
  for i in range(len(stack3)-1,-1,-1):
    getVal1 = output.pop()
    if (type(getVal1) == type([])):
      getVal1 = getVal1[0]
    if(len(output) != 0):
      getVal2 = output.pop()
      if(type(getVal2) == type([])):
        getVal2 = getVal2[0]

    booll = stack3.pop()
    if (booll == 'OR'):
      if(type(booll) == type([])):
        out.append(getVal1 or getVal2)
      out.append(getVal1 or getVal2)

  # for i in range(len(stack3)):
  #   getVal1 = output.pop()
  #   if type(getVal1) == type([]):
  #     getVal1 = getVal1[0]
  #   if(len(output) != 0):
  #     getVal2 = output.pop()
  #     if type(getVal2) == type([]):
  #       getVal2 = getVal2[0]
  #     if (stack3.pop() == 'OR'):
  #       out.append(getVal1 or getVal2)
  #     else:
  #       out.append(getVal1 and getVal2)
  #   else:
  #     getVal2 = ""

  #     print('stack3', stack3)
  #   if (len(output) > 0):
  #     if(stack3.pop() == "OR" and type(output) != type([])):
  #       return (getVal1 or output)
  #     elif(stack3.pop() == "OR" and type(output) == type([])):
  #       return (getVal1 or output[0])
  #     elif (stack3.pop() == "AND" and type(output) != type([])):
  #       return (getVal1 and output)
  #     else:
  #       return (getVal1 and output[0])

print(finalArr([[True], [False], [True]], ['AND', 'AND']))
def canTake(course, prereq, takenCourses):
  stack1 = []
  stack2 = []
  stack3 = []
  output = []
  previ = ''
  typeof = ''

  # if course in prereq.keys():
  for i in prereq:
    print('prereq: ',i)
    if (i == course):
      if (prereq[i] == []):
        return True
      else:
        for preres in prereq[i]:
          typeof = 'string'
          if(type(preres) == type([])):
            previ = 'list'
            for j in preres:
              print(j)
              if(j == 'OR' or j == "AND"):
                stack2.append(j)
              else:
                stack1.append(j)
            print('stack1', stack1)
            print('stack2', stack2)
            output.append(analyzeStacks(stack1, stack2, takenCourses))
            print('output', output)
            stack2 = []
            stack1 = []
          elif ((preres == 'AND' or preres == 'OR') and previ == 'list'):
            stack3.append(preres)
            print('stack3', stack3)
          elif (type(preres) == type(' ') and (typeof == 'string')):
            if ((preres in takenCourses) and ('AND' not in prereq[i])):
              return True
  print('new stack3: ',stack3)
  if (len(output) > 0):
    if (finalArr(output, stack3)):
      return True

  return False
# print(canTake("CS1171",{'CS1171' : ["CS1301", "OR", "CS15XX", "OR", "CS13X1", "OR", "CS1315"]}, []))
# print(canTake("CS1100", {"CS1100": []}, []))
# print(canTake('CX4242', {"CX4242": [["MATH2605", "OR", "MATH2401", "OR", "MATH24X1", "OR", "MATH2411"], "AND", [["MATH3215", "OR", "MATH3225"], "OR", "MATH3670", "OR", ["MATH3770", "OR", "ISYE3770", "OR", "CEE3770"], "OR", "ISYE2028", "OR", "BMED2400", "OR", "ECE3770"], "AND", ["CS1331", "OR", "CS1372", "OR", "CS2316", "OR", "CX4010", "OR", "ECE2035", "OR", "ECE2036", "OR", "CX4240"]]}, ["MATH2401", "MATH3215", "CS1331"]))
# import json

# with open('Data/Inf_Med.json') as json_data:
#   coursesToGraduate = json.load(json_data)
#   json_data.close()

# with open('credithours.json') as json_data:
#   creditHours = json.load(json_data)
#   json_data.close()

# with open('prereq.json') as json_data:
#   prereq = json.load(json_data)
#   json_data.close()

# takenCourses = []
# for group in coursesToGraduate:
#   # print(group)
#   for course in coursesToGraduate[group]:
#     if (canTake(course, prereq, takenCourses)):
#       takenCourses.append(course)
#   print()

# print(takenCourses)