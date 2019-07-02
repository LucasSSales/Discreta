#!/usr/bin/env python3

n = int(input('Digita:'))
n2 = n
x = 2
bases = []
exp = {}

while x!=n:
	if(n2%x==0):
		if x not in bases:
			bases.append(x)
		if x not in exp:
			exp[x] = 1
		else:
			exp[x] += 1
		print(""+str(x))
		n2 = n2//x
	if(n2%x!=0):
		x+=1

print(bases)
print(exp)
