contador=0
n=[]

while contador<6:
    n.append(int(input("Coloque um número")))
    contador+=1
n.reverse()
print(n)