menu = """
MENU

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = 0
limite = 500
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUES = 3

def mostrarExtrato(numero_depositos=0, numero_saques=0):
    print(extrato_deposito if numero_depositos !=0 else "Nenhum depósito feito hoje.")
    print(extrato_saque if numero_saques != 0 else "Nenhum saque realizado hoje.")
    print(f"O saldo atual da conta é de R${saldo:.2f} reais.")

while True:

    opcao = input(menu).lower()
    print("\n")
    
    if (opcao == "d"):
        deposito = float(input("Digite a quantidade que deseja depositar: "))
        
        if (numero_depositos == 0):
            extrato_deposito = ""
        
        if (deposito > 0):
            saldo += deposito
            print(f"Você depositou R${deposito:.2f} reais na sua conta com sucesso.")
            numero_depositos += 1
            extrato_deposito += f"{numero_depositos}º depósito de R${deposito:.2f} reais.\n"
        else:
            print("Número inválido, digite um valor positivo!")
            

        
    elif (opcao == "s"):
        if (numero_saques == LIMITE_SAQUES):
            print("Você alcançou o seu limite de saque diários!")
            continue
        
        saque = float(input("Digite o valor que deseja sacar: "))
        
        if (numero_saques == 0):
            extrato_saque = ""
        
        if (saque >= 500.00) or (saque < 1):
            print(f"O sistema não permite sacar R${saque:.2f} reais, tente outro valor!")
        elif (saldo < saque):
            print(f"Não é possível sacar R${saque:.2f} reais, sua conta possui apenas R${saldo:.2f} reais.")
        else:
            print(f"Saque de R${saque:.2f} reais feito com sucesso!")
            numero_saques += 1
            saldo -= saque
            extrato_saque += f"{numero_saques}º saque de R${saque:.2f} reais.\n"

        
    elif (opcao == "e"):
        mostrarExtrato(numero_depositos, numero_saques)

      
    elif (opcao == "q"):
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
