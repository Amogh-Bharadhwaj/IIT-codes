'''Accept a space-separated sequence of positive real numbers as input. 
Convert each element of the sequence into the greatest integer less than or equal to it.
Print this sequence of integers as output, with a comma between consecutive integers.'''
l = input().split(' ')
word = ''
for i in range(len(l)):
	l[i] = float(l[i])//1
	word = word + str(int(l[i]))
	if(i < len(l)-1):
		word = word + ','
print(word)