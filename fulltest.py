from board import *
from quat_ht import *
from menace import *


men = Menace('x')
exitcodes = ['quit', 'q', 'bye', 'exit', 'quit()', 'exit()', 'terminate']
negative = ['no','nope','n']
positive = ['yes','yep','y']


for i in range(10):
	b = Board()
	exitb = False
	men.new_game('x')
	while not b.full() and b.detect_win() is None:
		b = men.make_move(b)
		b.print_board(nums=False)

		if b.full() or b.detect_win() is not None:
			break 
		while True:
			try:
				n = input()
				if n.lower() in exitcodes:
					exitb = True
					print("Thanks For Playing!")
					break
				else:
					try:
						n = int(n)
						if n in range(1,10) and b.arr[n-1] == '-' :
							b.arr[n-1] = 'o'
							break
						else:
							print("TRY AGAIN")
					except:
						print("TRY AGAIN")
			except:
				pass
		if exitb:
			exit()
		b.print_board()

	if b.detect_win() == 'o':
		men.learn(-1)
	elif b.detect_win() == 'x':
		men.learn(3)
	elif b.detect_win() == None:
		men.learn(1)

	for i in range(3):
		print()
	print(b.detect_win() + " WINS!")
	b.print_board()
	for i in range(3):
		print()
	#PLAYER INTERFACE 
	#print('Play Again?')
	# response = input()
	# if response.lower() in negative:
	# 	exit()
	# elif response.lower() not in positive:
	# 	print('INVALID RESPONSE')
	# 	while True:
	# 		print('Play Again?')
	# 		response = input()
	# 		if response.lower() in negative:
	# 			exit()
	# 		elif response.lower() not in positive:
	# 			print('INVALID RESPONSE')











