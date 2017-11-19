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
				self.assertNotEqual(board.arr[i],'-')
				self.assertNotEqual(board.arr[i],'x')
			elif i // 3 is 1:
				self.assertEqual(board.arr[i],'-')
				self.assertNotEqual(board.arr[i],'o')
				self.assertNotEqual(board.arr[i],'x')
			elif i // 3 is 2:
				self.assertEqual(board.arr[i],'x')
				self.assertNotEqual(board.arr[i],'o')
				self.assertNotEqual(board.arr[i],'-')

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

	def test_board_hardequal_1(self):
		b = Board()

		cstring = ''
		cstring += '---'
		cstring += '--\n-'
		cstring += '-  - -'

		board = Board(cstring)

		cstring = ''
		cstring += '-x-'
		cstring += '--\n-'
		cstring += '-  - -'

		nboard = Board(cstring)

		self.assertTrue(b.is_hard_equal(board))
		self.assertTrue(board.is_hard_equal(b))
		self.assertFalse(nboard.is_hard_equal(b))
		self.assertFalse(nboard.is_hard_equal(board))
		self.assertFalse(board.is_hard_equal(nboard))
		self.assertFalse(b.is_hard_equal(nboard))

	def test_board_tranform_clockwise1(self):
		cstring = ''
		cstring += 'x--'
		cstring += '-o-'
		cstring += 'x--'

		orig = Board(cstring)

		cstring = ''
		cstring += 'x-x'
		cstring += '-o-'
		cstring += '---'

		confirm = Board(cstring)

		transout = orig.transform_clockwise()

		failure = False

		for i in range(len(transout.arr)):
			if transout.arr[i] != confirm.arr[i]:
				failure = True

		if failure:
			orig.print_board()
			transout.print_board()
			confirm.print_board()

		for i in range(len(transout.arr)):
			self.assertEqual(transout.arr[i],confirm.arr[i])


	

	def test_board_tranform_clockwise2(self):
		cstring = ''
		cstring += 'x-x'
		cstring += 'ox-'
		cstring += 'x--'

		orig = Board(cstring)

		cstring = ''
		cstring += 'xox'
		cstring += '-x-'
		cstring += '--x'

		confirm = Board(cstring)

		transout = orig.transform_clockwise()

		failure = False

		for i in range(len(transout.arr)):
			if transout.arr[i] != confirm.arr[i]:
				failure = True

		if failure:
			orig.print_board()
			transout.print_board()
			confirm.print_board()

		for i in range(len(transout.arr)):
			self.assertEqual(transout.arr[i],confirm.arr[i])


	def test_board_tranform_counter_clockwise1(self):
		cstring = ''
		cstring += 'x--'
		cstring += '-o-'
		cstring += 'x--'

		orig = Board(cstring)

		cstring = ''
		cstring += '---'
		cstring += '-o-'
		cstring += 'x-x'

		confirm = Board(cstring)

		transout = orig.transform_counter_clockwise()

		failure = False

		for i in range(len(transout.arr)):
			if transout.arr[i] != confirm.arr[i]:
				failure = True

		if failure:
			orig.print_board()
			transout.print_board()
			confirm.print_board()

		for i in range(len(transout.arr)):
			self.assertEqual(transout.arr[i],confirm.arr[i])


	def test_board_tranform_counter_clockwise2(self):
		cstring = ''
		cstring += 'x-x'
		cstring += 'ox-'
		cstring += 'x--'

		orig = Board(cstring)

		cstring = ''
		cstring += 'x--'
		cstring += '-x-'
		cstring += 'xox'

		confirm = Board(cstring)

		transout = orig.transform_counter_clockwise()

		failure = False

		for i in range(len(transout.arr)):
			if transout.arr[i] != confirm.arr[i]:
				failure = True

		if failure:
			orig.print_board()
			transout.print_board()
			confirm.print_board()

		for i in range(len(transout.arr)):
			self.assertEqual(transout.arr[i],confirm.arr[i])

	def test_board_tranform_180(self):
		cstring = ''
		cstring += 'x--'
		cstring += '-o-'
		cstring += 'x--'

		orig = Board(cstring)

		cstring = ''
		cstring += '--x'
		cstring += '-o-'
		cstring += '--x'

		confirm = Board(cstring)

		transout = orig.transform_180()

		failure = False

		for i in range(len(transout.arr)):
			if transout.arr[i] != confirm.arr[i]:
				failure = True

		if failure:
			orig.print_board()
			transout.print_board()
			confirm.print_board()

		for i in range(len(transout.arr)):
			self.assertEqual(transout.arr[i],confirm.arr[i])


	def test_board_tranform_180_2(self):
		cstring = ''
		cstring += 'x-x'
		cstring += 'ox-'
		cstring += 'x--'

		orig = Board(cstring)

		cstring = ''
		cstring += '--x'
		cstring += '-xo'
		cstring += 'x-x'

		confirm = Board(cstring)

		transout = orig.transform_180()

		failure = False

		for i in range(len(transout.arr)):
			if transout.arr[i] != confirm.arr[i]:
				failure = True

		if failure:
			orig.print_board()
			transout.print_board()
			confirm.print_board()

		for i in range(len(transout.arr)):
			self.assertEqual(transout.arr[i],confirm.arr[i])

	def test_board_tranform_fl_v1(self):
		cstring = ''
		cstring += 'x--'
		cstring += '-o-'
		cstring += 'x--'

		orig = Board(cstring)

		cstring = ''
		cstring += '--x'
		cstring += '-o-'
		cstring += '--x'

		confirm = Board(cstring)

		transout = orig.transform_flip_vertical()

		failure = False

		for i in range(len(transout.arr)):
			if transout.arr[i] != confirm.arr[i]:
				failure = True

		if failure:
			orig.print_board()
			transout.print_board()
			confirm.print_board()

		for i in range(len(transout.arr)):
			self.assertEqual(transout.arr[i],confirm.arr[i])


	def test_board_tranform_fl_v2(self):
		cstring = ''
		cstring += 'x-x'
		cstring += 'ox-'
		cstring += 'x--'

		orig = Board(cstring)

		cstring = ''
		cstring += 'x-x'
		cstring += '-xo'
		cstring += '--x'

		confirm = Board(cstring)

		transout = orig.transform_flip_vertical()

		failure = False

		for i in range(len(transout.arr)):
			if transout.arr[i] != confirm.arr[i]:
				failure = True

		if failure:
			orig.print_board()
			transout.print_board()
			confirm.print_board()

		for i in range(len(transout.arr)):
			self.assertEqual(transout.arr[i],confirm.arr[i])

if __name__ == "__main__":
	unittest.main()

	
