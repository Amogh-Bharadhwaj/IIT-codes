'''In the first line of input, accept a sequence of space-separated words. 
In the second line of input, accept a single word. If this word is not present in the sequence, print NO. 
If this word is present in the sequence,
print YES and in the next line of the output, print the number of times the word appears in the sequence.'''
sent = input().split(' ')
word = input()
flag = 0
for i in range(len(sent)):
    if word == sent[i]:
        flag += 1
if flag > 0:
    print("YES")
    print(flag)
else:
    print("NO")
