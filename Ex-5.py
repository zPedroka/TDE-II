dados=[]
contador=0
v = []
r = set()

while contador<=9:
    dados.append(int(input("Insira os números")))
    contador+=1


for dado in dados:
    if dado not in v:
        v.append(dado)
    else:
        r.add(dado)
print(v)
print(r)