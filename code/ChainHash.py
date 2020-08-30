#Open Hashing (also called separate chaining)
from mid_value import *

class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    

class OpenHashTable:
    #The defult intilization operator for class
    def __init__(self, size=10, hash_func_num ='H1'):
        self.size = size
        self.table = [None] * self.size
        self.hash_func_num = hash_func_num

    #The defult string operator for class
    def __str__(self):
        result = ''
        count = 0
        for element in self.table:
            if element != None:
                while element:
                    result += element.key +' ' +  str(element.value.Strength) +' \n'
                    element = element.next
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

    #If the provided index was not empty it chains the values with each node being 'HashEntry' type
    #Input Parameters: self  (OpenHashTable) -> The Class's defult parameters 
    #                  entry (HashEntry)     -> The chained keys location
    #                  key   (string)        -> The key to be hashed into the table
    #                  value (Generic)       -> The value for key to be hashed into the table
    #  
    #Returns:  Nothing
    def rehash(self, entry, key, value):
        while entry:
            prev, entry = entry, entry.next

        if entry:
            entry.value = value
        else:
            prev.next = HashEntry(key, value)
            prev.next.prev = prev
    
    #Inserts value into the hash table
    #Input Parameters: self  (OpenHashTable) -> The Class's defult parameters 
    #                  key   (string)        -> The key to be hashed into the table
    #                  value (Generic)       -> The value for key to be hashed into the table
    #  
    #Returns:  Nothing
    def set(self, key, value):
        if self.hash_func_num =="H1":
            slot = self.hashing_function(key)
        elif self.hash_func_num =="H2":
            slot = self.hashing_function2(key)
        elif self.hash_func_num =="H3":
            slot = self.hashing_function3(key)

        entry = self.table[slot]

        if not entry:
            self.table[slot] = HashEntry(key, value)
        else:
            self.rehash(entry, key, value)
    
    #Returns the value for the given key from the hash table
    #Input Parameters: self  (OpenHashTable) -> The Class's defult parameters 
    #                  key   (string)        -> The key to be hashed into the table
    #  
    #Returns:  Nothing
    def get(self, key):
        if self.hash_func_num =="H1":
            hash_v = self.hashing_function(key)
        elif self.hash_func_num =="H2":
            hash_v = self.hashing_function2(key)
        elif self.hash_func_num =="H3":
            hash_v = self.hashing_function3(key)
        return_str = ''
        slot_loc = []
        strngth_mem = []
        if not self.table[hash_v]: 
            return_str = "NotFound"
        else:
            entry = self.table[hash_v]
            slot_count =  hash_v
            while entry:
                if entry.key == key:
                    slot_loc.append(slot_count)
                    strngth_mem.append(entry.value.Strength)
                entry = entry.next
            
            if len(slot_loc) != 0:
                return_str = "slots: " + str(slot_loc) + "Strengths:" + str(strngth_mem)
            else:
                return_str = "NotFound"
                

        return return_str