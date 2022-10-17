dados=[]
contador=0
v = []
r = set()

while contador<20:
    dados.append(int(input("Insira um numero")))
    contador=contador+1


for dado in dados:
    if dado not in v:
        v.append(dado)

print(v)
