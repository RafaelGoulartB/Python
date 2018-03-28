import pickle
#Pega as informações
data = open('Data/acc_passw.pck', 'rb') 
info = pickle.load(data)
data.close()
#Variaveis Globais
times_try = logado = num_acc = 0
info_acc = []

class login():
	def __init__(self):
		self.num_acc = self.num_pass = 0
		self.info_acc = []

	def val(self):
		global logado
		if logado == 1:
			return 1

	def FazerLogin(self): #Função para logar no sistema
		global times_try, logado, info_conta
		self.num_acc = int(input("\nNúmero da sua conta: "))
		
		while self.num_acc not in info: #Verificar se o número da conta existe
			print("Número da conta não existe, tente de novo!")
			self.num_acc = int(input("Número da sua conta: "))
		while self.num_acc in info: #Se o número da conta existir...
			self.num_pass = int(input("Digite sua senha: "))
			self.info_acc = info.get(self.num_acc)
			
			if self.num_pass == self.info_acc[0]: #Verificar se a senha está correta
				print("\nSenha correta!\n")
				logado = 1
				
				break
			elif times_try > 3: #Não tentar mais que 5 vezes
				print("\nVocê já tentou 5 vezes, volte mais tarde! ")
				break
			else: #Se a senha estiver errada
				times_try += 1
				print("\nSenha Errada, tente novamente!")
