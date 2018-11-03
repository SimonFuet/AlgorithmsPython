# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 14:18:17 2018

@author: Simon
"""

import traceback

def test_function(f, array, validator, test_name):
    print("Testing " + f.__name__ + " on " + test_name + ": ", end="")
    try:
        f(array)
        assert validator(array)
    except AssertionError as error:
        print("incorrect result")
        return False
    except:
        print("unexpected exception")
        print(traceback.format_exc())
        return False
    else:
        print("OK")
        return True