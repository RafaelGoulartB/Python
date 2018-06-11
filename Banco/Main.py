from Classes import Conta

c1 = Conta("Rafael",111111,'CC',150)

c1.abrirAcc()

print(c1.saldo)

c1.depositar(5555)

print(c1.saldo)

c1.sacar(5555)

print(c1.saldo)
