'''Accept a sequence of words as input, append all these words to a list in the order in which they are entered, and print this list as output. 
The first line in the input is a positive integer nn that denotes the number of words in the sequence. The next nn lines will have one word on each line.'''
n = int(input())
x = ''
l = []
for i in range(n):
    x = str(input())
    l.append(x)
print(l)