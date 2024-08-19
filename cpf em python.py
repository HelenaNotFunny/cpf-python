# Código para checar se é um CPF possível
def achar_digito(posição, lista):
    i = 0
    j = posição
    n = 0

    while i < (posição - 1) and j > 1:
        n = n + lista[i]*j
        i += 1
        j -= 1 

    n = 11 - (n%11)
    if n > 9:
        n = 0 
    return n

CPF = input("Digite o seu CPF:")
cpf_dado = []
cpf_certo = []

for numero in CPF:
    cpf_dado.append(int(numero))
    cpf_certo.append(int(numero))

cpf_certo[9] = achar_digito(10, cpf_certo)
cpf_certo[10] = achar_digito(11, cpf_certo)

if cpf_dado == cpf_certo:
    print("O CPF é possível")
else:
    print(f"O CPF não é possível, o certo seria:{cpf_certo}")