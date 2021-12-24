'''filename is a text file that contains a collection of words in lower case, one word on each line. Write a function named get_freq that accepts filename as argument. It should return a dictionary where the keys are distinct words in the file, the values are the frequencies of these words in the file.'''


def get_freq(filename):
    d = dict()
    f = open(filename, 'r')
    lis = [x.strip() for x in f.readlines()]
    for s in lis:
        if s == '':
            break
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    return d