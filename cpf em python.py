# Código para descobrir últimos dois digitos de um CPF
def achar_digito(posição):
    i = 0
    j = posição
    n = 0

    while i < (posição - 1) and j > 1:
        n = n + cpf[i]*j
        i += 1
        j -= 1 

    n = 11 - (n%11)
    if n > 9:
        n = 0 
    return n

cpf = []
CPF = input("Digite os nove primeiros digitos do seu:")

for numero in CPF:
    cpf.append(int(numero))


cpf.append(achar_digito(10))
cpf.append(achar_digito(11))

print(cpf)