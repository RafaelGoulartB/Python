from time import sleep
import sys
sys.path.append('Data')
from CriarConta import *
from Login import *

print("--=-"* 15)
print("{:^60}".format("Banco Guarani"))
print("--=-"* 15,"\n")

def menu():
	print("Escolha sua opção:")
	option = int(input('''  [1] - Entrar na sua conta.
  [2] - Criar uma nova conta.
  [3] - Fechar a sua conta.
  [4] - Sair do Programa.
  :'''))

	if option == 1:
		login()

	elif option == 2:
		main_Criar()

menu()