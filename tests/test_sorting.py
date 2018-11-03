# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 11:51:51 2018

@author: Simon
"""

from testutils import test_function
from context import sorting

def is_array_sorted(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

def is_array_sorted_reverse(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

def test_bubble_sort():
    def test_function_bubble_sort(array, test_name):
        return test_function(sorting.bubble_sort, array, is_array_sorted, test_name)
    
    allOk = True
    array = []
    allOk = allOk and test_function_bubble_sort(array, "empty list")
    
    array = [1]
    allOk = allOk and test_function_bubble_sort(array, "singleton list")
    
    array = [1, 2, 3, 4, 5]
    allOk = allOk and test_function_bubble_sort(array, "ordered list")
  
    array = [5, 4, 3, 2, 1]
    allOk = allOk and test_function_bubble_sort(array, "reverse ordered list")
  
    array = [2, 1, 4, 3, 5]
    allOk = allOk and test_function_bubble_sort(array, "non-ordered list 1")
  
    array = [5, 3, 2, 1, 4]
    allOk = allOk and test_function_bubble_sort(array, "non-ordered list 2")
 
    array = [10, -602, 575, -178, -883, 641, -825, 691, -955, -220, -72, 819,
             -433, 577, -98, -118, 376, 867, -89, -762, -61, 730, 783, 648, 
             -320, -982, 730, -231, -18, -122, 879, -140, 464, -600, 791, -229, 
             258, 557, -765, 993, 231, 565, -485, 60, -949, -414, -319, -288, 
             521, -287, 369, 258, -533, 671, 779, -873, -559, -457, -1000, -882,
             379, -222, -537, 819, -421, 245, 395, 310, -756, -694, 323, 572,
             750, -333, -492, -440, 487, -736, 713, 890, -232, 361, 564, -604,
             153, -154, -818, -543, 110, 159, -655, 592, 353, 45, 118, -61, 
             -841, -837, -771, -522]
    allOk = allOk and test_function_bubble_sort(array, "big list")

    print()
    if allOk:
        print("Bubble sort OK")
    else:
        print("Error in bubble sort")
    print()

def test_bubble_sort_reverse():
    def test_function_bubble_sort_reverse(array, test_name):
        return test_function(sorting.bubble_sort, array, is_array_sorted_reverse, test_name)
    
    allOk = True
    array = []
    allOk = allOk and test_function_bubble_sort_reverse(array, "empty list")
    
    array = [1]
    allOk = allOk and test_function_bubble_sort_reverse(array, "singleton list")
    
    array = [1, 2, 3, 4, 5]
    allOk = allOk and test_function_bubble_sort_reverse(array, "ordered list")
  
    array = [5, 4, 3, 2, 1]
    allOk = allOk and test_function_bubble_sort_reverse(array, "reverse ordered list")
  
    array = [2, 1, 4, 3, 5]
    allOk = allOk and test_function_bubble_sort_reverse(array, "non-ordered list 1")
  
    array = [5, 3, 2, 1, 4]
    allOk = allOk and test_function_bubble_sort_reverse(array, "non-ordered list 2")
 
    array = [10, -602, 575, -178, -883, 641, -825, 691, -955, -220, -72, 819,
             -433, 577, -98, -118, 376, 867, -89, -762, -61, 730, 783, 648, 
             -320, -982, 730, -231, -18, -122, 879, -140, 464, -600, 791, -229, 
             258, 557, -765, 993, 231, 565, -485, 60, -949, -414, -319, -288, 
             521, -287, 369, 258, -533, 671, 779, -873, -559, -457, -1000, -882,
             379, -222, -537, 819, -421, 245, 395, 310, -756, -694, 323, 572,
             750, -333, -492, -440, 487, -736, 713, 890, -232, 361, 564, -604,
             153, -154, -818, -543, 110, 159, -655, 592, 353, 45, 118, -61, 
             -841, -837, -771, -522]
    allOk = allOk and test_function_bubble_sort_reverse(array, "big list")

    print()
    if allOk:
        print("Bubble sort reverse OK")
    else:
        print("Error in bubble sort reverse")
    print()

test_bubble_sort()
test_bubble_sort_reverse()