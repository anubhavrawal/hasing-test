import more_itertools as mit
from random import randint as rndGen

from mid_value import *

#-------------Constant declaration------------
HASH_TABLE_ELEMENTS = 199

#------------------------------Probing list Generator------------------------------
def random_permute_generator(iterable, n=10):
    """Yield a random permuation of an iterable n times."""
    for _ in range(n):
        yield mit.random_permutation(iterable)

l = list(random_permute_generator(range(1,HASH_TABLE_ELEMENTS), n=200))
randSelection = rndGen(0, 199)
psudo_list = list(l[randSelection])
psudo_list.insert(0,0)
#----------------------------------------------------------------------------------

#Closed Hasing using Pseudo Random Probing method
class PseudoRandomHashTable:
    def __init__(self, size, hash_func_num ='H1'):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.hash_func_num = hash_func_num

    def __str__(self):
        result = ''
        #print(self.keys)
        count =0
        for slot in range(len(self.keys)):
            if self.keys[slot] != None:
                result += self.keys[slot] +' ' +  str(self.values[slot].Strength) +' \n'
                if count ==5:
                    return result
                count +=1

        return result
    
    #Using inbuild hash algorithm with modulus for finding the location within the table
    #Input Parameters: self(OpenHashTable)  -> The Class's defult parameters 
    #                    key(string)        -> The key to be hashed into the table
    #  
    #Returns:  An index for the given key
    def hashing_function(self, key):
        return hash(key) % self.size

    #Using mid-squared hash function for finding the index then using mod to fit it within the table
    #Input Parameters: self(OpenHashTable)  -> The Class's defult parameters 
    #                    key(string)        -> The key to be hashed into the table
    #  
    #Returns:  mid -> An index for the given key
    def hashing_function2(self, key):
        val = hash(key)
        val_sq = abs(val*val)
        mid = int(middle_three_digits(val_sq,self.size))
        return mid

    #Using folding on a string, summed 4 bytes at a time
    #Input Parameters: self(OpenHashTable)  -> The Class's defult parameters 
    #                    key(string)        -> The key to be hashed into the table
    #  
    #Returns:  An index for the given key
    def hashing_function3(self, key):
        sum_num = 0 
        mul = 1
        for i in range(len(key)):
            if i % 4 ==0: 
                mul =  1 
            else:
                mul * 256
            sum_num += ord(key[i]) * mul
  
        return int(abs(sum_num) % self.size)
    
    def get_slot(self, key):
        if self.hash_func_num =="H1":
            slot = self.hashing_function(key)
        elif self.hash_func_num =="H2":
            slot = self.hashing_function2(key)
        elif self.hash_func_num =="H3":
            slot = self.hashing_function3(key)

        i=1
        while self.keys[slot]:
            if slot >= self.size:
                slot = slot - self.size 
                
            slot = slot + psudo_list[i]
            
            if slot >= self.size:
                slot = slot - self.size 
            i+=1
        return slot
    
    #Inserts value into the hash table
    #Input Parameters: self  (OpenHashTable) -> The Class's defult parameters 
    #                  key   (string)        -> The key to be hashed into the table
    #                  value (Generic)       -> The value for key to be hashed into the table
    #  
    #Returns:  Nothing
    def set(self, key, value):
        slot = self.get_slot(key)
        self.keys[slot] = key
        self.values[slot] = value

    #Returns the value for the given key from the hash table
    #Input Parameters: self  (OpenHashTable) -> The Class's defult parameters 
    #                  key   (string)        -> The key to be hashed into the table
    #  
    #Returns:  Nothing    
    def get(self, key):
        if self.hash_func_num =="H1":
            slot = self.hashing_function(key)
        elif self.hash_func_num =="H2":
            slot = self.hashing_function2(key)
        elif self.hash_func_num =="H3":
            slot = self.hashing_function3(key)
        return_str = ''
        slot_loc = []
        strngth_mem = []
        i=0
        while self.keys[slot] and i<self.size:
            if self.keys[slot] == key:
                slot_loc.append(slot)
            slot = slot + psudo_list[i]
            if slot >= self.size:
                slot = slot - self.size 
            i+=1
        
        slot_loc = list(dict.fromkeys(slot_loc))

        for loc in slot_loc:
            strngth_mem.append(self.values[loc].Strength)

        if len(slot_loc) != 0:
            return_str = "slots: " + str(slot_loc) + "Strengths:" + str(strngth_mem)
        else:
            return_str = "NotFound"

        return return_str