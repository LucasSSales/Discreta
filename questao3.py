#!/usr/bin/env python3

n = int(input('kk eae men, digita:'))
n2 = n
x = 2

while x!=n:
	if(n2%x==0):
		print(""+str(x))
		n2 = n2//x
	if(n2%x!=0):
		x+=1
