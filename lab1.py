
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    try:
        max_val = int_list[0]   #set default max value 
        for num in int_list:
            if num == None:     #if value in list is None, raise a ValueError
                raise ValueError("")
            if num > max_val:   #compare values in list, replace max_val if current check is greater
                max_val = num
        return max_val
    except IndexError:  #if int_list is None, return None
        print ("IndexError")
        return None  


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    pass

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    pass
