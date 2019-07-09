#!/usr/bin/env python3

restos = {}
n1 = int(input('Digita o primeiro:  '))
n2 = int(input('Digita o segundo:  '))

def mdc(a, b):
	if(a%b == 0):
		return b
	if(a%b != a):
		restos[a%b] = [1, a, -(a//b), b]
	return mdc(b, a%b)

def coefLin(r):
	#caso os numeros sejam multiplos
	if(len(restos)==0):
		print("kk eae men")
		return [1, n1, -(n1//n2), n2]
	for i in range(len(restos)):
		if restos[r][3] in restos:
			restos[restos[r][3]][0] *= restos[r][2] 
			restos[restos[r][3]][2] *= restos[r][2]
			restos[restos[r][3]][2] += restos[r][0]			
			#print(restos[r][3])
			r = restos[r][3]
	if(restos[r][1] == n1):
		return  restos[r][0]
	if(restos[r][3] == n1):
		return  restos[r][2]




resto = mdc(n1, n2)
if(n1%n2==0):
	resto = 0
#print(restos)
exit = coefLin(resto)
print(exit)
print("Inverso de " + str(n1) + " mod " + str(n2) + " -> " + str(exit))

#print(restos)
