file = open("credithours.txt", "r+")
map = {}
for line in file:
    line = line.split(" ")
    i = 0
    for word in line:
        word = line[i]
        if word == "CS":
            map[line[i]+line[i+1]] = 0
            key = line[i]+line[i+1]
        if word == "Credits":
            map[key] = line[0:(i)]
        i+=1

