"""
@author  JungBok Cho
@version 1.0
"""

import time

# Word list file
WORDSLIST = "words.txt"

# Pairs file
PAIRLIST = "pairs.txt"

# Dictionary to store every word
dictionary = dict()

# Minimum and Maximum of word length
wordMin, wordMax = 4, 6


def readWordsFile():
    """ Function to read word list file
        and store every word in the dictionary. """

    file = open(WORDSLIST, "r")
    for line in file:
        line = line.strip()
        if wordMin <= len(line) <= wordMax:
            # Store words separately depending on the word length
            if len(line) in dictionary:
                dictionary.get(len(line)).add(line)
            else:
                dictionary[len(line)] = set()
                dictionary.get(len(line)).add(line)
    file.close()


def readPairsFile():
    """ Function to read pairs file and
        call findPath function to initiate the BFS. """

    file = open(PAIRLIST, "r")
    count = 1

    for line in file:
        line = line.strip()
        tempList = line.split(" ")

        # Get beginning and ending words
        begWord = tempList.pop(0)
        endWord = tempList.pop(0)
        print(count, end="")
        print(". Beginning word: " + begWord + ", Ending word: " + endWord)

        # Call findPath function and measure the speed using timeit class
        start = time.time()
        result = findPath(dictionary.get(len(begWord)), begWord, endWord)
        end = time.time()

        # Print the result
        if isinstance(result, str):
            print(" - " + result)
        else:
            print("Path: ", end="")
            print(result)
        print("Time in seconds: {}".format(end - start))
        print()
        count += 1
    file.close()


def findPath(tempDictionary, begWord, endWord):
    """ Find the shortest path between words with Breath First Search """

    if len(begWord) != len(endWord):
        return "Length of pairs must be equivalent"
    elif not (wordMin <= len(begWord) <= wordMax and
              wordMin <= len(endWord) <= wordMax):
        return "Path does not exist"
    elif begWord == endWord:
        return [begWord]
    else:
        if begWord in tempDictionary and endWord in tempDictionary:
            visited = set()        # Set to check if word was visited
            visited.add(begWord)
            queue = [[begWord]]    # Create a queue of lists

            # Process until the queue is empty
            while len(queue) > 0:
                currList = queue.pop(0)

                # List to store a cut-down version of tempDictionary
                tempList = []
                smallerTempDictionary(currList, tempDictionary, tempList, visited)

                # Using unvisited words, create new currLists and append to the queue
                for currWord in tempList:
                    if currWord not in currList:
                        temp = currList[:]
                        temp.append(currWord)
                        if temp[-1] == endWord:
                            return temp
                        queue.append(temp)
    return "Path does not exist"


def smallerTempDictionary(currList, tempDictionary, tempList, visited):
    """ Create a cut-down version of tempDictionary """

    # Find all the words that are one letter apart
    # from the last word in the currList
    for i in range(len(currList[-1])):
        for char in range(ord('a'), ord('z') + 1):
            word = currList[-1][:i] + chr(char) + currList[-1][i + 1:]
            if word in tempDictionary and word != currList[-1] and word not in visited:
                tempList.append(word)
                visited.add(word)


def _main():
    """ Main function to print Hello and Goodbye messages
        and call readWordsFile and readPairsFile functions"""

    print("\nWelcome to Word Ladder program.\n")
    print("These are the files you are using:")
    print("Word List file:", WORDSLIST)
    print("Pair List file:", PAIRLIST, "\n")
    readWordsFile()
    readPairsFile()
    print("Thank you for playing this program!\n")


""" Call main method if this file is main module """
if __name__ == '__main__':
    _main()
