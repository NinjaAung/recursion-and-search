#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    
    
    #return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index > len(array)-1:
        return None
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item): # names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    min = 0
    max = len(array)
    guess = (min+max)//2
    while array[guess] != item:
        guess = (min+max)//2
        print(min,max,guess)
        if min > max or guess > len(array)-1:
            return None
        if array[guess] < item:
            min = guess + 1
            continue
        elif array[guess] > item:
            max = guess - 1
            continue
    return guess
        

def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass

