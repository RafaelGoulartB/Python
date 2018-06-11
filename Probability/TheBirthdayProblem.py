################
'''
Program show the probability that
each person in a party has a distinct birthday
'''
################

people_party = int(input("How many people has in the party? "))


def calcYear(n):
	omega = 365**n
	l = []
	for i in range(n+1):
		if i > 0:
			l.append(365-i+1)

		r = 0
	for x in l:
		if x == 365:
			r = x
		else:
			r *= x

	p_distinct = (r/omega)*100
	print("The probability of each person has a distinct birthday is {:.5f}%".format(p_distinct))


calcYear(people_party)
calcMonth(people_party)