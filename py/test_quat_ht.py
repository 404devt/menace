import unittest
from quat_ht import *
from board import *

class testing_menace(unittest.TestCase):

	def test_ht_simple(self):
		bht = BoardHashTable()
		board = Board('-o-o-o-o-')
		bht.put(board)
		self.assertTrue(bht.contains(board))
		self.assertListEqual(bht.get_movelist(board),[2,0,2,0,2,0,2,0,2])

	def test_ht_a_bit_harder(self):
		bht = BoardHashTable()
		board = Board('-o-o-o-o-')
		bht.put(board)
		for i in range(6):
			self.assertTrue(bht.contains(board.transform(i)))
		self.assertListEqual(bht.get_movelist(board),[2,0,2,0,2,0,2,0,2])

	def test_ht__harder(self):
		bht = BoardHashTable()
		board = Board('------xo-')
		bht.put(board)
		expect = [False,False,False,False,True,False]
		topboard = Board('xo-------')
		for i in range(6):
			self.assertEqual(bht.contains(topboard.transform(i)),expect[i])
		self.assertListEqual(bht.get_movelist(board),[2,2,2,2,2,2,0,0,2])



if __name__ == "__main__":
	unittest.main()

	
