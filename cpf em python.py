# Código para descobrir últimos dois digitos de um CPF
cpf = []
A = []

CPF = input("Digite os nove primeiros digitos do seu:")

for numero in CPF:
    cpf.append(int(numero))

# while a > 0:
    #A.append(a%10)
    #a = int(a/10)

# for i in range (8, -1, -1):
    #cpf.append(A[i])

i = 0
j = 10
n1 = 0

while i < 9 and j > 1:
    n1 = n1 + cpf[i]*j
    i += 1
    j -= 1 

n1 = 11 - (n1%11)
if n1 > 9:
    n1 = 0  

cpf.append(n1)

i = 0
j = 11
n2 = 0

while i < 10 and j > 1:
    n2 = n2 + cpf[i]*j
    i += 1
    j -= 1 

n2 = 11 - (n2%11)
if n2 > 9:
    n2 = 0

cpf.append(n2)

print(cpf)