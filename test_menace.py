import unittest
from board import *

class testing_menace(unittest.TestCase):

	def test_board_construction_rows1(self):
		cstring = ''
		cstring += 'ooo'
		cstring += '---'
		cstring += 'xxx'

		board = Board(cstring)

		for i in range(len(board.arr)):
			if i // 3 is 0:
				self.assertEqual(board.arr[i],'o')
			elif i // 3 is 1:
				self.assertEqual(board.arr[i],'-')
			elif i // 3 is 2:
				self.assertEqual(board.arr[i],'x')

	def test_board_construction_cols1(self):
		cstring = ''
		cstring += 'o-x'
		cstring += 'o-x'
		cstring += 'o-x'

		board = Board(cstring)

		for i in range(len(board.arr)):
			if i % 3 is 0:
				self.assertEqual(board.arr[i],'o')
			elif i % 3 is 1:
				self.assertEqual(board.arr[i],'-')
			elif i % 3 is 2:
				self.assertEqual(board.arr[i],'x')

	def test_hardequal_1(self):
		b = Board()

		cstring = ''
		cstring += '---'
		cstring += '--\n-'
		cstring += '-  - -'

		board = Board(cstring)

		self.assertTrue(b.is_hard_equal(board))
		self.assertTrue(board.is_hard_equal(b))



if __name__ == "__main__":
	unittest.main()

	
