lista1=[1,2,3,4,5,6,7,8,9,10]
lista2=["a","b","c","d","e","f","g","h","i","j"]
lista3=[0]*20

for i in range(20):
    if (i%2==0):
        lista3[0]=lista1[0]
        lista3[2]=lista1[1]
        lista3[4]=lista1[2]
        lista3[6]=lista1[3]
        lista3[8]=lista1[4]
        lista3[10]=lista1[5]
        lista3[12]=lista1[6]
        lista3[14]=lista1[7]
        lista3[16]=lista1[8]
        lista3[18]=lista1[9]
    else:
        lista3[1]=lista2[0]
        lista3[3]=lista2[1]
        lista3[5]=lista2[2]
        lista3[7]=lista2[3]
        lista3[9]=lista2[4]
        lista3[11]=lista2[5]
        lista3[13]=lista2[6]
        lista3[15]=lista2[7]
        lista3[17]=lista2[8]
        lista3[19]=lista2[9]

print(lista3)