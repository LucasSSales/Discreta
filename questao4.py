#!/usr/bin/env python3

def fatorar(num):
	bases= []
	exp = {}
	aux = num
	x = 2
	while x!=num+1:
		if(aux%x==0):
			if x not in bases:
				bases.append(x)
			if x not in exp:
				exp[x] = 1
			else:
				exp[x] += 1
			aux = aux//x
		if(aux%x!=0):
			x+=1
	return exp


def getBases(e1, e2):
	saida = list(e1.keys())
	for i in e2.keys():
		if i not in saida:
			saida.append(i)
	return saida



def mmc(bases, f1, f2):
	saida = 1
	for item in bases:
		if item not in f1:
			f1[item] = 0
		if item not in f2:
			f2[item] = 0
		if(f1[item] > f2[item]):
			saida *= item**f1[item]
		else:
			saida *= item**f2[item]
	return saida


def mdc(bases, f1, f2):
	saida = 1
	for item in bases:
		if item not in f1:
			f1[item] = 0
		if item not in f2:
			f2[item] = 0
		if(f1[item] < f2[item]):
			saida *= item**f1[item]
		else:
			saida *= item**f2[item]
	return saida


n1 = int(input('Digita o primeiro:  '))
n2 = int(input('Digita o segundo:  '))
b = getBases(fatorar(n1), fatorar(n2))
print("MMC -> " + str(mmc(b, fatorar(n1), fatorar(n2))))
print("MDC -> " + str(mdc(b, fatorar(n1), fatorar(n2))))
