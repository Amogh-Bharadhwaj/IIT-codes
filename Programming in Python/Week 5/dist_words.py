'''The distance between two different letters in the English alphabet is defined as one more than the number of letters between them.
Alternatively, it can be defined as the number of steps needed to move from the alphabetically smaller letter to the larger letter.
This is always a non-negative integer. The distance between any letter and itself is always zero.
Write a function named distance that accepts two words as arguments and returns the distance between them.'''

def distance(word, sent):
    if len(word) == len(sent):
        l = word.split()
        m = sent.split()
        summ = 0
        for i in range(len(word)):
            summ += abs(ord(word[i]) - ord(sent[i]))
        return summ  
    else:
        return -1