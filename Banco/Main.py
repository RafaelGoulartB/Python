from time import sleep
import sys
sys.path.append('Data')
from CriarConta import *
from Login import * 
x = login()

print("--=-"* 15)
print("{:^60}".format("Banco Guarani"))
print("--=-"* 15,"\n")

def menu():
  print("Escolha sua opção:")
	option = int(input('''  
  [1] - Entrar na sua conta.
  [2] - Criar uma nova conta.
  [3] - Fechar a sua conta.
  [0] - Sair do Programa.
  : '''))

	if option == 1:
		x.FazerLogin()
		Opition()
    num = x.FazerLogin() 
	elif option == 2:
		main_Criar()

def Opition():
  if x.val() == 1:
		op_logado = int(input('''
  [1] - Fazer uma transferencia.
  [2] - Fezer um deposito.
  [3] - Sacar.
  [4] - Consultar Saldo.
  [0] - Sair do Programa.
  : '''))


menu()