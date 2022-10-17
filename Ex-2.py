from random import randint

maior=0
menor=0
contador=0
lista=[0]*50

while contador<=49:
    lista[contador]=randint(0, 20)
    soma=sum(lista)
    print(lista[contador])
    qtd=lista.count(9)
    if (lista[contador] > maior): 
        maior = lista[contador]
    if (lista[contador] < menor): 
        menor = lista[contador]
    contador=contador+1
print(soma)
print(qtd)
print(maior)
print(menor)