import pickle
data = open('Data/acc_passw.pck', 'rb') 
info = pickle.load(data)
data.close()


class logado():
	def __init__(self):
		self.data = open('Data/DC.pck', 'rb')
		self.num_acc = pickle.load(self.data)
		self.data.close()
		

	def ConsultarSaldo(self):
		print(self.num_acc)

	