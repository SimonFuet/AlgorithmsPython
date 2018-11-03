# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 11:46:11 2018

@author: Simon
"""
    
def bubble_sort_reverse(array):
    bubble_sort(array, lambda x, y: x < y)

def bubble_sort(array, comparator=lambda x, y: x>y):
    """
    Sorts an array using a bubble sort algorithm
    Inputs:
        array: the list to sort
        comparator: function that compare two elements of the list.
                    Must take 2 arguments and return a boolean
    """
    if len(array) < 2:
        return
    try:
        if type(comparator(array[0], array[1])) != bool:
            raise ValueError("Function must take two arguments and return a bool")
    except ValueError as value_error:
        raise value_error
    except:
        raise ValueError("Incorrect comparator")
    last_index = len(array) - 1
    while last_index >= 0:
        last_change = -1
        for i in range(last_index):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                last_change = i
        last_index = last_change
