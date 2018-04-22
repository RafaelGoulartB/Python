import random as rd
from time import sleep

##################
'''
Programa mostra que trocar de porta no meio do jogo,
Aumenta as chances de certar a porta, The Monty Hall problem
'''
##################

doors_img = [''' _______
|       |
|       |
|   1   |
|       |
|_______|''','''
 _______
|       |
|       |
|   2   |
|       |
|_______|''','''
 _______
|       |
|       |
|   3   |
|       |
|_______|''']

doors = [1,2,3]

door_prize = rd.choice(doors)

def choiceUser():
	'''Pega a porta que o usuário quiser.'''
	global doors, door_prize, choice_user
	while True:
		print(doors_img[0],doors_img[1],doors_img[2],'\n')
		choice_user = int(input("Choose a door 1 or 2 or 3: "))
		if choice_user < 1 or choice_user > 3:
			print("\nChoose a door valid\n")
			continue
		else:
			Check(choice_user)
			break

def Check(num):
	'''Faz o proceso de abrir uma porta e trocar de porta
	de acordo com o usuário.'''
	global door_prize, doors, choice_user
	print('\nI will open a door!\n')
	open_door = [1,2,3]

	if num != door_prize:
		open_door.remove(num)
		open_door.remove(door_prize)
		doors.remove(open_door[0])
	else:
		open_door.remove(num)
		open_door.remove(rd.choice(open_door))
		doors.remove(open_door[0])

	sleep(1.8)

	print('I opened the door {} and it is empty'.format(open_door[0]))
	sleep(1)
	while True: #Para trocar a porta escolhida
		print(doors_img[doors[0]-1],doors_img[doors[1]-1])
		print("\nYou picked up the door {}".format(choice_user))
		switch = str(input("\nDo you wanna switch the door?[Y/N] ")).lower().strip()[0]
		if switch == 'y':
			if choice_user == doors[0]:
				choice_user = doors[1]
			elif choice_user == doors[1]:
				choice_user = doors[0]
			WinOrNot()
			break
		elif switch == 'n':
			WinOrNot()
			break
		else:
			print("\n\033[31mAnwser YES or NO!\n\033[m")
			sleep(1.5)
def WinOrNot():
	'''Imprime o resultado, se o jogador ganhou ou não.'''
	global choice_user
	if choice_user == door_prize:
		print('')
		print('+=++=+'*10)
		print('\n\033[32mYou won the game, You choose the right door.\n\033[m')
		print('+=++=+'*10)
	else:
		print('\n\n\033[31mYou wrong the right door, try again!\033[m\n')


choiceUser()
