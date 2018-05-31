class Conta(object):
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
	#Métodos
	def trasferir():
		pass
	
	def depositar(self, valor):
		self.__setSaldo(self.getSaldo() + valor)

	def sacar(self, valor):
		if valor <= self.getSaldo():
			self.__setSaldo(self.getSaldo() - valor)
		else:
			return False

	def abrirAcc(self):
		self.__setStatus(True)
		if self.getTipo() == 'CC':
			self.__setSaldo(50)
		else:
			self.__setSaldo(100)
		return True

	def fecharAcc():
		self.__setStatus = False
		return True

	def salvarInfo():
		pass