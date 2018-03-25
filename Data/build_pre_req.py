import json

def build_pre_req(filename):
  coursesToGraduate = {
    "Wellness": ["APPH1040"],
    "CoreA": ["ENGL1101", "ENGL1102", "MATH1552"],
    "CoreB": ["CS1301"],
    "CoreC": ["Humanity1", "Humanity2"],
    "CoreD": ["PHYS2211", "MATH1551", "MATH1554", "LabScience"],
    "CoreE_1": ["HIST2111", "HIST2112", "INTA1200", "POL1101", "PUBP3000"],
    "SocialScience": ["SS1", "SS2", "SS3"],
    "CoreF": ["Lab", "CS1100", "CS1331", "CS1332", "CS2050", "MATH2550"],
    "MajorRequirements": ["CS2340", "CS4001"],
    "JuniorDesign": ["CS3311", "CS3312"],
    "Stats_1": ["MATH3251", "MATH3670", "CEE3770", "ISYE3770"],
    "Combo": ["MATH3012"]
  }

  file = open(filename, 'r')
  courseCodes = ["CS", "MATH", "ECE", "ISYE", "CX", "LMC"]

  lines = file.readlines()

  i = 0
  while i < len(lines):
    line = lines[i]
    if 'Concentration' in line:
      coursesToGraduate['Concentration'] = []
      i += 1
      line = lines[i]
      while line != '\n':
        spl = line.split(' ')
        courseName = spl[:2]
        coursesToGraduate['Concentration'].append(''.join(courseName))
        i += 1
        if i == len(lines):
          break
        line = lines[i]
    elif 'Select one' in line:
      line = line.replace(' of the following', '')
      groupName = line[15:19] + '_1'
      coursesToGraduate[groupName] = []
      i += 1
      line = lines[i]
      while line != '\n':
        spl = line.split(' ')
        courseName = spl[:2]
        coursesToGraduate[groupName].append(''.join(courseName))
        i += 1
        if i == len(lines):
          break
        line = lines[i]
    elif 'Select two' in line:
      line = line.replace(' of the following', '')      
      groupName = line[15:19] + '_2'
      coursesToGraduate[groupName] = []
      i += 1
      line = lines[i]
      while line != '\n':
        spl = line.split(' ')
        courseName = spl[:2]
        coursesToGraduate[groupName].append(''.join(courseName))
        i += 1
        if i == len(lines):
          break
        line = lines[i]          
    i += 1

  for group in coursesToGraduate:
    print group
    print coursesToGraduate[group]

  with open(filename[:-4] + '.json', 'w') as fp:
    json.dump(coursesToGraduate, fp)

filenames = ['Dev_Inf.txt', 'Dev_Int.txt', 'Dev_Med.txt', 'Dev_Mod.txt', 'Dev_Peo.txt',
'Dev_Sys.txt', 'Dev_The.txt', 'Inf_Int.txt', 'Inf_Med.txt', 'Inf_Mod.txt',
'Inf_Peo.txt', 'Inf_Sys.txt', 'Inf_The.txt', 'Int_Med.txt', 'Int_Mod.txt',
'Int_Peo.txt', 'Int_Sys.txt', 'Int_The.txt', 'Med_Mod.txt', 'Med_Peo.txt',
'Med_Sys.txt', 'Med_The.txt', 'Mod_Peo.txt', 'Mod_Sys.txt', 'Mod_The.txt',
'Peo_Sys.txt', 'Peo_The.txt', 'Sys_The.txt']
for filename in filenames:
  build_pre_req(filename)
