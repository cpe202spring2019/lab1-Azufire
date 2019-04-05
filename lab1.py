
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == None:        # if int_list is None, raise error
        raise ValueError("")
    if len(int_list) == 0:      # if int_list is empty, return None
        return None
    max_val = int_list[0]   #set default max value 
    for num in int_list:
        if num > max_val:   #compare values in list, replace max_val if current check is greater
            max_val = num
    return max_val 


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError("")
    if len(int_list) == 1:
        return [int_list[0]]
    return reverse_rec(int_list[1:]) + [int_list[0]]


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    pass
