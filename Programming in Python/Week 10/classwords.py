'''Create a class named StringManipulation that has the following specification:

Attributes

words: list of strings, all of which will be in lower case

Methods

__init__: accept a list words as argument and assign it to the corresponding attribute

total_words: return the total number of words in words

count: accept an argument named some_word and return the number of times this word occurs in the list words
words_of_length: accept a positive integer length as argument and return a list of all the words in the list words that have a length equal to length

words_start_with: accept a character char as argument and return the list of all the words in words that start with char

longest_word: return the longest word in the list words; if there are multiple words that satisfy this condition, return the first such occurrence
palindromes: return a list of all the words that are palindromes in words'''

class StringManipulation:
    def __init__(self,words):
        self.words = words
    def total_words(self):
        return len(words)
    def count(self,some_word):
        counter = 0
        for i in self.words:
            if i == some_word:
                counter += 1
        return counter
    def words_of_length(self,length):
        leng = []
        for i in self.words:
            if len(i) == length:
                leng.append(i)
        return leng
    def words_start_with(self,char):
        ch = []
        for i in self.words:
            if i[0] == char:
                ch.append(i)
        return ch
    def longest_word(self):
        maxi = 0
        word = ''
        for i in self.words:
            if len(i) > maxi:
                word = i
                maxi = len(i)
        return word
    def palindromes(self):
        pali = []
        for i in self.words:
            if i[::-1] == i:
                pali.append(i)
        return pali