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
		#Nome
	def __setNome(self, no):
		self.__nome = no
	@property
	def nome(self):
		return self.__nome
		
		#Número da conta
	def __setNumAcc(self, num):
		self.__numAcc = num
	@property
	def numAcc(self):
		return self.__numAcc
		
		#Tipo da Conta
	def __setTipo(self, tipo):
		self.__tipo = tipo
	@property
	def tipo(self):
		return self.__tipo
		
		#Saldo
	def __setSaldo(self, saldo):
		self.__saldo = saldo
	@property
	def saldo(self):
		return self.__saldo
		#Status destivada ou ativada
	def __setStatus(self, status):
		self.__status = status
	@property
	def status(self):
		return self.__status


	def trasferir():
		'''Transferir dinheiro para uma outra conta registrada'''
		pass
	
	def depositar(self, valor):
		'''Deposita um valor em uma conta se a conta tiver aberta'''
		if self.status:
			self.__setSaldo(self.saldo + valor)
		else:
			return False
	
	def sacar(self, valor):
		'''Saca o dinheiro da conta se a conta tiver aberta'''
		if valor <= self.saldo and self.status:
			self.__setSaldo(self.saldo - valor)
		else:
			return False

	def abrirAcc(self):
		'''Abre a conta e da um bonus dependendo do tipo de conta'''
		self.__setStatus(True)
		if self.tipo == 'CC':
			self.__setSaldo(self.saldo + 50)
		else:
			self.__setSaldo(self.saldo + 100)
		return True

	def fecharAcc():
		'''Fecha a conta se ela não tiver em débito'''
		if self.status and self.saldo >= 0:
			self.__setStatus = False
		else:
			return False

	def extrato(self):
		pass


	def salvarInfo():
		'''Salva as informações no banco de dados'''
		pass

