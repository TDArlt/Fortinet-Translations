f1 = open("prefix.txt", "r")
f2 = open("translated-file.txt", "r")

ftext = ""

for x in f1:
    ftext += x.strip() + f2.readline().strip() + "\n"

output = open("output.txt", "w")
output.write(ftext)
f1.close()
f2.close()
output.close()