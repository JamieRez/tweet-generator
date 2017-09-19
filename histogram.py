def histogram(bookFile):
    #open bookfile
    book = open(bookFile)
    #get book line array
    bookLines = book.readlines()
    #get the word array
    bookWords = []
    for bookLine in bookLines:
        for bookWord in bookLine.split():
            bookWords.append(bookWord)

    class WordFreq:
        def __init__(self, word, freq):
            self.word = word
            self.freq = freq

    wordFreqArr = []
    for word in bookWords:
        newWordFreq = WordFreq(word, bookWords.count(word))
        if(wordFreqArr.count(newWordFreq) == 0):
            wordFreqArr.append(newWordFreq)

    print(wordFreqArr[30].word)


histogram("/Users/James/Downloads/bookOfText.txt")
