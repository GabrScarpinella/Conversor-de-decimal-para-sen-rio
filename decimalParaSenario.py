def pospt(n):
    return n-int(n)

ent=float(input("Número a ser convertido: "))
entpospt=pospt(ent)
sinal=False #negativo?
if ent<0:
    ent*=-1
    sinal=True

algs={}
for i in range(100):
    algs[i]=ent%(6**(i+1))
    ent-=ent%(6**(i+1))
decs={}
for k in range(10):
    entpospt=6*pospt(entpospt)
    decs[k]=6*entpospt

arq=open("entparares.txt", "w")
if sinal:
    arq.write(f"-")
j=99
while j>=0:
    arq.write(f"{int(algs[j]/6**j)}")
    j-=1
arq.write(f".")
for l in range(10):
    arq.write(f"{int(decs[l]/6)}")
arq.close()
#coisa inteira só para tirar os zeros
f=open("entparares.txt", "r")
nsz=float(f.read())
f.close()
a=open("entparares.txt", "w")
a.write(f"{nsz}")
a.close()