'''
Q1. Calc number of letters and digits
sent = input("Enter a sentence")
lcount,dcount = 0,0
for i in sent:
	if i.isalpha():
		lcount += 1
	elif i.isdigit():
		dcount += 1
print(f"LETTERS {lcount}\nDIGITS {dcount}")
Q2. Special Character Check
sent = input()
special = "!@#$%^&*()[]{};:,./?><\'\""
count = 0
for i in sent:
	if i in special:
		print("String is not accepted")
		count += 1
		break
if count == 0:
	print("String is accepted")
Q3. Time from 12 hour to 24 hour format
time = input().split()
actualtime = time[0].split(':')
if time[1] == 'AM':
	if actualtime[0] == '12':
		actualtime[0] = '00'
	print(actualtime[0],actualtime[1],actualtime[2],sep = ':')
else:
	print(int(actualtime[0])+12,end = ':')
	print(actualtime[1],actualtime[2],sep = ':')
'''