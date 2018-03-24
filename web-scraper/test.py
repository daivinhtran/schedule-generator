import sys
a = "CS 1301 or CS 1371"
def paser(a):
    line = a.split(" ") 
    print line
    temp = []
    i = 0
    while(i<len(line)):
        if line[i] == "CS":
            temp.append(line[i]+line[i+1])
            i+=2
            continue
        else:
            temp.append(line[i])
            i+=1
    print temp
paser(a)
sys.exit()
