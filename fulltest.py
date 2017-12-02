from board import *
from quat_ht import *
from menace import *


men = Menace('x')



for i in range(10):
	b = Board()
	men.new_game('x')
	while not b.full() and b.detect_win() is None:
		b = men.make_move(b)
		b.print_board(nums=False)

		if b.detect_win() is not None:
			break 
		while True:
			try:
				n = int(input())
				if n in range(9) and b.arr[n] == '-' :
					b.arr[n] = 'o'
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

	for i in range(3):
		print()
	print(b.detect_win().upper() + " WINS!")
	b.print_board()
	for i in range(3):
		print()







