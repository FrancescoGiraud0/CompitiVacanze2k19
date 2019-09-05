#Giraudo Francesco Study Drill 2

from sys import argv

script, filename = argv

textFile = open(filename, "r")
textLines = []
pointerPosition = -1

while pointerPosition != textFile.tell():
    pointerPosition = textFile.tell()
    line = textFile.readline()
    if line != "":
        textLines.append(line)

textFile.close()

for textLine in textLines:
    print(textLine, end="")

textLineLengths = (len(textLine) for textLine in textLines)

print(f"\n||Line counter: {len(textLines)} || Characters counter: {sum(textLineLengths)}||")