from time import sleep
import os

acc_passw = {123456:1234,}
saldo = 0

def CriarAcc():
    num_acc = int(input("\nDigite o número da conta: "))
    while num_acc in acc_passw:
        print("Número da conta já está em uso, digite outro.")
        num_acc = int(input("Digite o número da conta: "))

    num_pass = int(input("Digite uma senha: "))
    while num_pass >= 10000: #Permitir somente senhas com 4 digitos
        print("Só é permitido senha com 4 digitos, digite outro.")
        num_pass = int(input("Digite uma senha: "))

def Deposito():
    global saldo
    print("\nConta criada, faça seu primeiro depósito.\n")
    volordep = float(input("Valor do primeiro depósito: "))
    while volordep < 30: #Deposito minimo de 30 reais
        print("O valor de deposito minimo é R$30,00.")
        volordep = float(input("Valor do primeiro depósito: "))
    saldo += volordep
    sleep(2)
    print("\nDeposito feito!\n")
    sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    val = str(input("Você quer criar uma nova conta?(S/N) ")).strip().upper()[0]
    if val == "S":
        CriarAcc()
        Deposito()
    else:
        break
