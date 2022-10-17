lista=[]
contador=0

while contador<=14:
    lista.append(int(input("Insira um valor: ")))
    
    
    del(lista[0])
    contador+=1

lista[0]=lista[1]
lista[1]=lista[2]
lista[2]=lista[3]
lista[3]=lista[4]
lista[4]=lista[5]
lista[5]=lista[6]
lista[6]=lista[7]
lista[7]=lista[8]
lista[8]=lista[9]
lista[9]=lista[10]
lista[10]=lista[11]
lista[11]=lista[12]
lista[12]=lista[13]
lista[13]=lista[14]

print(lista)