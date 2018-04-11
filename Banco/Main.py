from time import sleep
import sys
import pickle
sys.path.append('Data')
from CriarConta import * 
from Logado import *

#Variaveis Globais
times_try = logado = num_acc = 0

class login():
  def __init__(self):
    self.num_acc = self.num_pass = 0
    self.info_acc = []
    self.data = open('Data/acc_passw.pck', 'rb')
    self.info = pickle.load(self.data)
    self.data.close()

  def val(self):
    '''Faz a validação para o sistema saber se o usuario esta logado'''
    global logado
    if logado == 1:
      return 1

  def FazerLogin(self):
    '''Função para logar no sitema'''
    global times_try, logado, num_acc
    self.num_acc = int(input("\nNúmero da sua conta: "))
    
    while self.num_acc not in self.info: #Verificar se o número da conta existe
      print("Número da conta não existe, tente de novo!")
      self.num_acc = int(input("Número da sua conta: "))
    
    while self.num_acc in self.info: #Se o número da conta existir...
      self.num_pass = int(input("Digite sua senha: "))
      self.info_acc = self.info.get(self.num_acc)
      
      if self.num_pass == self.info_acc[0]: #Verificar se a senha está correta
        print("\nSenha correta!\n")
        num_acc = self.num_acc
        logado = 1
        break
      elif times_try > 3: #Não tentar mais que 5 vezes
        print("\nVocê já tentou 5 vezes, volte mais tarde! ")
        break
      else: #Se a senha estiver errada
        times_try += 1
        print("\nSenha Errada, tente novamente!")
x = login()

def menu():
  '''Imprime o menu de opçoẽs'''
  print("--=-"* 15)
  print("{:^60}".format("Banco Guarani"))
  print("--=-"* 15,"\n")
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
  elif option == 2:
    main_Criar()

def Opition():
  '''Imprime o menu de opçoẽs do usuario se estiver logado'''
  sleep(1.2)
  os.system('cls' if os.name == 'nt' else 'clear')
  while x.val() == 1:
    op_logado = int(input('''
  [1] - Fazer uma transferencia.
  [2] - Fezer um deposito.
  [3] - Sacar.
  [4] - Consultar Saldo.
  [0] - Sair do Programa.
  : '''))
    y = Oplogado(num_acc)
    if op_logado == 1:
      pass
    elif op_logado == 2:
      y.Depositar()
    elif op_logado == 3:
      y.Sacar()
    elif op_logado == 4:
      y.ConsultarSaldo()
    elif op_logado == 0:
      break
    else:
      print("Digite uma opção valída")
menu()