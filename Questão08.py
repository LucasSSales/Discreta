#!/usr/bin/env python3

restos = {}
print("A entrada segue a forma: ax = b (mod m)")
n1 = int(input('Digite o a:  '))
n2 = int(input('Digite o b:  '))
n3 = int(input('Digite o m:  '))

def mdc(a, b):
	if(a%b == 0):
		return b
	if(a%b != a):
		restos[a%b] = [1, a, -(a//b), b]
	return mdc(b, a%b)

def mdcSemRestos(a, b):
	if(a%b == 0):
		return b
	return mdcSemRestos(b, a%b)

def inverso(r):
	#caso os numeros sejam multiplos
	if(len(restos)==0):
		return [1, n1, -(n1//n2), n2]
	#percorre lista de restos realizando as permutas
	for i in range(len(restos)):
		if restos[r][3] in restos:
			restos[restos[r][3]][0] *= restos[r][2] 
			restos[restos[r][3]][2] *= restos[r][2]
			restos[restos[r][3]][2] += restos[r][0]			
			r = restos[r][3]
	#vendo qual coeficiente é o inverso
	if(restos[r][1] == n1//mdcSemRestos(n1, n3)):
		return  restos[r][0]
	if(restos[r][3] == n1//mdcSemRestos(n1, n3)):
		return  restos[r][2]

def resolver():
	#setando variaveis
	A, B, M, d = n1, n2, n3, mdcSemRestos(n1, n3)
	saida = []
	#vendo a e m sao coprimos
	if(d != 1):
		#vendo se b não é divisivel pelo mdc de a e m
		if(n2%d!=0):
			return saida #nesse caso a saida e vazia
		A, B, M = n1//d, n2//d, n3//d #dividindo por d
	#restos.clear()
	#teorema 3
	Abarra = inverso(mdc(A, M))
	x = (Abarra*B)%M
	for i in range(d):
		saida.append(x + i*M)
	return saida


print("Valores possiveis para x = " +  str(resolver()))