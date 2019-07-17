#!/usr/bin/env python3

#b, m , dicionario com os restos
eqs = []

def coprimos(x):
	for i in range(len(eqs)-1):
		if(eqs[i][1]%x==0 or x%eqs[i][1]==0):
			return 0
	return 1

def mdc(a, b, restos):
	if(a%b == 0):
		return b
	if(a%b != a):
		restos[a%b] = [1, a, -(a//b), b]
	return mdc(b, a%b, restos)


def mdcSemRestos(a, b):
	if(a%b == 0):
		return b
	return mdcSemRestos(b, a%b)

def inverso(r, restos, n1, n2, n3):
	if(r == 0): return 0
	#percorre lista de restos realizando as permutas
	for i in range(len(restos)):
		if restos[r][3] in restos:
			restos[restos[r][3]][0] *= restos[r][2] 
			restos[restos[r][3]][2] *= restos[r][2]
			restos[restos[r][3]][2] += restos[r][0]			
			r = restos[r][3]
	#vendo qual coeficiente é o inverso
	if(restos[r][1] == n1//mdcSemRestos(n1, n3)):
		if(restos[r][0] < 1 or restos[r][0] > n3):
			restos[r][0] = restos[r][0]%n3
		return  restos[r][0]
	if(restos[r][3] == n1//mdcSemRestos(n1, n3)):
		if(restos[r][2] < 1 or restos[r][2] > n3):
			restos[r][2] = restos[r][2]%n3
		return  restos[r][2]


def teoRestoChines(n):
	M, Mk, s, x0 = 1, [], [], 0
	for i in range(n):
		M = M * eqs[i][1]

	for i in range(n):
		Mk.append(M//eqs[i][1])
	
	for i in range(n):
		d = mdc(Mk[i],eqs[i][1],eqs[i][2])
		s.append(inverso(d, eqs[i][2], Mk[i], 1, eqs[i][1]))

	for i in range(n):
		x0 = x0 + Mk[i]*s[i]*eqs[i][0]

	return x0%M


n = int(input("Insira o numero de equações: "))
aux = 1
print("As entradas seguem a forma: x ≡ b (mod m)")
for i in range(n):
	print("Equação " + str(i+1) + ": ")
	eqs.append([])
	eqs[i].append(int(input('Digite o b:  ')))
	eqs[i].append(int(input('Digite o m:  ')))
	eqs[i].append({})
	if(not coprimos(eqs[i][1])):
		print("Valores de m não sao coprimos, parando operação")
		aux = 0
		break

if(aux):
	if(n<=1):
		print("Um sistema precisa de mais equações")
	else:
		print("Resposta -> " + str(teoRestoChines(n)))