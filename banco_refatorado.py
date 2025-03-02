from datetime import datetime, date

menu = """
MENU

[u] Criar usuário
[c] Criar conta
[l] Listar contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
limite = 500
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUES = 3
lista_usuarios = [{'nome': 'gui', 'data_de_nascimento': '12/123/2345', 'cpf': '1231241212', 'endereco': 'paraiba'}, {'nome': 'reto', 'data_de_nascimento': '09/09/2009', 'cpf': '99481214', 'endereco': 'mata'}]
lista_contas = []

def calcularDeposito(saldo, deposito, extrato, numero_depositos): 
    saldo += deposito
    print(f"Você depositou R${deposito:.2f} reais na sua conta com sucesso.")
    extrato += f"{numero_depositos}º depósito de R${deposito:.2f} reais.\n"
    return saldo, extrato

def calcularSaque(saldo, saque, extrato, limite, numero_saques):
    if (saque >= limite) or (saque < 1):
        print(f"O sistema não permite sacar R${saque:.2f} reais, tente outro valor!")
    elif (saldo < saque):
        print(f"Não é possível sacar R${saque:.2f} reais, sua conta possui apenas R${saldo:.2f} reais.")
    else:
        print(f"Saque de R${saque:.2f} reais feito com sucesso!")
        numero_saques += 1
        saldo -= saque
        extrato += f"{numero_saques}º saque de R${saque:.2f} reais.\n"
    return saldo, extrato, numero_saques 

def mostrarExtrato(saldo, /, *, extrato, numero_depositos=0, numero_saques=0):
    if numero_depositos ==0:
        print("Nenhum depósito feito hoje.")
    if numero_saques ==0:
        print("Nenhum saque realizado hoje.")
    print(extrato)
    print(f"O saldo atual da conta é de R${saldo:.2f} reais.")

def verificarCpf(cpf):
    for user in lista_usuarios:
        if (user["cpf"] == cpf):
            return False
        
    return True

def criarUsuario(lista_usuarios):
    nome_de_usuario = input("Digite o nome do usuário: ")
    data_de_nascimento = input("Digite a data de nascimento: ")
    cpf = input("Digite o cpf: ")
    if (not verificarCpf(cpf)):
        print("Esse cpf já foi cadastrado no sistema!")
    else:
        endereco = input("Digite seu endereco: ")
        lista_usuarios.append({"nome": nome_de_usuario, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})

def verificarUsuario(cpf):
    for user in lista_usuarios:
        if (user["cpf"] == cpf):
            return user["nome"]
    
    return False
        
def criarConta(lista_contas):
    
    cpf = input("Digite o cpf do usuário que você deseja cadastrar: ")
    usuario = verificarUsuario(cpf)
    if (type(usuario) == str):
        numero_da_conta = len(lista_contas) + 1
        lista_contas.append({"agencia": "0001", "numero_da_conta": numero_da_conta, "usuario": usuario})
    else:
        print("Esse usuário não foi cadastrado!")

def listarContas():
    for conta in lista_contas:
        for chave, valor in conta.items():
            print(chave, valor)
        
        print()

while True:
    opcao = input(menu).lower()
    print("\n")
    
    if (opcao == "u"):
        criarUsuario(lista_usuarios)
    
    elif (opcao == "c"):
        criarConta(lista_contas)
        
    elif (opcao == "l"):
        listarContas()
    
    elif (opcao == "d"):   
        if (numero_depositos == 10):
            print(f"Você alcançou o limite de depósitos por hoje {datetime.strftime(date.today(), "%d/%m/%Y")}.")
            continue

        deposito = float(input("Digite a quantidade que deseja depositar: "))
        if (deposito > 0):
            numero_depositos += 1
            saldo, extrato = calcularDeposito(saldo, deposito, extrato, numero_depositos)
        else:
            print("Número inválido, digite um valor positivo!")
            
    elif (opcao == "s"):
        if (numero_saques == LIMITE_SAQUES):
            print("Você alcançou o seu limite de saque diários!")
            continue
        
        saque = float(input("Digite o valor que deseja sacar: "))
        saldo, extrato, numero_saques = calcularSaque(saldo=saldo, saque=saque, extrato=extrato, limite=limite, numero_saques=numero_saques)
        
    elif (opcao == "e"):
        mostrarExtrato(saldo, extrato=extrato, numero_depositos=numero_depositos, numero_saques=numero_saques)

    elif (opcao == "q"):
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
