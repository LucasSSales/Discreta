#!/usr/bin/env python3

#questao5 - euclides
def mdc(a, b):
	if(a%b == 0):
		return b
	return mdc(b, a%b)

n1 = int(input('Digita o primeiro:  '))
n2 = int(input('Digita o segundo:  '))

print("MDC -> " + str(mdc(n1, n2)))
