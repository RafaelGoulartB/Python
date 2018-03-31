import pickle
import os
from time import sleep
class Oplogado():
	def __init__(self, numAcc):
		self.acc_acc = numAcc
		if __name__ == '__main__':
			self.data = open('acc_passw.pck', 'rb')
		else:
			self.data = open('Data/acc_passw.pck', 'rb') 
			self.info = pickle.load(self.data)
			self.data.close()
		self.infoAcc = self.info.get(self.acc_acc)

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
				self.info[self.acc_acc][1] += valor_dep
		
				if __name__ == '__main__':
					self.data = open('acc_passw.pck', 'wb')
				else:
					self.data = open('Data/acc_passw.pck', 'wb') 
				pickle.dump(self.info, self.data)


			elif choice == 'n':
				break
			else:
				print("\nDigite SIM ou NÃO!")
		