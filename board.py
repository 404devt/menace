

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

    def is_hard_equal(self, board):
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
        if tid not in range(6):
            raise AssertionError("attempted illegal transformation")
        if tid == 0:
            return self
        if tid == 1:
            return self.transform_counter_clockwise()
        if tid == 2: 
            return self.transform_clockwise()
        if tid == 3:
            return self.transform_180()
        if tid == 4:
            return self.transform_flip_horizontal()
        if tid == 5:
            return self.transform_flip_vertical()

    def find_soft_equal_tuple(self, table):
        for i in range(6):
            cboard = transform(i)
            if table.contains(cboard):
                back_id = i
                if i is 2:
                    back_id = 1
                elif i is 1:
                    back_id = 2
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
        None if No Win
        x if x Wins
        o if o Wins
        '''
        for i in range(6):
            if self.ddh('o', i):
                return 'o'
        for i in range(6):
            if self.ddh('x', i):
                return 'x'

    def make_movelist(self):
        l = []
        for i in range(9):
            l.append(2)
        return l


    def ddh(self, marker, rtnum):
        '''
        Helper Function
        For detect_win
        '''
        if (self.transform(rtnum)).testdiag(marker):
            return True
        elif (self.transform(rtnum)).testmid(marker):
            return True
        elif (self.transform(rtnum)).testtop(marker):
            return True
        return False

    def testdiag(self, marker):
        if self.arr[0] ==  marker and self.arr[4] == marker and self.arr[8] == marker:
            return True
        else:
            return False

    def testmid(self, marker):
        if self.arr[1] == marker and self.arr[4] == marker and self.arr[7] == marker:
            return True
        else:
            return False

    def testtop(self, marker):
        if self.arr[0] == marker and self.arr[1] == marker and self.arr[2] == marker:
            return True
        else:
            return False

