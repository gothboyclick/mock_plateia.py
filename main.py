import random
#declara os valores
#lista = [a, b, c, d]
valor = int(0)
a = int()
b = int()
c = int()
d = int()
#faz a distribuição
#faz a saída em json
def cal_100(a,b,c,d,valor):
  valorNovo=int(0)
  a = int(0)
  b = int(0)
  c = int(0)
  d = int(0)
  #def val_novo(a,b,c,d,valorNovo):
    #valorNovo = int(0)
  valor_soma = a + b + c + d
    #return a,b,c,d,valorNovo
  valor = int(valor_soma)
  while(valor < 101):
    a = random.randint(0,100)
    b = random.randint(0,100)  
    c = random.randint(0,100)
    d = random.randint(0,100)
    print("declarando variáveis...")
  
  valor = val_novo(a,b,c,d,valorNovo)
  return valor
print(cal_100(a,b,c,d,valor))