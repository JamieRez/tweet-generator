import re
bookFilePath = "/Users/James/Downloads/bookOfText.txt"

def histogram(bookFile):
    #open bookfile
    book = open(bookFile)
    #get book words
    regex = re.compile('[,\.!?:/$()@]')
    bookWords = regex.sub('', book.read().lower()).split()

    uniqueWords = []
    histogramList = []

    for word in bookWords:
        if not word.isdigit() and word.isalpha():
            if word not in uniqueWords:
                uniqueWords.append(word)
                histogramList.append([word, 1])
            else:
                histogramList[uniqueWords.index(word)][1] += 1

    return histogramList


def unique_words(histogram):
    uniqueWords = []
    for histogramWord in histogram:
        if histogramWord[1] == 1:
            uniqueWords.append(histogramWord)
    return(len(uniqueWords))


def frequency(word, histogram):
    for histogramWord in histogram:
        if histogramWord[0] == word:
            return histogramWord[1]


print(histogram(bookFilePath))
print(unique_words(histogram(bookFilePath)))
print(frequency("cigar", histogram(bookFilePath)))
