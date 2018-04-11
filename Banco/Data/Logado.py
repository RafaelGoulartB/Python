import pickle
import os
from time import sleep
class Oplogado():
	def __init__(self, numAcc):
		self.num_acc = numAcc
		if __name__ == '__main__':
			self.data = open('acc_passw.pck', 'rb')
		else:
			self.data = open('Data/acc_passw.pck', 'rb') 
			self.info = pickle.load(self.data)
			self.data.close()
		self.infoAcc = self.info.get(self.num_acc)

	def ConsultarSaldo(self):
		'''Função para Consultar o Saldo'''
		print("\nSeu saldo no memento é de R${}.".format(self.infoAcc[1]))
		sleep(1.3)
	def Depositar(self):
		choice = 's'
		os.system('cls' if os.name == 'nt' else 'clear')
		while choice != 'n':
			choice = str(input("\nVocê quer fazer um deósito?[S/N] ")).strip().lower()[0]
			if choice == 's':
				valor_dep = float(input("\nDigite o Valor do depósito: R$"))
				self.info[self.num_acc][1] += valor_dep
		
				if __name__ == '__main__':
					self.data = open('acc_passw.pck', 'wb')
				else:
					self.data = open('Data/acc_passw.pck', 'wb') 
				pickle.dump(self.info, self.data)
				self.data.close()

			elif choice == 'n':
				break
			else:
				print("\nDigite SIM ou NÃO!")
		
	def Sacar(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		while True:
			choice = str(input("\nVocê quer realizar um saque?[S/N] ")).strip().lower()[0]
			if choice == 's':
				valor_sac = float(input("\nDigite o valor do saque: R$"))
				if valor_sac > self.info[self.num_acc][1]:
					print("\nVocê não tem dinheiro suficiente para o saque!")
					continue
				self.info[self.num_acc][1] -= valor_sac
				if __name__ == '__main__':
					self.data = open('acc_passw.pck', 'wb')
				else:
					self.data = open('Data/acc_passw.pck', 'wb')
				pickle.dump(self.info, self.data)
				self.data.close()
				sleep(0.5)
				print("\n Saque Feito! \n")
				sleep(0.8)
			if choice == 'n':
				break

	def Transferencia(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		while True:
			choice = str(input("Você quer fazer uma transferencia?[S/N] ")).strip().lower()[0]
			
			if choice == 's':
				acc_send = float(input("Digite o número da conta para transferencia: "))
				valor_trans = float(input("Digite o valor da transferencia: R$"))
				
				if valor_trans > self.info[self.num_acc][1]:
					print("\nVocê não tem dinheiro suficiente para a transferencia!")
					continue
				
				self.info[self.num_acc][1] -= valor_trans
				self.info[self.acc_send][1] += valor_trans

				if __name__ == '__main__':
					self.data = open('acc_passw.pck', 'wb')
				else:
					self.data = open('Data/acc_passw.pck', 'wb')
				pickle.dump(self.info, self.data)
				self.data.close()
				sleep(0.5)
				print("\n Transferencia Feita! \n")
				sleep(0.8)

			elif choice == 'n':
				break
			else:
				print("\nDigite SIM ou NÃO.\n")
