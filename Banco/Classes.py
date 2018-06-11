class Conta(object):
	'''Classes com as funções da conta de um Banco'''
	def __init__(self, no, num, tp, sd):
		#Atributos
		self.__nome = no
		self.__numAcc = num
		self.__tipo = tp 	#Tipos: CC, Conta Corrente. CP, Conta Popança
		self.__saldo = sd
		self.__status = False

	#Métodos Especiais
	def __setNome(self, no):
		self.__nome = no
	def getNome(self):
		return self.__nome

	def __setNumAcc(self, num):
		self.__numAcc = num
	def getNumAcc(self):
		return self.__numAcc

	def __setTipo(self, tipo):
		self.__tipo = tipo
	def getTipo(self):
		return self.__tipo

	def __setSaldo(self, saldo):
		self.__saldo = saldo
	def getSaldo(self):
		return self.__saldo

	def __setStatus(self, status):
		self.__status = status
	def getStatus(self):
		return self.__status

	def getInfo(self):
		print("\n" + ("-=-" * 10))
		print("Nome: "+self.getNome())
		print("Num da Conta: "+ str(self.getNumAcc()))
		print("Tipo: " + self.getTipo())
		print("Saldo: "+ str(self.getSaldo()))
		print("Status: "+ str(self.getStatus()))
		print(("-=-" * 10 + "\n"))
	
	##Funções
	def trasferir():
		'''Transferir dinheiro para uma outra conta registrada'''
		pass
	
	def depositar(self, valor):
		'''Deposita um valor em uma conta se a conta tiver aberta'''
		if self.getStatus():
			self.__setSaldo(self.getSaldo() + valor)
		else:
			return False
	
	def sacar(self, valor):
		'''Saca o dinheiro da conta se a conta tiver aberta'''
		if valor <= self.getSaldo() and self.getStatus():
			self.__setSaldo(self.getSaldo() - valor)
		else:
			return False

	def abrirAcc(self):
		'''Abre a conta e da um bonus dependendo do tipo de conta'''
		self.__setStatus(True)
		if self.getTipo() == 'CC':
			self.__setSaldo(50)
		else:
			self.__setSaldo(100)
		return True

	def fecharAcc():
		'''Fecha a conta se ela não tiver em débito'''
		if self.getStatus() and self.getSaldo() >= 0:
			self.__setStatus = False
		else:
			return False

	def extrato(self):
		pass


	def salvarInfo():
		'''Salva as informações no banco de dados'''
		pass