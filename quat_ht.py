'''Implementation of Quadratic Probing Hash Table'''
import re
import string

class HashTableQuadPr:
    ''' Quadratic Hash Class '''
    def __init__(self, size=10):
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
        if float(self.count +1)/float(self.get_tablesize()) > 0.3:
            copy = self.arr
            oldct = self.count
            self.tablesize = self.tablesize*2 + 1
            self.count = 0
            self.arr = []
            for i in range(self.tablesize):
                self.arr.append(None)
            for tup in copy:
                if tup is not None:
                    self.put(tup[0],tup[1])
            if abs(oldct - self.count) >= 1:
                print("old=%d, new=%d" % (oldct,self.count))
                raise AssertionError("lost elements in rehash")


        indx = self.get_conflict_resolved_index(board.get_key())

        if self.arr[indx] == None:
            self.arr[indx] = (key,self.make_movelist(movelist))
            self.count += 1
        else:
            raise AssertionError("double put")

    
    # def contains(self,key):
    #     '''returns true if the key is indeed in the list'''
    #     indx = self.get_conflict_resolved_index(key)

    #     # print(self.arr[indx])
    #     if self.arr[indx] is None:
    #         return False

    #     if self.arr[indx][0] == key:
    #         return True

    # def get_lines(self, key):
    #     ''' Uses given key to find and return the item, key pair'''

    #     indx = self.get_conflict_resolved_index(key)

    #     if self.arr[indx] == None:
    #         raise LookupError()

    #     if self.arr[indx][0] == key:
    #         return self.arr[indx][1]

    # def read_stop(self, filename):
    #     '''reads the stopwords from a file and inserts them into the table'''
    #     f = open(filename)
    #     while True:
    #         l = f.readline()
    #         if l:
    #             if l.endswith("\n"):
    #                 l = l[:-1]
    #             self.insert(l,None)
    #         else:
    #             break
    #     f.close()


    # def read_file(self, filename, stoptable):
    #     ''' Read File, Hashes into Table, and Filters Stop Words '''
    #     f = open(filename)
    #     didskip = True
    #     num = 1
    #     word = ''
    #     while True:
    #         character = f.read(1)
    #         if not character:
    #             break
    #         elif character is "'":
    #             pass
    #         elif character in string.ascii_letters or character in string.digits:
    #             word = word + character
    #             didskip = False
    #         elif not didskip or character is '\n':
    #             didskip = True              
    #             self.decide_to_insert_conditionally(word,stoptable,num)
    #             if character is '\n':
    #                 num += 1
    #             word = ''
    #     self.decide_to_insert_conditionally(word,stoptable,num)
    #     f.close()

    # def decide_to_insert_conditionally(self, word,stoptable,num):
    #     '''decides to insert the word based on if its valid'''
    #     if len(word) is 0:
    #         return
    #     try:
    #         float(word)
    #     except:
    #         if not self.is_in_stoptable(stoptable, word.lower()):
    #             self.insert(word.lower(),num)

    # def is_in_stoptable(self,stoptable,word):
    #     '''returns true if word is in the stoptable'''
    #     try:
    #         return stoptable.contains(word)
    #     except:
    #         return False

    # def sorted_ht_copy(self):
    #     '''returns a copy of the hashtable without nones and sorted'''
    #     ret = []
    #     for tup in self.arr:
    #         if tup != None:
    #             ret.append(tup)
    #     return sorted(ret)


    # def get_tablesize(self):
    #     '''returns Size of Hash Table'''
    #     return self.tablesize

    # def save_concordance(self, outputfilename):
    #     '''saves the concordance of the file based on the contents of the table'''
    #     ofile = open(outputfilename,"w")
    #     firstline = True
    #     for tup in self.sorted_ht_copy():
    #         if firstline:
    #             firstline = False
    #         else:
    #             ofile.write("\n")
    #         ofile.write(tup[0] + ":")
    #         for num in tup[1]:
    #             ofile.write("\t" + str(num))
    #     ofile.close()

    # def get_load_fact(self):
    #     '''returns the load factor of the hash table'''
    #     return float(self.count) / float(self.tablesize)

    # def myhash(self, key, table_size):
    #     '''hashes based on horners rule'''
    #     num = 0
    #     for i in range(min(len(key),9)):
    #         num = 31*num + ord(key[i])
    #     return num % table_size
