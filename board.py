

class Board():

	def __init__(self, string='---------'):
		self.arr = []
		for c in string:
			if c is '\n':
				continue
			elif c is '':
				continue
			elif c is ' ':
				continue
			self.arr.append(c)

	def is_hard_equal(self,board):
		for i in range(len(self.arr)):
			if self.arr[i] != board.arr[i]:
				return False
		return True
