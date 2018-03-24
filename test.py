


def parser(s):
  res = []
  s = s.split(' ')
  i = 0
  while i < len(s):
    if s[i] == '(':
      t = []
      i += 1
      while s[i] != ')':
        if s[i] == 'MATH' or s[i] == 'CS':
          t.append(s[i] + s[i+1])
          i += 1
        elif s[i] == 'or' or s[i] == 'and':
          t.append(s[i])
        i += 1
      res.append(t)
    elif s[i] == 'CS' or s[i] == 'ECE' or s[i] == 'MATH':
      res.append(s[i] + s[i+1])
      i += 1
    elif s[i] == 'or' or s[i] == 'and':
      res.append(s[i])
    i += 1

  return res

s = '( MATH 2605 or MATH 2401 or MATH 2411 or MATH 24X1 ) and ( CS 2110 or CS 2261 ) and ( CS 1332 and CS 2340 )'
print(parser(s))