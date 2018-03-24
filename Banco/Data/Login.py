#Pega as informações
data = open('Data/acc_passw.txt', 'r')
info = data.readline()
info = eval(info)
data.close()
times_try = 0

def login(): #Função para logar no sistema
	global times_try
	num_acc = int(input("\nNúmero da sua conta: "))
	
	while num_acc not in info: #Verificar se o número da conta existe
		print("Número da conta não existe, tente de novo!")
		num_acc = int(input("Número da sua conta: "))

	while num_acc in info: #Se o número da conta existir...
		num_pass = int(input("Digite sua senha: "))
		test = info.get(num_acc)
		
		if num_pass == test[0]: #Verificar se a senha está correta
			print("\nSenha correta!\n")
			break
			return 123
		elif times_try > 3: #Não tentar mais que 3 vezes
			print("\nVocê já tentou 3 vezes, volte mais tarde! ")
			break
		else: #Se a senha estiver errada
			times_try += 1
			print("\nSenha Errada, tente novamente!")
