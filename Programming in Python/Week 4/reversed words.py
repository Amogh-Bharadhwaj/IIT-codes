'''Accept a sequence of comma-separated words as input. Reverse the sequence and print it as output.'''
l = input().split(',')
l.reverse()
word = ''
for i in range(len(l)):
	word = word + l[i]
	if i < len(l) - 1:
		word = word + ','
print(word)