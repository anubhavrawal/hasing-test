from mid_value import *

#Closed Hasing using Linear Probing method
class LinerHashTable:
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
        key = str(key)
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
        
        i = slot

        while (True):
            if self.keys[i] == None:
                return i
            
            i = (i+1) % self.size
            
            if i==slot:
                break

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

        i = slot

        while(self.keys[i] != None):
            if self.keys[i] == key:
                slot_loc.append(i)
                strngth_mem.append(self.values[i].Strength)
            i = (i+1) %self.size

        
        if len(slot_loc) != 0:
            return_str = "slots: " + str(slot_loc) + " Strengths:" + str(strngth_mem)
        else:
            return_str = "NotFound"

        return return_str