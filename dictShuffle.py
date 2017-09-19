import sys
import random
file = open("/usr/share/dict/web2", "r")
numWords = int(sys.argv[1])

#Every word is separated by a newline
dictWords = file.readlines()

randWords = []
i = 0
while(i < numWords):
    randWords.append(dictWords[random.randint(0, len(dictWords))])
    i += 1

newStr = ""
for word in randWords:
    newStr += (word.rstrip() + " ")

print(newStr)
