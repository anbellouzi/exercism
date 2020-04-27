'''
Word Count
-------
Given a phrase, count the occurrences of each word in that phrase.

You may assume: - The count is case insensitive (ie "You", "you", and "YOU" are 3 uses of the same word)
                - The count is unordered; the tests will ignore how words and counts are ordered
                - Other than the apostrophe in a contraction all forms of punctuation are ignored
                - The words can be separated by any form of whitespace (ie "\t", "\n", " ")

RESTATE
In a string or words and characters, return the count of all english words ignoring all other chars
How long is the input list?

ASSUMPTIONS
We'll assume that input is a string containing words and special chars. 

BRAINSTORM
My initial idea is to loop over every char and saving it to another string called result.
When I reach a special char, it will be replaced by a white space in the result string  

EXPLAIN
Here we have a 0(n^2) solution in which we check if each char is a alphabetical letter.
Then we have another o(n^2) loop that checks if the word is already in hist,
then simply add 1 to its count, or register it in hist with value 1. 

TRADEOFFS
Overall it's less time efficient but is more memory efficient.
'''


def count_words(sentence):
    hist = {}                                           
    for c in sentence:
        if not c.isalnum():
            sentence = sentence.replace(c, " ")

    for word in sentence.split():
        word = word.lower()

        if word not in hist.keys():
            hist[word] = 1
        else:
            hist[word] += 1

    return hist


print(count_words("one fish two fish red fish blue fish"))

