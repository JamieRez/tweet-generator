"""Program that randomly picks words from a Dictionary."""
import sys
import random
file = open("/usr/share/dict/web2", "r")
numWords = int(sys.argv[1])

# Every word is separated by a newline
dictWords = file.readlines()

randWords = []
while(len(randWords) < numWords):
    randWords.append(dictWords[random.randint(0, len(dictWords))])

newStr = ""
for word in randWords:
    newStr += (word.rstrip() + " ")

print(newStr)
