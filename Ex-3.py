n=0
lista=[]
Par=[]
Impar=[]

while True:
    n=int(input("Insira um número: "))
    if n<0:
        break
    else: 
        lista.append(n)
print(lista)

for valor in lista:
    if (valor%2==0):
        Par.append(valor)
    else:
        Impar.append(valor)

print(Par)
print(Impar)
print(len(lista))