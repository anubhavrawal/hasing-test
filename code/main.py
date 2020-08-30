#!/usr/bin/python3
import numpy as np
import copy
from random import randint as rndGen
import time

from data import Data 
from newCards import newCards
from ChainHash import *
from linprbHash import *
from doublehash import *
from pseudorand import *

#-------------Constant declaration------------
HASH_TABLE_ELEMENTS = 199
COUNT_IN_ONE_BAG = 125
#---------------------------------------------


#Selecting random entry from the array
#Input Parameters: itemsArray(numpy array) -> Is an array of newCard type elements within it.
#                                             Contatins all the infromation read from the txt file
#  
#Returns: search_key(string) -> A random element from the array that combines the rarity and itemname as a key
def random_selector(itemsArray):
   randSelection = rndGen(0, len(itemsArray)-1)
   search_key = itemsArray[randSelection].rarity +' '+itemsArray[randSelection].itemName

   #return 'Masterwork Hatchet'
   return search_key 

#Calculates time taken to search the hash table
#Both average and single
#Input Parameters: itemsArray(numpy array)   -> Is an array of newCard type elements within it.
#                                               Contatins all the infromation read from the txt file
#                    bag(numpy array)        -> The bag of 'n' hashtables
#                  total_bag_number(int)     -> Holds the total 
#              repitition(int)[optional]     -> IF A VALUE >1 IS PROVIDED : Returns the AVERAGE time taken to seach N items
#                                               IF NOTHING IS PROVIDED: Prints the time and element that was being searched 
#  
#Returns:  The total time to search for 1 element within the bag OR AVERAGE for n elements depending if repition is given or not
def time_table_search(itemsArray,bag, total_bag_number, repitition = 1):
   print_data = ''
   randomitem = random_selector(itemsArray)
   if repitition == 1:
      print("Looking for "+ randomitem +"... \n")

   start_time = time.perf_counter()
   for x in range(repitition):
      #When more than 1 bag count is given
      if total_bag_number !=1:
         track_bag =1
         for row in bag:
            recieved_str = row[0].get(randomitem)
            if recieved_str != 'NotFound':
               pass
               #print_data += "Bag: "+ str(track_bag) + " "
               #print_data +=  recieved_str + ' \n'
            
            track_bag +=1
      
      #When we are dealing with only one bag
      else:
         recieved_str = bag[0].get(randomitem)
         if recieved_str != 'NotFound':
            print_data += "Bag:"+ str(x)
            #print_data += recieved_str + ' \n'
      
      randomitem = random_selector(itemsArray)
   end_time = time.perf_counter()

   if repitition == 1:
      if len(print_data) == 0:
         print("Sorry the item you are looking for was not found!!!")
      print(print_data)
      return end_time-start_time

   return (end_time-start_time)/repitition

#Calles the Appropriate Hash function and type based on the parameters and 
# THEN appendes them into the 'tbag' array.
#Input Parameters: itemsArray(numpy array)   -> Is an array of newCard type elements within it.
#                                               Contatins all the infromation read from the txt file
#                  bag_count(int)            -> Holds the total 
#                 hash_req(stirng)           -> The type of hashtable 
#                 hash_func_num(stirng)      -> The Hashfunction to be used for the hashtable
#           
#Returns:  tBag(numpy array) -> An array of hashtables
def hasing_to_table(items_array, bag_count, hash_req, hash_func_num):
   #Row array declaration(row represents the number of bags)
   tBag = np.array([])
   seedlist = list(random_permute_generator(range(0,len(items_array)), n=200))
   randSelection = rndGen(0, 199) 
   psudo_list_bag_fill = list(l[randSelection])

   #Total numeber of entries in the list
   array_size = len(items_array)
   #Counter to keep track of how to extract elements
   seq_counter = 0

   #tack_succ_bag = 0

   #Assigning elements to the array from the linked list
   for i in range(bag_count):
      if hash_req == 'open':
         hash_table =  OpenHashTable(HASH_TABLE_ELEMENTS,hash_func_num)
      elif hash_req == 'Liner':
         hash_table =  LinerHashTable(HASH_TABLE_ELEMENTS,hash_func_num)
      elif hash_req == 'Double':
         hash_table =  DoubleHashTable(HASH_TABLE_ELEMENTS,hash_func_num)
      elif hash_req == 'Pseudo':
         hash_table =  PseudoRandomHashTable(HASH_TABLE_ELEMENTS,hash_func_num)

      for j in range(COUNT_IN_ONE_BAG):
         if (seq_counter >= len(psudo_list_bag_fill)):
            seq_counter = 0
         k = psudo_list_bag_fill[seq_counter]
         
         #received object
         recvdObj =items_array[k]
         newStrength = rndGen(int(recvdObj.minStrength ),int(recvdObj.maxStrength)+1)
         modyObj = newCards(recvdObj.itemName, newStrength ,recvdObj.rarity)

         key_for_hash = modyObj.rarity +' '+ modyObj.itemName
         
         hash_table.set(key_for_hash, modyObj)
         seq_counter += 1
      
      #When required to deal with the first bag/ also works when its the only bag
      if (i==0):
         tBag = np.append(tBag,hash_table)
         continue
      
      #For storing and dealing with >1 number of bags
      tBag = np.vstack((tBag, hash_table))
      #tack_succ_bag +=1
      
      #print("Bag "+ str(tack_succ_bag) + "is suceess!!! ")

   if bag_count ==1:
      print(tBag[0])

   elif bag_count <= 10:
      for x in range(bag_count):
         print("The content of bag " + str(x+1)+ " are as follows:::::")
         print(tBag[x][0])

   print("Single search: ", str(time_table_search(items_array, tBag, bag_count)))
   print("Average: ", str(time_table_search(items_array,tBag, bag_count,10)))
      
   return tBag
   



##---------------Main Function------------------------##
#Input Parameters: NONE
#  
#Returns: 0
def main():   
   items_array = np.array([])

   with open("input.txt", 'r') as file: # Use file to refer to the file object
      #Discard the first useless line
      data = file.readline()

      while(True):
         #All the other lines 
         data = file.readline()

         #Break if nothing is read from the file
         if (len(data) == 0):
            break 

         #remove the extra new line character and split the remaining based of "," deliminator
         data = data.strip('\n')
         tmp = data.split(',')

         #Assign the splitted data into the object
         newData = Data(tmp[0].title(), tmp[1], tmp[2], tmp[3].title())
         
         #Append the object into the array
         items_array = np.append(items_array, newData)

   #Filtering user input
   while True:
      try:
         n = int(input("Enter the number of bags(Must be >0): ")) #Take the number of input from the user
         if n<1:
            print("Sorry please try again!!!")
         else:
            break
      except ValueError:
         print("Please enter a numeric value greater than 0")

   tBag = hasing_to_table(items_array,n, 'open', "H1")
   tBag = hasing_to_table(items_array,n, 'open', "H2")
   tBag = hasing_to_table(items_array,n, 'open', "H3")

   tBag = hasing_to_table(items_array,n, 'Double',"H1")
   tBag = hasing_to_table(items_array,n, 'Double',"H2")
   tBag = hasing_to_table(items_array,n, 'Double',"H3")

   tBag = hasing_to_table(items_array,n, 'Liner',"H1")
   tBag = hasing_to_table(items_array,n, 'Liner',"H2") 
   tBag = hasing_to_table(items_array,n, 'Liner',"H3") 
   
   tBag = hasing_to_table(items_array,n, 'Pseudo',"H1")
   tBag = hasing_to_table(items_array,n, 'Pseudo',"H2")
   tBag = hasing_to_table(items_array,n, 'Pseudo',"H3") 


   return 0


#Calling main function
main()