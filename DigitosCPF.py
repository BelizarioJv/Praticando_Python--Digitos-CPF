# Primeiro Digito
cpf = '70037622692'
i = 0
primeiroDigito = 0
for numero in range(10,1,-1):
  primeiroDigito += int(cpf[i]) * numero
  i +=1
  print(primeiroDigito)
  
#       Segundo Digito

primeiroDigito *= 10 
primeiroDigito = primeiroDigito % 11
if primeiroDigito > 9 :
  print('O digito e 0')
else:
  print(f'O primeiro digito e {primeiroDigito}')

cpf = '70037622692'
i = 0
segundoDigito = 0
for numero in range(11,1,-1):
  segundoDigito += int(cpf[i]) * numero
  i +=1
  print(segundoDigito)
  

segundoDigito *= 10 
segundoDigito = segundoDigito % 11
if segundoDigito > 9 :
  print('O digito e 0')
else:
  print(f'O segundo digito e {segundoDigito}')

