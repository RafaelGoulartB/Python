from socket import *

def main():
	'''Interface of Program'''
	while True:
		print('''Select a option
	1 - To Get Ip
	0 - Exit''')

		res =int(input(": "))
		
		if res == 1:
			domain = str(input("\nDomain: "))
			ip = get_ip(domain, domain)
			print("The IP from {} is {}".format(domain, ip))
		
		elif res == 0:
			break
		
		else:
			print("\nInvalid Option\n")


def get_ip(x, y):
	'''To get a ip, x is a domain and y the same domain,
	get_ip(www.google.com www.google.com)'''
	
	x = gethostbyname(y)
	return x

main()