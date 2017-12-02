

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
        if tid not in range(5):
            raise AssertionError("attempted illegal transformation")
        if tid == 0:
            return self
        if tid == 1:
            return transform_counter_clockwise
        if tid == 2: 
            return transform_clockwise
        if tid == 3:
            return transform_180()
        if tid == 4:
            return transform_flip_horizontal()
        if tid == 5:
            return transform_flip_vertical()

    def find_soft_equal_tuple(self, table):
        for i in range(5):
            cboard = transform(i)
            if table.contains(cboard):
                back_id = i
                if i is 0:
                    back_id = 1
                elif i is 1:
                    back_id = 0
                return (cboard,back_id)
        return (None, -1)


    def print_board(self):
        print()
        for i in range(len(self.arr)):
            # print(i, end=' ')
            print(self.arr[i].upper(), end=' ')
            if i % 3 == 2:
                print()

    # will be relatively slow, maybe should save a var of the key
    def get_key(self):
        build = ''
        for e in self.arr:
            build += e.lower()
        return build
    
    def detect_win(self):
        '''
        Returns:
        None if Tie
        X if X Wins
        O if O Wins
        '''
