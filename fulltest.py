from board import *
from quat_ht import *
from menace import *


men = Menace('x')

b = Board()

while not b.full():
	b = men.make_move(b)
	b.print_board(nums=True)

	b.arr[int(input())] = 'o'
	b.print_board()





