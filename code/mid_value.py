#The middle_three_digits is borrowed from geeks for geeks website\
def middle_three_digits(i, table_size):
    mid = 0
    #print(i)
    s = str(abs(i))
    length = len(s)
    #assert length >= 3 , "Need odd and >= 3 digits"
    if (length % 2) != 0: 
        mid = length // 2
    else:
        mid = (length+1) // 2

    ret_val = int(s[mid-1:mid+2])
    
    if ret_val >= table_size:
        ret_val %=100
        if ret_val == 99:
            return ret_val
        else:
            return ret_val + 100
    return ret_val