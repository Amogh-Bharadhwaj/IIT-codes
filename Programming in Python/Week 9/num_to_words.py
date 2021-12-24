'''Write a function named num_to_words that accepts a square matrix of single digit numbers as argument. Within the function, create a file named words.csv. Write the matrix to the file by replacing the digits with their corresponding words. For example, num_to_words([[1, 2], [3, 4]]) should create the file words.csv with the following contents:
one,two
three,four'''


import pandas as pd
def num_to_words(mat):
    num_words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    words = []
    for i in mat:
        line = []
        for j in i:
            line.append(num_words[j])
        words.append(line)
    word = pd.DataFrame(words[1:], columns = words[0])
    word.to_csv('words.csv', index=False)