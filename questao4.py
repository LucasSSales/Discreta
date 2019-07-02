#!/usr/bin/env python3

def fatorar(num):
	fatores = []
	aux = num
	x = 2
	while x!=num+1:
		if(aux%x==0):
			fatores.append(x)
			aux = aux//x
		if(aux%x!=0):
			x+=1
	return fatores


def cleanList(f1, f2):
	if(len(f1) > len(f2)):
		f = f1
	else:
		f = f2

	start = f[0]
	i, j = 0, 0

	bases = []

	while 1:
		if i < len(f1):
			if f1[i] not in bases:
				bases.append(f1[i])
			#print(str(f1[i]))
			i += f1.count(f1[i])
		if j < len(f2):
			if f2[j] not in bases:
				bases.append(f2[j])
			#print("  " + str(f2[j]))
			j += f2.count(f2[j])
		if( i >= len(f1) and j >= len(f2)):
			break

	return bases

def mmc(bases, f1, f2):
	saida = 1
	for item in bases:
		if(f1.count(item) > f2.count(item)):
			saida *= item**f1.count(item)
		else:
			saida *= item**f2.count(item)

	return saida


def mdc(bases, f1, f2):
	saida = 1
	for item in bases:
		if(f1.count(item) < f2.count(item)):
			saida *= item**f1.count(item)
		else:
			saida *= item**f2.count(item)

	return saida



n1 = int(input('Digita o primeiro:  '))
n2 = int(input('Digita o segundo:  '))
b = cleanList(fatorar(n1), fatorar(n2))
print(fatorar(n1), fatorar(n2))
print(b)

#print(fatorar(n1))
#print(fatorar(n2))
print("")
print(mmc(b, fatorar(n1), fatorar(n2)))
print(mdc(b, fatorar(n1), fatorar(n2)))