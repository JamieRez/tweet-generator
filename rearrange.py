import sys
import random
currentInput = sys.argv


def rearrange(myList):
    myList.pop(0)
    random.shuffle(myList)
    newStr = ""
    for word in myList:
        newStr += (word + " ")
    print(newStr)


rearrange(currentInput)
