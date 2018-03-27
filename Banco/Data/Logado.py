data = open('Data/acc_passw.txt', 'r')
info = data.readline()
info = eval(info)
data.close()

def consultar_Saldo():
	global info
	