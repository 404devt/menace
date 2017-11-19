

class Board():

	IND_CIRCLE = [0,1,2,5,8,7,6,3]

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
		if len(self.arr) != 9:
			raise AssertionError("invalid buildstring length")

	def is_hard_equal(self,board):
		for i in range(len(self.arr)):
			if self.arr[i] != board.arr[i]:
				return False
		return True

	def transform_circular(self, amount):
		rboard = Board()
		
		for i in range(len(self.IND_CIRCLE)):
			indx = (i+amount)%len(self.IND_CIRCLE)
			rboard.arr[self.IND_CIRCLE[indx]] = self.arr[self.IND_CIRCLE[i]]

		rboard.arr[4] = self.arr[4]
		return rboard

	def transform_clockwise(self):
		return self.transform_circular(2)

	def transform_counter_clockwise(self):
		return self.transform_circular(-2)

	def transform_180(self):
		return self.transform_circular(4)

	def transform_flip_vertical(self):
		rboard = Board()
		
		for i in range(len(self.IND_CIRCLE)):
			if i % 3 == 0:
				rboard.arr[i+2] = self.arr[i]
			elif i % 3 == 2:
				rboard.arr[i-2] = self.arr[i]
			else:
				rboard.arr[i] = self.arr[i]
		return rboard

	def transform_flip_horizontal(self):
		rboard = Board()
		
		for i in range(len(self.IND_CIRCLE)):
			if i // 3 == 0:
				rboard.arr[6+(i%3)] = self.arr[i]
			elif i // 3 == 2:
				rboard.arr[(i%3)] = self.arr[i]
			else:
				rboard.arr[i] = self.arr[i]
		return rboard

	def transform(self, tid):
		if tid not in range(1,6):
			raise AssertionError("attempted illegal transformation")
		if tid = 1:
			return 

	def print_board(self):
		print()
		for i in range(len(self.arr)):
			# print(i, end=' ')
			print(self.arr[i].upper(), end=' ')
			if i % 3 == 2:
				print()