import random
numero_cpf = ''
for index in range (0,9):
  numero_cpf += str(random.randint(0,9))
print(f'Os nove numeros do cpf e {numero_cpf}')

i = 0
primeiroDigito = 0
for numero in range(10,1,-1):
  primeiroDigito += int(numero_cpf[i]) * numero
  i +=1
  
primeiroDigito *= 10 
primeiroDigito = primeiroDigito % 11
if primeiroDigito > 9 :
  print('O digito e 0')
else:
  print(f'O primeiro digito e {primeiroDigito}')

cpf_com_primeiro = numero_cpf + str(primeiroDigito)

soma = sum(int(cpf_com_primeiro[i]) * (11 - i) for i in range(10))
segundoDigito = (soma * 10) % 11
if segundoDigito > 9:
    segundoDigito = 0
print(f'O segundo dígito é {segundoDigito}')

print(f'O cpf gerado e:{numero_cpf[0:3]}.{numero_cpf[3:6]}.{numero_cpf[6:9]}-{primeiroDigito}{segundoDigito}')
  print(f'O segundo digito e {segundoDigito}')

