# this method takes in a .txt file and returns the number of words in the file
def get_total_number_of_words(file):
    wordCount = 0
    f = open(file, "r")
    # read first line
    line = f.readline()
    while line:
        # do whatever
        line = f.readline()
        wordCount = wordCount + 1
    f.close()
    return wordCount

# getTotalUniqueWords()
# this method returns the number of unique words in the novel
def get_total_unique_words(file):

# get20MostFrequentWords()
# get20MostInterestingFrequentWords()
# get20LeastFrequentWords()
# getFrequencyOfWord()
# getChapterQuoteAppears()
# generateSentence()
