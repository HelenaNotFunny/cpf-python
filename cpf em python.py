# Código para checar se é um CPF possível
def achar_digito(posição, lista): # Algoritmo para achar os últimos dois digitos de um cpf
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

CPF = input("Digite o seu CPF: ")
while len(CPF) != 11: # O número só será aceito se tiver a quantidade certa de digitos
    if len(CPF) < 11:
        CPF = input("O número digitado possui menos digitos que um cpf, digite novamente: ")
    if len(CPF) > 11:
        CPF = input("O número digitado possui mais digitos que um cpf, digite novamente: ")

cpf_dado = []
cpf_certo = []

for numero in CPF: #Transformando a string em lista
    cpf_dado.append(int(numero))
    cpf_certo.append(int(numero))

# Usando a função para os últimos dois digitos
cpf_certo[9] = achar_digito(10, cpf_certo)
cpf_certo[10] = achar_digito(11, cpf_certo)

# Formatando o CPF
CPF = ""
for i in range(11):
    CPF = CPF + str(cpf_certo[i])
    if i == 2 or i == 5:
        CPF = CPF + "."
    elif i == 8:
        CPF = CPF + "-" 
    
# Resultado
if cpf_dado == cpf_certo:
    print(f"O CPF {CPF} é possível")
else:
    print(f"O CPF dado não é possível, o certo seria: {CPF}")
    