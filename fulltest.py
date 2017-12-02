from board import *
from quat_ht import *
from menace import *
from random import randint

men = Menace('x')
sec = Menace('o')


for i in range(250):
	b = Board()
	men.new_game('x')
	sec.new_game('o')
	while not b.full() and b.detect_win() is None:
		b = men.make_move(b)
		
		b.print_board(nums=False)

		if b.full() or b.detect_win() is not None:
			break 


		if b.count_token('x') -1 != b.count_token('o'):
			for i in range(100):
				print()
			print("AAAAAA MENACE PLAYED ON TOP OF SELF")
			# for i in range(len(men.move_history)):
			# 	mvboard = men.move_history[i][0]
			# 	print("FOR THIS BOARD:" + str( men.move_history[i][1]))
			# 	mvboard.print_board()
			# 	print(men.ht.get_movelist(mvboard))
			for i in range(100):
				print()


		while True:
			try:	
				if i % 3 == 1:
					n = int(input())
				else:
					b = sec.make_move(b)
					break
				if n in range(1,10) and b.arr[n-1] == '-' :
					b.arr[n-1] = 'o'
					break
			except:
				pass
			print("TRY AGAIN")
		
		b.print_board()

	if b.detect_win() == 'o':
		men.learn(-1)
	elif b.detect_win() == 'x':
		men.learn(3)
	elif b.detect_win() == None:
		men.learn(1)

	if not ( i % 3 == 1):
		
		# sec.ht.print_all_boards()
		

		if b.detect_win() == 'o':
			sec.learn(3)
		elif b.detect_win() == 'x':
			sec.learn(-1)
		elif b.detect_win() == None:
			sec.learn(1)


	for i in range(3):
		print()
	print(str(b.detect_win()) + " WINS!")
	b.print_board()
	for i in range(3):
		print()







