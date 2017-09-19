import sys
import random
file = open("/usr/share/dict/web2", "r")
numWords = int(sys.argv[1])

dictLines = file.readlines()

randWords = []
i = 0
while(i < numWords):
    randWords.append(dictLines[random.randint(0, len(dictLines))])
    i += 1

newStr = ""
for word in randWords:
    newStr += (word.rstrip() + " ")

print(newStr)
