import random

wins_jogador = 0
wins_cpu = 0


def resetWins(Play, Sony):
	 Play = 0
	 Sony = 0

def getInput(msg):
	choice = input(msg + "\n>>> ")
	return choice

def game(Play, Sony):
	while Play < 3 and Sony < 3:

		par_impar = 0
		while par_impar not in [1, 2]:
			par_impar = int(getInput("Escolha:\n1 - Par\n2 - Impar"))

		num = -1
		while num not in range(0, 5):
			num = int(getInput("Escolha um número de 0 à 5"))

		random.seed()
		cpu_num = random.randint(0,5)
		print("Seu oponente escolheu", cpu_num)

		if (num + cpu_num) % 2 == 0:
			print("Par ganhou.\n")
			ganhador = 1
		else:
			ganhador = 2
			print("Impar ganhou.\n")

		if par_impar == ganhador:
			Play += 1
		else:
			Sony += 1

	novamente = 0
	while novamente not in [1, 2]:
		novamente = int(getInput("Você quer jogar denovo?\n1 - Sim\n2 - Não"))
	if novamente == 1:
		resetWins(Play, Sony)
		game(Play, Sony)
	else:
		print("Partidas Enceradas")

if __name__ == '__main__':
	game(wins_jogador, wins_cpu)