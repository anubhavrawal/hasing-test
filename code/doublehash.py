from mid_value import *

DOUBLE_HASH_PRIME = 97

#Closed Hasing using Double Hash implementation
class DoubleHashTable:
    def __init__(self, size, hash_func_num ='H1'):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.hash_func_num = hash_func_num
        
    def __str__(self):
        result = ''
        #print(self.keys)
        #print(self.values)
        count = 0
        for element in self.keys:
            if element != None:
                #slot = self.hash_function(element)
                result += element +' ' +' \n' #+  str(self.values[slot].Strength) 
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
    
    #Uses the Prime number hash concept for finding the index for the hash table
    #Input Parameters: self(OpenHashTable)  -> The Class's defult parameters 
    #                    key(string)        -> The key to be hashed into the table
    #  
    #Returns:  An index for the given key
    def second_hash_function(self, key): 
        return DOUBLE_HASH_PRIME - (hash(key) % DOUBLE_HASH_PRIME)
    
    #Inserts value into the hash table
    #Input Parameters: self  (OpenHashTable) -> The Class's defult parameters 
    #                  key   (string)        -> The key to be hashed into the table
    #                  value (Generic)       -> The value for key to be hashed into the table
    #  
    #Returns:  Nothing
    def set(self, key, value):
        if self.hash_func_num =="H1":
            index = self.hashing_function(key)
        elif self.hash_func_num =="H2":
            index = self.hashing_function2(key)
        elif self.hash_func_num =="H3":
            index = self.hashing_function3(key)

        new_index = index
        if (self.keys[index] != None):
            index2 = self.second_hash_function(key)
            
            while(1):
                new_index = (new_index + index2) % self.size

                if (self.keys[new_index] == None):
                    self.keys[new_index] = key
                    self.values[new_index] = value
                    break

        else:
            self.keys[index] =key
            self.values[index] = value
        

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

        tmp_slot = self.second_hash_function(key)
        anchor_slot = tmp_slot
        found = 0
        new_slot = slot

        while(self.keys[slot] != None):
            if self.keys[slot] == key:
                slot_loc.append(slot)
            
            new_slot = (new_slot + tmp_slot) % self.size
            slot = new_slot
        
        slot_loc = list(dict.fromkeys(slot_loc))
        for loc in slot_loc:
            strngth_mem.append(self.values[loc].Strength)
        
        if len(slot_loc) != 0:
            return_str = "slots: " + str(slot_loc) + "Strengths:" + str(strngth_mem)
        else:
            return_str = "NotFound"

        return return_str