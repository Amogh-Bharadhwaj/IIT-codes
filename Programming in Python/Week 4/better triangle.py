n = 0
while n not in range(5,21):
	n = int(input("Enter a number bw 5 and 20: "))
for i in range(n+1):
	for j in range(i):
		print('-', end = '')
	print('\\')
for i in range(6):
	print('-' , end = '')
print('|')
for i in reversed(range(n)):
	for j in reversed(range(n)):
		print('-', end = '')
	print('/')