#Accept a sequence of comma-separated integers as input and print the maximum value in the sequence as output.
l = str(input())
n = l.split(',')
max = int(n[0])
for i in range(len(n)):
	if(int(n[i]) > max):
		max = int(n[i])
print(max)