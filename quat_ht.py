'''Implementation of Quadratic Probing Hash Table'''
import re
import string
from board import *

class BoardHashTable:
    ''' Quadratic Hash Class '''
    def __init__(self, size=251):
        ''' Initialization of Hash Table '''
        self.tablesize = size
        self.count = 0
        self.arr = []
        for i in range(size):
            self.arr.append(None)

    def get_conflict_resolved_index(self,key):
        ''' Gets a free index in the table based on 
        the key with the proper conflict resolution strategy'''
        indx = self.myhash(key,self.get_tablesize())
        orig = indx
        inc = 0
        while self.arr[indx] is not None and self.arr[indx][0] != key:
            inc += 1
            indx = orig + inc**2
            indx %= self.get_tablesize()
        return indx


    def put(self, board, movelist=None):
        '''inserts the keyitem pair into the table, rehashes if table too large'''
        if self.get_load_fact() > 0.4:
            copy = self.arr
            oldct = self.count
            self.tablesize = self.tablesize*2 + 1
            self.count = 0
            self.arr = []
            for i in range(self.tablesize):
                self.arr.append(None)
            for tup in copy:
                if tup is not None:
                    self.put(Board(tup[0]),tup[1])
            if abs(oldct - self.count) >= 1:
                print("old=%d, new=%d" % (oldct,self.count))
                raise AssertionError("lost elements in rehash")


        indx = self.get_conflict_resolved_index(board.get_key())

        if self.arr[indx] == None:
            self.arr[indx] = (board.get_key(),board.make_movelist())
            self.count += 1
        else:
            raise AssertionError("double put")

    
    def contains(self,board):
        '''returns true if the key is indeed in the list'''
        indx = self.get_conflict_resolved_index(board.get_key())

        # print(self.arr[indx])
        if self.arr[indx] is None:
            return False

        if self.arr[indx][0] == board.get_key():
            return True

    def get_movelist(self, board):
        ''' Uses given key to find and return the item, key pair'''

        indx = self.get_conflict_resolved_index(board.get_key())

        if self.arr[indx] == None:
            raise LookupError()

        if self.arr[indx][0] == board.get_key():
            return self.arr[indx][1]


    def get_tablesize(self):
        '''returns Size of Hash Table'''
        return self.tablesize

    def get_load_fact(self):
        '''returns the load factor of the hash table'''
        return float(self.count) / float(self.tablesize)

    def myhash(self, key, table_size):
        '''hashes based on horners rule'''
        num = 0
        for i in range(min(len(key),9)):
            num = 31*num + self.strangeord(key[i])
        return num % table_size

    def strangeord(self, char):
        if char == '-':
            return 0
        elif char == 'o':
            return 1
        elif char == 'x':
            return 2
        else:
            return ord(char)

    def print_all_boards(self):
        for i in range(self.tablesize):
            if self.arr[i] is not None:
                Board(self.arr[i][0]).print_board()

    def menace_save(self,filename):
        f = open(filename, 'w')
        for i in range(self.tablesize):
            if self.arr[i] is not None:
                line = self.arr[i][0] + "|" + str(self.arr[i][1]) + '\n'
                f.write(line)
        f.close()


